#!/usr/bin/env python3
import re
from pathlib import Path

from bs4 import BeautifulSoup


ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "html"

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

TEXT_SELECTORS = [
    "div[itemprop='articleBody'] h1",
    "div[itemprop='articleBody'] h2",
    "div[itemprop='articleBody'] h3",
    "div[itemprop='articleBody'] h4",
    "div[itemprop='articleBody'] p",
    "div[itemprop='articleBody'] li",
    "div[itemprop='articleBody'] dt",
    "div[itemprop='articleBody'] dd",
]

ALLOWED_ENGLISH = {
    "Lean",
    "Mathlib",
    "GitHub",
    "Gitpod",
    "Gradescope",
    "VS",
    "Code",
    "Microsoft",
    "Research",
    "Fordham",
    "Heather",
    "Macbeth",
    "Mario",
    "Carneiro",
    "Jeremy",
    "Avigad",
    "Rob",
    "Lewis",
    "Patrick",
    "Massot",
    "Matthew",
    "Hertz",
    "Gabriel",
    "Ebner",
    "Scott",
    "Morrison",
    "Thomas",
    "Murrills",
    "David",
    "Renshaw",
    "TA",
    "API",
    "HTML",
    "PDF",
    "N",
    "Z",
    "Q",
    "R",
}


def has_chinese(text: str) -> bool:
    return any("\u4e00" <= ch <= "\u9fff" for ch in text)


def english_words(text: str) -> list[str]:
    stripped = re.sub(r"`[^`]*`", " ", text)
    stripped = re.sub(r"\\\([\s\S]*?\\\)", " ", stripped)
    stripped = re.sub(r"\\\[[\s\S]*?\\\]", " ", stripped)
    stripped = re.sub(r"\b[a-zA-Z]\b", " ", stripped)
    words = []
    for word in re.findall(r"[A-Za-z][A-Za-z0-9_'.-]*", stripped):
        if word in ALLOWED_ENGLISH:
            continue
        if "_" in word or "." in word or "'" in word:
            continue
        words.append(word)
    return words


def main() -> None:
    failures = []
    for path in sorted(HTML.glob("*.html")):
        if path.name not in CONTENT_PAGES:
            continue
        soup = BeautifulSoup(path.read_text(encoding="utf-8"), "lxml")
        for selector in TEXT_SELECTORS:
            for tag in soup.select(selector):
                for hidden in tag.select("a.headerlink"):
                    hidden.extract()
                text = " ".join(tag.get_text(" ").split())
                if not text or text == "¶":
                    continue
                if not english_words(text):
                    continue
                if not has_chinese(text) and len(english_words(text)) >= 3:
                    failures.append((path.name, text[:180]))
    for filename, text in failures[:200]:
        safe_text = text.encode("ascii", "backslashreplace").decode("ascii")
        print(f"{filename}: {safe_text}")
    if failures:
        raise SystemExit(f"{len(failures)} likely untranslated blocks")
    print("All checked article blocks contain Chinese text.")


if __name__ == "__main__":
    main()
