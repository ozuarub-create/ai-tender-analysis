from __future__ import annotations
from collections import Counter, defaultdict

STATUSES = ["met", "partially met", "not met", "not evidenced", "not applicable"]

def evaluate(reference_rows, findings):
    pred = {(f.bidder_id, f.requirement_id): f.status for f in findings}
    total = len(reference_rows)
    correct = 0
    matrix = {r: {p: 0 for p in STATUSES} for r in STATUSES}
    per_status = defaultdict(lambda: {"correct": 0, "total": 0})
    for row in reference_rows:
        key = (row["bidder_id"], row["requirement_id"])
        ref = row["reference_status"]
        got = pred[key]
        matrix[ref][got] += 1
        per_status[ref]["total"] += 1
        if ref == got:
            correct += 1
            per_status[ref]["correct"] += 1
    agreement = correct / total if total else 0.0
    per_status_out = {}
    for s in STATUSES:
        x = per_status[s]
        per_status_out[s] = round(x["correct"] / x["total"], 4) if x["total"] else None
    return {
        "total_pairs": total,
        "correct_pairs": correct,
        "exact_status_agreement": round(agreement, 4),
        "per_status_accuracy": per_status_out,
        "confusion_matrix": matrix,
    }
