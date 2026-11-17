from __future__ import annotations
from typing import Dict, Any
from .compliance_models import ComplianceFinding, VALID_STATUSES


def classify_pair(pair: Dict[str, Any]) -> ComplianceFinding:
    explicit = (pair.get("explicit_commitment") or "").strip().lower()
    evidence = pair.get("bid_evidence")
    exclusion = bool(pair.get("exclusion"))
    contradiction = bool(pair.get("contradiction"))
    partial = bool(pair.get("partial"))
    na = bool(pair.get("not_applicable"))
    scope_justification = pair.get("scope_justification")

    if na and scope_justification:
        status = "not applicable"
        rationale = "Recorded scope justification confirms the requirement does not apply to this bidder's offered scope."
    elif not evidence:
        status = "not evidenced"
        rationale = "No sufficient bidder evidence was found in the searched bid documents."
    elif exclusion or explicit in {"reject", "not comply", "excluded", "deviation"}:
        status = "not met"
        rationale = "Bidder evidence contains an explicit exclusion, rejection, or conflicting commitment."
    elif contradiction:
        status = "partially met"
        rationale = "Supporting and contradictory statements are both present, so full compliance is not established."
    elif partial or explicit in {"partial", "conditional"}:
        status = "partially met"
        rationale = "The bidder addresses the requirement but only partially or conditionally."
    else:
        status = "met"
        rationale = "The bidder provides explicit evidence satisfying the stated requirement."

    if status not in VALID_STATUSES:
        raise ValueError(status)

    if pair.get("mandatory") and status == "met" and not evidence:
        status = "not evidenced"
        rationale = "Mandatory requirements cannot be marked met without supporting bid evidence."

    question = pair.get("unresolved_question")
    if not question and status in {"partially met", "not met", "not evidenced"}:
        question = f"Please clarify compliance with {pair['requirement_id']} and provide supporting evidence."

    return ComplianceFinding(
        requirement_id=pair["requirement_id"],
        bidder_id=pair["bidder_id"],
        category=pair["category"],
        mandatory=bool(pair["mandatory"]),
        status=status,
        tender_reference=pair["tender_reference"],
        tender_source=pair["tender_source"],
        bid_evidence=evidence,
        bid_source=pair.get("bid_source"),
        rationale=rationale,
        unresolved_question=question,
        searched_documents=list(pair.get("searched_documents", [])),
        deviation_type=pair.get("deviation_type"),
        scope_justification=scope_justification,
        contradiction=contradiction,
    )
