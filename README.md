# 证明的技艺

本仓库是 Heather Macbeth 的教材 [The Mechanics of Proof](https://hrmacbeth.github.io/math2001) 的中文本地化版本，并保留配套 Lean 代码。中文网页位于 `html/`，中文 PDF 为仓库根目录下的 `the_mechanics_of_proof_zh.pdf`。

Lean 源文件位于 `Math2001/` 与 `Library/`。本地验证 Lean 代码：

```powershell
lake exe cache get
lake build
```

中文文档由 `scripts/write_manual_translations.py` 中的人工译文映射生成。重新生成 HTML 与 `_sources`：

```powershell
python scripts\write_manual_translations.py
python scripts\translate_html_blocks.py apply
python scripts\normalize_chinese_html.py
python scripts\write_translated_sources.py
python scripts\check_chinese_translation.py
```

重新导出 PDF：

```powershell
node scripts\export_pdf.js
```

GitHub Actions 会在 `main` 分支上构建 Lean 项目、重新应用中文文档脚本、检查残留英文，并把 `html/` 部署到 `gh-pages` 分支，便于配置 GitHub Pages。
