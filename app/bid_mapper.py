from __future__ import annotations
import re
from difflib import SequenceMatcher

SYNONYMS = {
    "warranty": ["guarantee", "defects liability"],
    "delivery": ["lead time", "completion period", "schedule"],
    "certificate": ["certification", "compliance certificate"],
    "training": ["operator training", "user training"],
    "support": ["technical support", "service support"],
}

def _norm(text: str) -> str:
    text = text.lower()
    for root, variants in SYNONYMS.items():
        for v in variants:
            text = text.replace(v, root)
    return re.sub(r"[^a-z0-9]+", " ", text).strip()

def semantic_match_score(requirement_text: str, evidence_text: str) -> float:
    a, b = _norm(requirement_text), _norm(evidence_text)
    if not a or not b:
        return 0.0
    seq = SequenceMatcher(None, a, b).ratio()
    at, bt = set(a.split()), set(b.split())
    jac = len(at & bt) / max(1, len(at | bt))
    return round((seq * 0.45) + (jac * 0.55), 4)

def maps_to_requirement(requirement_text: str, evidence_text: str, threshold: float = 0.28) -> bool:
    return semantic_match_score(requirement_text, evidence_text) >= threshold
