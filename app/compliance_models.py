from __future__ import annotations
from dataclasses import dataclass, asdict
from typing import List, Optional

VALID_STATUSES = {"met", "partially met", "not met", "not evidenced", "not applicable"}

@dataclass
class ComplianceFinding:
    requirement_id: str
    bidder_id: str
    category: str
    mandatory: bool
    status: str
    tender_reference: str
    tender_source: str
    bid_evidence: Optional[str]
    bid_source: Optional[str]
    rationale: str
    unresolved_question: Optional[str]
    searched_documents: List[str]
    deviation_type: Optional[str] = None
    scope_justification: Optional[str] = None
    contradiction: bool = False

    def to_dict(self):
        return asdict(self)
