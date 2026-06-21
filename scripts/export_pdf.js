#!/usr/bin/env node
const fs = require("fs");
const path = require("path");
const { spawnSync } = require("child_process");

const root = path.resolve(__dirname, "..");
const htmlDir = path.join(root, "html");
const out = path.join(root, "the_mechanics_of_proof_zh.pdf");

const pages = [
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
  "Index_of_Tactics.html",
  "Mainstream_Lean.html",
  "Homework.html",
];

function fileUrl(filePath) {
  return `file:///${filePath.replace(/\\/g, "/").replace(/#/g, "%23")}`;
}

function bodyOnly(file) {
  const html = fs.readFileSync(path.join(htmlDir, file), "utf8");
  const match = html.match(/<div itemprop="articleBody">([\s\S]*?)<\/div>\s*<\/div>\s*<footer>/);
  if (!match) {
    throw new Error(`Could not find article body in ${file}`);
  }
  return match[1]
    .replace(/<a class="headerlink"[\s\S]*?<\/a>/g, "")
    .replace(/href="(?!https?:|#|mailto:)([^"]+)"/g, `href="${fileUrl(htmlDir)}/$1"`);
}

function candidateBrowsers() {
  const env = process.env.CHROME_PATH || process.env.PUPPETEER_EXECUTABLE_PATH;
  const candidates = [
    env,
    "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
    "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe",
    "C:\\Program Files\\Microsoft\\Edge\\Application\\msedge.exe",
    "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe",
    "google-chrome",
    "google-chrome-stable",
    "chromium",
    "chromium-browser",
    "microsoft-edge",
  ].filter(Boolean);
  for (const candidate of candidates) {
    if (candidate.includes("\\") || candidate.includes("/")) {
      if (fs.existsSync(candidate)) {
        return candidate;
      }
    } else {
      const result = spawnSync(candidate, ["--version"], { encoding: "utf8" });
      if (!result.error && result.status === 0) {
        return candidate;
      }
    }
  }
  throw new Error("Could not find Chrome/Chromium/Edge. Set CHROME_PATH to a browser executable.");
}

const combined = `<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <base href="${fileUrl(htmlDir)}/">
  <title>证明的技艺</title>
  <link rel="stylesheet" href="_static/pygments.css">
  <link rel="stylesheet" href="_static/css/theme.css">
  <link rel="stylesheet" href="_static/css/custom.css">
  <style>
    @page { size: A4; margin: 18mm 16mm; }
    body {
      font-family: "Noto Serif CJK SC", "Source Han Serif SC", "Microsoft YaHei", serif;
      color: #202020;
      background: white;
      line-height: 1.55;
    }
    .document, .wy-nav-content { max-width: none; }
    .pdf-page { break-after: page; }
    .pdf-page:last-child { break-after: auto; }
    h1, h2, h3, h4 {
      font-family: "Noto Sans CJK SC", "Microsoft YaHei", sans-serif;
      break-after: avoid;
      color: #111;
    }
    pre, code { font-family: "Noto Sans Mono CJK SC", "Consolas", monospace; }
    pre { white-space: pre-wrap; word-break: break-word; }
    table, img, pre, .highlight { break-inside: avoid; }
    a { color: #2364aa; text-decoration: none; }
    .math { font-family: "Cambria Math", "Times New Roman", serif; }
    .headerlink, .wy-breadcrumbs, .wy-nav-side, .wy-nav-top, footer { display: none !important; }
  </style>
  <script>
    window.MathJax = {
      tex: { inlineMath: [["\\\\(", "\\\\)"]], displayMath: [["\\\\[", "\\\\]"]] },
      startup: { typeset: true }
    };
  </script>
  <script async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
</head>
<body>
${pages.map((file) => `<main class="pdf-page">${bodyOnly(file)}</main>`).join("\n")}
<script>
  (async () => {
    if (window.MathJax?.startup?.promise) {
      await window.MathJax.startup.promise;
    }
    if (document.fonts?.ready) {
      await document.fonts.ready;
    }
    window.status = "ready";
  })();
</script>
</body>
</html>`;

const tmp = path.join(root, "tmp", "pdfs");
fs.mkdirSync(tmp, { recursive: true });
const combinedPath = path.join(tmp, "the_mechanics_of_proof_zh.html");
fs.writeFileSync(combinedPath, combined, "utf8");
if (fs.existsSync(out)) {
  fs.unlinkSync(out);
}

const browser = candidateBrowsers();
const result = spawnSync(
  browser,
  [
    "--headless=new",
    "--disable-gpu",
    "--no-sandbox",
    "--allow-file-access-from-files",
    "--run-all-compositor-stages-before-draw",
    "--virtual-time-budget=30000",
    "--no-pdf-header-footer",
    "--print-to-pdf-no-header",
    `--print-to-pdf=${out}`,
    fileUrl(combinedPath),
  ],
  { encoding: "utf8" },
);

if (result.status !== 0) {
  process.stderr.write(result.stdout || "");
  process.stderr.write(result.stderr || "");
  throw new Error(`PDF export failed using ${browser}`);
}
if (!fs.existsSync(out) || fs.statSync(out).size < 1000) {
  throw new Error(`PDF was not created at ${out}`);
}
console.log(`Wrote ${out}`);
