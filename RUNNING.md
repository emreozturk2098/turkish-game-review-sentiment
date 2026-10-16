# Running and verifying the archive
## Verify the supplied materials without training
From the repository root, run:
```bash
python tools/check_archive.py
```
This uses only Python's standard library, parses Python/notebook files and checks the supplemental-source checksums. It does not import model libraries, scrape sites, fit models or establish reproduction of published metrics.

## Set up basic analysis tools
Use a separate virtual environment and install the basic analysis dependencies:
```bash
python -m venv .venv
# Activate .venv for your operating system, then:
python -m pip install -r requirements-analysis.txt
```
This unpinned list reflects the basic source imports; it is not an exact historical environment lock and does not guarantee compatibility of optional deep-learning variants.

## Project workflow and remaining dependencies
Use source/original/aspect_labeling_sentiment.py for the recovered dictionary-based labeling workflow and source/original/kufur_vs_removal.py for filtering. Change INPUT_PATH and OUTPUT_PATH or the corresponding source constants to a selected workbook under data/original. Review sheet and column names before execution; workbook variants represent different annotation/processing stages. Keyword labels are not automatically manual ground truth. A full original BERT training pipeline is not present; the archived BERT scores cannot be reproduced by these scripts alone.

## Evidence and scope
Original source archives and results are preserved. Packaging validation is separate from running the research. Missing original code, external data or hardware dependencies are documented rather than replaced with invented implementations.
