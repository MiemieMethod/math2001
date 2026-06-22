#!/usr/bin/env python3
import argparse
import copy
import json
import re
from pathlib import Path

from bs4 import BeautifulSoup
from bs4 import NavigableString


ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "html"
TRANSLATIONS = ROOT / "translations" / "zh_blocks.json"
TRANSLATION_DIR = ROOT / "translations" / "zh_blocks"

CONTENT_PAGES = {
    "index.html",
    "00_Introduction.html",
    "01_Proofs_by_Calculation.html",
    "02_Proofs_with_Structure.html",
    "03_Parity_and_Divisibility.html",
    "04_Proofs_with_Structure_II.html",
    "05_Logic.html",
    "06_Induction.html",
    "07_Number_Theory.html",
    "08_Functions.html",
    "09_Sets.html",
    "10_Relations.html",
    "Homework.html",
    "Index_of_Tactics.html",
    "Mainstream_Lean.html",
}

TRANSLATABLE_SELECTORS = [
    "div[itemprop='articleBody'] h1",
    "div[itemprop='articleBody'] h2",
    "div[itemprop='articleBody'] h3",
    "div[itemprop='articleBody'] h4",
    "div[itemprop='articleBody'] p",
    "div[itemprop='articleBody'] li",
    "div[itemprop='articleBody'] dt",
    "div[itemprop='articleBody'] dd",
    "div[itemprop='articleBody'] th",
    "div[itemprop='articleBody'] td",
]

SKIP_CLASSES = {"headerlink", "math", "notranslate"}


def normalize_space(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def block_text(tag) -> str:
    headerlinks = []
    for link in list(tag.select("a.headerlink")):
        placeholder = soup_marker(link)
        link.replace_with(placeholder)
        headerlinks.append((placeholder, link))
    text = normalize_space(tag.get_text(" "))
    for placeholder, link in reversed(headerlinks):
        placeholder.replace_with(link)
    return text


def soup_marker(tag):
    soup = tag if isinstance(tag, BeautifulSoup) else tag.find_parent()
    while soup is not None and not isinstance(soup, BeautifulSoup):
        soup = soup.find_parent()
    if soup is None:
        return NavigableString("")
    return soup.new_string("")


def is_translatable(tag) -> bool:
    text = block_text(tag)
    if not text or text in {"¶", ""}:
        return False
    if tag.name in {"script", "style", "pre", "code"}:
        return False
    if tag.name == "p" and tag.find_parent("li") is not None:
        return False
    classes = set(tag.get("class") or [])
    return not classes.intersection(SKIP_CLASSES)


def is_nested_block_candidate(tag) -> bool:
    if tag.name != "p":
        return False
    return tag.find_parent(["li", "dd", "th", "td"]) is not None


def iter_blocks(path: Path):
    soup = BeautifulSoup(path.read_text(encoding="utf-8"), "lxml")
    seen = set()
    for selector in TRANSLATABLE_SELECTORS:
        for tag in soup.select(selector):
            ident = id(tag)
            if ident in seen or not is_translatable(tag):
                continue
            seen.add(ident)
            yield soup, tag


def stable_id(path: Path, index: int) -> str:
    return f"{path.stem}:{index:04d}"


def extract() -> None:
    items = []
    by_file = {}
    for path in sorted(HTML.glob("*.html")):
        if path.name not in CONTENT_PAGES:
            continue
        index = 0
        for _soup, tag in iter_blocks(path):
            index += 1
            item = {
                "id": stable_id(path, index),
                "file": path.name,
                "tag": tag.name,
                "text": block_text(tag),
                "html": str(tag),
                "zh": "",
            }
            items.append(item)
            by_file.setdefault(path.stem, []).append(item)
    out = TRANSLATIONS.with_name("zh_blocks.template.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(items, ensure_ascii=False, indent=2), encoding="utf-8")
    template_dir = out.parent / "zh_blocks_template"
    template_dir.mkdir(parents=True, exist_ok=True)
    for stem, file_items in by_file.items():
        (template_dir / f"{stem}.json").write_text(
            json.dumps(file_items, ensure_ascii=False, indent=2), encoding="utf-8"
        )
    print(f"Wrote {len(items)} blocks to {out}")


def load_translations() -> dict[str, str]:
    return {item["id"]: item["zh"] for item in load_translation_items() if item.get("zh", "")}


def load_translation_items() -> list[dict]:
    data = []
    if TRANSLATION_DIR.exists():
        for path in sorted(TRANSLATION_DIR.glob("*.json")):
            data.extend(json.loads(path.read_text(encoding="utf-8")))
    elif TRANSLATIONS.exists():
        data = json.loads(TRANSLATIONS.read_text(encoding="utf-8"))
    else:
        raise FileNotFoundError(f"No translations found in {TRANSLATION_DIR} or {TRANSLATIONS}")
    return data


def build_translation_lookup() -> dict[tuple[str, str, str], str]:
    lookup = {}
    for item in load_translation_items():
        zh = item.get("zh", "")
        text = normalize_space(item.get("text", ""))
        tag = item.get("tag", "")
        item_id = item.get("id", "")
        if not zh or not text or ":" not in item_id:
            continue
        stem = item_id.split(":", 1)[0]
        key = (stem, tag, text)
        existing = lookup.get(key)
        if existing is None or existing == zh:
            lookup[key] = zh
    return lookup


def unwrap_matching_outer_tag(tag, html: str) -> str:
    if not re.search(r"</?[A-Za-z][^>]*>", html):
        return html
    parsed = BeautifulSoup(html, "html.parser")
    roots = [node for node in parsed.contents if not (isinstance(node, NavigableString) and not str(node).strip())]
    if len(roots) != 1:
        return html
    root = roots[0]
    if getattr(root, "name", None) != tag.name:
        return html
    return "".join(str(node) for node in root.contents)


def set_inner_html(soup: BeautifulSoup, tag, html: str) -> None:
    html = html.replace('\\"', '"')
    html = unwrap_matching_outer_tag(tag, html)
    headerlink = None
    link = tag.select_one("a.headerlink")
    if link is not None:
        headerlink = str(link)
    tag.clear()
    if not re.search(r"</?[A-Za-z][^>]*>", html):
        tag.append(NavigableString(html))
    else:
        template = BeautifulSoup("<template></template>", "lxml").template
        template.append(BeautifulSoup(html, "html.parser"))
        for node in list(template.contents):
            tag.append(node)
    if headerlink is not None:
        restored = BeautifulSoup(headerlink, "lxml")
        restored_body = restored.body
        restored_nodes = list(restored_body.contents if restored_body else restored.contents)
        for node in restored_nodes:
            tag.append(node)


def set_list_item_with_code(soup: BeautifulSoup, tag, html: str) -> None:
    html = html.replace('\\"', '"')
    if re.search(r"<p(?:\s|>)", html):
        parsed = BeautifulSoup(html, "html.parser")
        new_paragraphs = [node for node in parsed.contents if getattr(node, "name", None) == "p"]
        old_paragraphs = tag.find_all("p", recursive=False)
        for old, new in zip(old_paragraphs, new_paragraphs):
            set_inner_html(soup, old, "".join(str(node) for node in new.contents))
        for old in old_paragraphs[len(new_paragraphs) :]:
            old.decompose()
        return
    first_paragraph = tag.find("p", recursive=False)
    set_inner_html(soup, first_paragraph or tag, html)
    if first_paragraph is not None:
        for paragraph in tag.find_all("p", recursive=False)[1:]:
            paragraph.decompose()


def set_translated_block(soup: BeautifulSoup, tag, html: str) -> None:
    if tag.name == "li" and tag.select_one("pre"):
        set_list_item_with_code(soup, tag, html)
        return
    if tag.name in {"th", "td"}:
        paragraphs = tag.find_all("p", recursive=False)
        if len(paragraphs) == 1:
            set_inner_html(soup, paragraphs[0], html)
            return
    set_inner_html(soup, tag, html)


def iter_apply_blocks(soup: BeautifulSoup):
    article = soup.select_one("div[itemprop='articleBody']")
    if article is None:
        return
    for tag in article.find_all(["h1", "h2", "h3", "h4", "p", "li", "dt", "dd", "th", "td"]):
        if is_nested_block_candidate(tag) or not is_translatable(tag):
            continue
        yield tag


def apply() -> None:
    translations = build_translation_lookup()
    files_with_translations = {stem + ".html" for stem, _tag, _text in translations}
    applied = 0
    for path in sorted(HTML.glob("*.html")):
        if path.name not in CONTENT_PAGES:
            continue
        if path.name not in files_with_translations:
            continue
        soup = BeautifulSoup(path.read_text(encoding="utf-8"), "lxml")
        for tag in iter_apply_blocks(soup):
            zh = translations.get((path.stem, tag.name, block_text(tag)))
            if zh:
                set_translated_block(soup, tag, zh)
                applied += 1
        path.write_text(str(soup), encoding="utf-8")
    print(f"Applied {applied} translated blocks")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=["extract", "apply"])
    args = parser.parse_args()
    if args.command == "extract":
        extract()
    else:
        apply()


if __name__ == "__main__":
    main()
