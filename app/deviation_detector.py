from __future__ import annotations
from typing import Iterable

DEVIATION_TYPES = {"qualification", "exclusion", "delivery deviation", "warranty gap", "alternative proposal", "contradiction"}

def deviation_rows(findings: Iterable):
    rows = []
    for f in findings:
        dtype = f.deviation_type
        if f.contradiction and not dtype:
            dtype = "contradiction"
        if dtype or f.status in {"partially met", "not met"}:
            rows.append({
                "bidder_id": f.bidder_id,
                "requirement_id": f.requirement_id,
                "mandatory": f.mandatory,
                "status": f.status,
                "deviation_type": dtype or "technical deviation",
                "rationale": f.rationale,
                "bid_source": f.bid_source,
            })
    return rows
