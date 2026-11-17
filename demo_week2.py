from pathlib import Path
import csv, json
from app.compliance_engine import classify_pair
from app.deviation_detector import deviation_rows
from app.clarification_service import clarification_rows
from app.week2_evaluation import evaluate
from app.compliance_matrix import export_csv, export_json, export_xlsx

ROOT = Path(__file__).parent
rows = json.loads((ROOT/'benchmarks/week2_90_pairs.json').read_text())
findings = [classify_pair(r) for r in rows]
metrics = evaluate(rows, findings)
export_csv(findings, ROOT/'exports/week2_compliance_matrix.csv')
export_json(findings, ROOT/'exports/week2_compliance_matrix.json')
export_xlsx(findings, ROOT/'exports/week2_compliance_matrix.xlsx')

with (ROOT/'exports/week2_deviation_register.csv').open('w', newline='', encoding='utf-8') as f:
    ds=deviation_rows(findings); w=csv.DictWriter(f, fieldnames=list(ds[0].keys())); w.writeheader(); w.writerows(ds)
with (ROOT/'exports/week2_clarification_questions.csv').open('w', newline='', encoding='utf-8') as f:
    qs=clarification_rows(findings); w=csv.DictWriter(f, fieldnames=list(qs[0].keys())); w.writeheader(); w.writerows(qs)
(ROOT/'results/week2_evaluation_results.json').write_text(json.dumps(metrics, indent=2))

mandatory_met_without_evidence=sum(1 for f in findings if f.mandatory and f.status=='met' and not f.bid_evidence)
seeded_exclusions=sum(1 for r in rows if r.get('exclusion'))
detected_exclusions=sum(1 for f in findings if f.deviation_type=='exclusion' and f.status=='not met')
seeded_contradictions=sum(1 for r in rows if r.get('contradiction'))
detected_contradictions=sum(1 for f in findings if f.contradiction and f.status=='partially met')
print('Week 2 - Technical Bid Compliance and Scope Alignment Demo')
print('='*58)
print(f"Requirement-bid pairs: {len(findings)}")
print(f"Exact status agreement: {metrics['exact_status_agreement']*100:.1f}%")
print(f"Mandatory met without evidence: {mandatory_met_without_evidence}")
print(f"Seeded exclusions surfaced: {detected_exclusions}/{seeded_exclusions}")
print(f"Seeded contradictions surfaced: {detected_contradictions}/{seeded_contradictions}")
print(f"Deviation findings: {len(deviation_rows(findings))}")
print(f"Clarification questions: {len(clarification_rows(findings))}")
print('Compliance matrix exports: working')
print('Per-status metrics + confusion matrix: working')
