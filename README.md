# Omar Hamad - Resume

[![Build and Release Resume PDF](https://github.com/etahamad/resume/actions/workflows/release.yml/badge.svg)](https://github.com/etahamad/resume/actions/workflows/release.yml)
[![Latest Release](https://img.shields.io/github/v/release/etahamad/resume?label=Latest%20PDF&color=black)](https://github.com/etahamad/resume/releases/latest)

Clean, ATS-friendly, single-page monochrome resume for **Omar Hamad** (Azure DevOps & Systems Engineer).

---

## 📥 Download Latest PDF

👉 **[Download Omar_Hamad_Resume.pdf](https://github.com/etahamad/resume/releases/download/latest/Omar_Hamad_Resume.pdf)**

---

## 🛠 Repository Structure

* **`Omar_Hamad_Resume.tex`**: The primary LaTeX source code. Formatted in standard, ATS-friendly monochrome typography.
* **`build_pdf.py`**: Standalone Python script using ReportLab to generate the pixel-perfect PDF locally in under 0.1s.
* **`Omar_Hamad_Resume.pdf`**: The pre-compiled, single-page PDF.
* **`.github/workflows/release.yml`**: CI/CD pipeline that automatically builds the PDF and publishes it to the `latest` GitHub Release upon every push to `main`.

---

## 🚀 How to Edit and Update

### Option 1: Edit on GitHub / Locally (Automated Release)
1. Edit `Omar_Hamad_Resume.tex` directly.
2. Commit and push your changes to the `main` branch.
3. The GitHub Actions workflow will automatically compile the new PDF and update the **[Latest Release](https://github.com/etahamad/resume/releases/latest)**.

### Option 2: Overleaf
1. Upload or copy-paste `Omar_Hamad_Resume.tex` into [Overleaf](https://www.overleaf.com).
2. Click **Recompile** to preview and download.

### Option 3: Local Python Generator
Run the local python generator without needing LaTeX installed:
```bash
pip install reportlab pymupdf
python build_pdf.py
```
