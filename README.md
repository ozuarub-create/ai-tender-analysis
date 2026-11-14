# Week 1 - AI Tender Analysis and Bid Comparison

Standalone prototype that converts a synthetic tender package into a structured, traceable requirement register.

## Features
- 30 development requirements, 30 BOQ lines, 3 bids
- Reserved Week 4 package with 10 requirements, 10 BOQ lines, 2 bids
- Stable IDs and explicit unknown values
- Amendment/supersession and conflict tracking
- PDF/XLSX source references
- JSON/CSV export and HTML register viewer
- Precision/recall evaluation
- Idempotent imports and clear unsupported-file errors

## Run
```bash
python -m pip install -r requirements.txt
python demo_week1.py
pytest
```
