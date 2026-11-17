# AI Tender Analysis & Bid Comparison - Week 2

Week 2 extends the Week 1 tender requirement register into a technical bid compliance workspace.

## Features
- 30 requirements x 3 bidders = 90 labeled compliance decisions
- five statuses: met, partially met, not met, not evidenced, not applicable
- tender reference, bidder evidence, rationale, unresolved question, and searched-document tracking
- qualifications, exclusions, delivery deviations, warranty gaps, alternative proposals, and contradiction detection
- mandatory-gap visibility and optional improvement tracking
- CSV, JSON, and XLSX compliance matrix exports with filters
- deviation register and clarification-question export
- exact-status evaluation, per-status metrics, and confusion matrix

## Run
```bash
python -m pip install -r requirements_week2.txt
python demo_week2.py
python -m pytest tests/test_week2_compliance.py
```

Keep the Week 4 reserved package unchanged.
