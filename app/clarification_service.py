from __future__ import annotations

def clarification_rows(findings):
    return [
        {
            "bidder_id": f.bidder_id,
            "requirement_id": f.requirement_id,
            "status": f.status,
            "question": f.unresolved_question,
        }
        for f in findings
        if f.unresolved_question
    ]
