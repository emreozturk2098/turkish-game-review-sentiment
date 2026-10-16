# Original CS549 archive
The supplied Excel versions, original filtering script, report, slide deck and code document are preserved under `data/original/`, `source/` and `reports/original/`. Duplicate byte-identical workbooks are represented once in the manifest; similar filenames do not establish chronological order or a final annotation version.

`source/recovered_code_document.txt` preserves the code-document text. It includes dictionary-based aspect labeling and must not be confused with the team's BERT training pipeline. Team contribution roles in PROJECT_CONTEXT remain unchanged. Existing reported metrics are archived validation results, not newly reproduced scores.

Inspect workbook sheet schemas before joining variants: reviews, preprocessing results and aspect labels represent different pipeline stages. Neutral defaults and heuristic labels are not interchangeable with manually reviewed ground truth. Original scripts contain machine-specific paths; update input/output paths before running them. Review text is third-party material; no blanket licence is asserted.

The complete `aspect_labeling_sentiment.py` was recovered from the mixed CS552 VSCode folder: its input/output filenames and aspect vocabulary are for game-review labeling. This file is preserved as original code; its location does not make it a CS552 bibliometric script.
