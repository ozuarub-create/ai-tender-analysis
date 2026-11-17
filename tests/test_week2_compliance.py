from pathlib import Path
import json
from app.bid_mapper import semantic_match_score
from app.compliance_engine import classify_pair
from app.week2_evaluation import evaluate
from app.deviation_detector import deviation_rows
from app.clarification_service import clarification_rows

ROOT = Path(__file__).resolve().parents[1]
ROWS = json.loads((ROOT/'benchmarks/week2_90_pairs.json').read_text())
FINDINGS = [classify_pair(r) for r in ROWS]

def test_90_pairs():
    assert len(ROWS) == 90 and len(FINDINGS) == 90

def test_exact_status_agreement_acceptance():
    assert evaluate(ROWS, FINDINGS)['exact_status_agreement'] >= 0.85

def test_no_mandatory_met_without_evidence():
    assert not [f for f in FINDINGS if f.mandatory and f.status=='met' and not f.bid_evidence]

def test_seeded_exclusions_surfaced():
    seeded=[r for r in ROWS if r.get('exclusion')]
    got=[f for f in FINDINGS if f.deviation_type=='exclusion' and f.status=='not met']
    assert len(got) == len(seeded) and len(seeded) > 0

def test_seeded_contradictions_surfaced():
    seeded=[r for r in ROWS if r.get('contradiction')]
    got=[f for f in FINDINGS if f.contradiction and f.status=='partially met']
    assert len(got) == len(seeded) and len(seeded) > 0

def test_missing_responses_not_evidenced():
    assert all(f.status=='not evidenced' for f in FINDINGS if not f.bid_evidence and not f.scope_justification)

def test_clarifications_link_bidder_requirement():
    rows=clarification_rows(FINDINGS)
    assert rows and all(r['bidder_id'] and r['requirement_id'] for r in rows)

def test_paraphrase_mapping():
    assert semantic_match_score('minimum 24 month warranty', '24 month guarantee against defects') > 0.2

def test_deviation_register_not_empty():
    assert len(deviation_rows(FINDINGS)) >= 10
