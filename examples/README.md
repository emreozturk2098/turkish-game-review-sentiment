# Selected original code
`keyword_matching_excerpt.py` preserves the Turkish-character normalization, source suffix list and keyword regex definitions from `PROJE KODLARI.docx`. Personal file paths and workbook writing are omitted. This is only a small original excerpt; it is not the BERT/TF-IDF training code.

The heuristic is not a Turkish morphological analyzer. The source pattern requires a listed suffix and normalizes Turkish characters; it can miss forms and produce false matches. Other source logic uses local sentiment windows and review filtering, and recovered full labeling/filtering scripts are now under source/. A complete original model-training pipeline is not available. No code here generates the archived model scores.
