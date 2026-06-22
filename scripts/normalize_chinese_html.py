#!/usr/bin/env python3
import json
import re
from pathlib import Path

from bs4 import BeautifulSoup
from bs4.element import NavigableString


ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "html"
TRANSLATION_DIR = ROOT / "translations" / "zh_blocks"
TEMPLATE_DIR = ROOT / "translations" / "zh_blocks_template"

TITLE = "证明的技艺"

FALLBACK_TITLE_MAP = {
    "The Mechanics of Proof": "证明的技艺",
    "Preface": "前言",
    "About this book": "关于本书",
    "Why Lean?": "为什么使用 Lean？",
    "Contents and prerequisites": "内容与预备知识",
    "Note for instructors": "教师说明",
    "Acknowledgements": "致谢",
    "Proofs by calculation": "计算式证明",
    "Proving equalities": "证明等式",
    "Proving equalities in Lean": "在 Lean 中证明等式",
    "Tips and tricks": "提示与技巧",
    "Proving inequalities": "证明不等式",
    "A shortcut": "一种简便写法",
    "Proofs with structure": "有结构的证明",
    "Intermediate steps": "中间步骤",
    "Invoking lemmas": "调用引理",
    '"Or" and proof by cases': "“或”与分类证明",
    '"And"': "“且”",
    "Existence proofs": "存在性证明",
    "Parity and divisibility": "奇偶性与整除性",
    "Definitions; parity": "定义；奇偶性",
    "Divisibility": "整除性",
    "Modular arithmetic: theory": "模算术：理论",
    "Modular arithmetic: calculations": "模算术：计算",
    "Bézout's identity": "贝祖等式",
    "Proofs with structure, II": "有结构的证明（二）",
    '"For all" and implication': "“对所有”与蕴含",
    "“For all” and implication": "“对所有”与蕴含",
    '"If and only if"': "“当且仅当”",
    '"There exists a unique"': "“存在唯一”",
    "Contradictory hypotheses": "矛盾的假设",
    "Proof by contradiction": "反证法",
    "Logic": "逻辑",
    "Logical equivalence": "逻辑等价",
    "The law of the excluded middle": "排中律",
    "Normal form for negations": "否定的范式",
    "Induction": "归纳法",
    "Introduction": "引言",
    "Recurrence relations": "递推关系",
    "Two-step induction": "两步归纳法",
    "Strong induction": "强归纳法",
    "Pascal's triangle": "帕斯卡三角形",
    "The Division Algorithm": "带余除法定理",
    "The Euclidean algorithm": "欧几里得算法",
    "Number theory": "数论",
    "Infinitely many primes": "素数有无穷多个",
    "Gauss' and Euclid's lemmas": "高斯引理与欧几里得引理",
    "The square root of two": "二的平方根",
    "Functions": "函数",
    "Injectivity and surjectivity": "单射性与满射性",
    "Bijectivity": "双射性",
    "Composition of functions": "函数复合",
    "Product types": "积类型",
    "Sets": "集合",
    "Set operations": "集合运算",
    "The type of sets": "集合的类型",
    "Relations": "关系",
    "Reflexive, symmetric, antisymmetric, transitive": "自反、对称、反对称、传递",
    "Equivalence relations": "等价关系",
    "Index of Lean tactics": "Lean 策略索引",
    "Transitioning to mainstream Lean": "过渡到主流 Lean",
    "Homework": "作业",
    "Appendices": "附录",
    "Logical equivalences for negations": "否定的逻辑等价",
    "Values of the recursively defined function pascal": "递归定义函数 pascal 的取值",
    "Tactics in this book, and their mathlib originals": "本书策略及其 mathlib 原型",
    "Tactics in this book with no mathlib analogues": "本书中没有 mathlib 对应物的策略",
    "Advanced algorithms not used in this book": "本书未使用的高级算法",
}

UI_REPLACEMENTS = {
    "The Mechanics of Proof": TITLE,
    "The Mechanics of Proof, by Heather Macbeth": f"{TITLE}，Heather Macbeth 著",
    "Search docs": "搜索文档",
    "View page source": "查看页面源码",
    "Index": "索引",
    "Search": "搜索",
    "Next": "下一页",
    "Previous": "上一页",
    "Permalink to this headline": "此标题的永久链接",
    "Link to this heading": "链接到此标题",
    "Permalink to this table": "此表的永久链接",
    "Navigation menu": "导航菜单",
    "Mobile navigation menu": "移动端导航菜单",
    "Page navigation": "页面导航",
    "Footer": "页脚",
    "Contents": "目录",
    "Appendices": "附录",
    "Built with": "构建工具为",
    "using a": "使用",
    "theme": "主题",
    "provided by": "由",
    "Read the Docs": "Read the Docs",
}

STATIC_TEXT_REPLACEMENTS = {
    "Built with": "构建工具为",
    "using a": "使用",
    "provided by": "由",
    "Search Results": "搜索结果",
    "Your search did not match any documents. Please make sure that all words are spelled correctly and that you've selected enough categories.": "没有找到匹配的文档。请检查关键词拼写，并确认选择了足够的分类。",
}

ARTICLE_BLOCK_REPLACEMENTS = {
    r"Let \(a\) and \(b\) be integers, with \(b\) positive. Let \(r\) and \(s\) be integers, both in the range \(0 \le r < b\) , \(0 \le s < b\) and both congruent to \(a\) modulo \(b\) . Show that they are equal.": r'设 \(a\) 和 \(b\) 为整数，且 \(b\) 为正。设 \(r\) 和 \(s\) 为整数，二者都在范围 \(0 \le r < b\)、\(0 \le s < b\) 中，并且都与 \(a\) 模 \(b\) 同余。证明 \(r=s\)。',
}

PROTECTED_PARENTS = {"script", "style", "pre", "code", "math"}


def plain_text(html: str) -> str:
    return " ".join(BeautifulSoup(html, "html.parser").get_text(" ").split())


def load_heading_map() -> dict[str, str]:
    mapping = dict(FALLBACK_TITLE_MAP)
    template_items = {}
    if TEMPLATE_DIR.exists():
        for path in sorted(TEMPLATE_DIR.glob("*.json")):
            for item in json.loads(path.read_text(encoding="utf-8")):
                template_items[item["id"]] = item
    if not TRANSLATION_DIR.exists():
        return mapping
    for path in sorted(TRANSLATION_DIR.glob("*.json")):
        for item in json.loads(path.read_text(encoding="utf-8")):
            source_item = item if item.get("tag") else template_items.get(item.get("id", ""), item)
            if source_item.get("tag") not in {"h1", "h2", "h3", "h4"}:
                continue
            zh = item.get("zh", "")
            if zh:
                mapping[source_item["text"]] = plain_text(zh)
    return mapping


def translate_phrase(text: str, heading_map: dict[str, str]) -> str:
    leading = text[: len(text) - len(text.lstrip())]
    trailing = text[len(text.rstrip()) :]
    core = text.strip()
    if not core:
        return text
    table_label = re.fullmatch(r"Table(\s+[\d.]+)", core)
    if table_label:
        return f"{leading}表{table_label.group(1)}{trailing}"
    if core in heading_map:
        return f"{leading}{heading_map[core]}{trailing}"
    if core in UI_REPLACEMENTS:
        return f"{leading}{UI_REPLACEMENTS[core]}{trailing}"
    replaced = core
    combined = {**UI_REPLACEMENTS, **heading_map}
    for src, dst in sorted(combined.items(), key=lambda item: len(item[0]), reverse=True):
        replaced = replaced.replace(src, dst)
    for src, dst in STATIC_TEXT_REPLACEMENTS.items():
        replaced = replaced.replace(src, dst)
    return f"{leading}{replaced}{trailing}"


def set_inner_html(tag, html: str) -> None:
    tag.clear()
    parsed = BeautifulSoup(html, "html.parser")
    for node in list(parsed.contents):
        tag.append(node)


def normalize_article_blocks(soup: BeautifulSoup) -> None:
    for tag in soup.select("div[itemprop='articleBody'] p, div[itemprop='articleBody'] li, div[itemprop='articleBody'] dd"):
        text = plain_text(str(tag))
        replacement = ARTICLE_BLOCK_REPLACEMENTS.get(text)
        if replacement:
            set_inner_html(tag, replacement)


def normalize_caption_blocks(soup: BeautifulSoup) -> None:
    for caption in soup.select("div[itemprop='articleBody'] caption"):
        text = plain_text(str(caption))
        if "Values of the recursively defined function pascal" in text:
            caption_text = caption.select_one(".caption-text")
            if caption_text is not None:
                set_inner_html(
                    caption_text,
                    '递归定义函数 <code class="docutils literal notranslate"><span class="pre">pascal</span></code> 的取值',
                )


def is_inside_article_body(tag) -> bool:
    return tag.find_parent(attrs={"itemprop": "articleBody"}) is not None


def should_translate_article_node(path: Path, parent) -> bool:
    classes = set(parent.get("class") or [])
    if classes.intersection({"caption-number", "caption-text"}):
        return True
    if path.name in {"index.html", "latexindex.html"}:
        return parent.name in {"h1", "h2", "h3", "h4", "a", "strong"}
    return False


def is_protected_node(node: NavigableString) -> bool:
    parent = node.parent
    return parent is None or parent.find_parent(PROTECTED_PARENTS) is not None or parent.name in PROTECTED_PARENTS


def normalize_html(path: Path, heading_map: dict[str, str]) -> None:
    soup = BeautifulSoup(path.read_text(encoding="utf-8"), "lxml")
    if soup.html is not None:
        soup.html["lang"] = "zh-CN"

    normalize_article_blocks(soup)
    normalize_caption_blocks(soup)

    if soup.title and soup.title.string:
        soup.title.string.replace_with(translate_phrase(str(soup.title.string), heading_map))

    for tag in soup.find_all(True):
        for attr in ("title", "placeholder", "aria-label", "alt"):
            if attr in tag.attrs and isinstance(tag.attrs[attr], str):
                tag.attrs[attr] = translate_phrase(tag.attrs[attr], heading_map)

    for node in soup.find_all(string=True):
        if not isinstance(node, NavigableString) or is_protected_node(node):
            continue
        parent = node.parent
        if parent is None:
            continue
        if is_inside_article_body(parent) and not should_translate_article_node(path, parent):
            continue
        translated = translate_phrase(str(node), heading_map)
        if translated != str(node):
            node.replace_with(NavigableString(translated))

    path.write_text(str(soup), encoding="utf-8")


def normalize_documentation_options() -> None:
    path = HTML / "_static" / "documentation_options.js"
    text = path.read_text(encoding="utf-8")
    text = text.replace("LANGUAGE: 'None'", "LANGUAGE: 'zh_CN'")
    text = text.replace("VERSION: ''", "VERSION: '中文版'")
    path.write_text(text, encoding="utf-8")


def main() -> None:
    heading_map = load_heading_map()
    for path in HTML.glob("*.html"):
        normalize_html(path, heading_map)
    normalize_documentation_options()


if __name__ == "__main__":
    main()
