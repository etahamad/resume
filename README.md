# Resume

Single-page monochrome LaTeX resume template designed for ATS readability.

## How to use this template

1. Fork or clone this repository:
   ```bash
   git clone https://github.com/etahamad/resume.git
   cd resume
   ```

2. Open `Omar_Hamad_Resume.tex` and replace the content with your own information, experience, education, and links.

3. Build the PDF using any of the options below:

### Option A: Overleaf (Recommended, no local setup)
- Create a new project on [Overleaf](https://www.overleaf.com).
- Upload or paste `Omar_Hamad_Resume.tex`.
- Click **Recompile** to preview and download your PDF.

### Option B: Local LaTeX
If you have TeX Live, MiKTeX, or MacTeX installed:
```bash
pdflatex Omar_Hamad_Resume.tex
```

### Option C: Python Builder (No LaTeX installation required)
If you prefer building without a LaTeX distribution:
```bash
pip install reportlab pymupdf
python build_pdf.py
```

### Option D: GitHub Actions Automated Release
Any push to the `main` branch triggers `.github/workflows/release.yml`, which compiles the LaTeX document and uploads the PDF to the `latest` GitHub Release automatically.
