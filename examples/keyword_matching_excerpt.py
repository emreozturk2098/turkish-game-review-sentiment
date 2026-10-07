"""Selected original keyword-matching definitions from the supplied Word code.
No annotation pipeline, training or raw review data is distributed.
"""
import re

SUFFIXES = [
    "", "i", "ı", "u", "ü", "e", "a", "de", "da", "den", "dan", "ye", "ya",
    "nin", "nın", "nun", "nün", "ne", "na", "ler", "lar", "si", "sı",
    "su", "sü", "inden", "undan", "lerinin", "larının", "deki", "daki",
    "yle", "yla", "li", "lı", "lu", "lü", "ik", "ık", "ük", "ek", "ak"
]

def normalize_text(text):
    replacements = str.maketrans("çğıöşü", "cgiosu")
    return text.translate(replacements)

def get_keyword_pattern(keyword):
    """Verilen keyword için suffix'leri de içeren regex desenini oluşturur."""
    norm_kw = normalize_text(keyword.lower())
    pattern = r'\b' + re.escape(norm_kw) + '(' + '|'.join(SUFFIXES) + r')\b'
    return pattern

