from pathlib import Path
import json, pytest
from app.ingestion import ingest_package
from app.evaluation import evaluate
from app.conflict_detector import detect_conflicts
ROOT=Path(__file__).resolve().parents[1]
def test_extract_30(): assert len(ingest_package(ROOT/'development_tender'))==30
def test_precision_recall():
 r=ingest_package(ROOT/'development_tender'); ref=json.loads((ROOT/'annotations/development_reference.json').read_text()); m=evaluate(r,ref); assert m['precision']>=.9 and m['recall']>=.9
def test_sources(): assert all(x['source']['quote'] for x in ingest_package(ROOT/'development_tender'))
def test_conflicts(): assert len(detect_conflicts(ingest_package(ROOT/'development_tender')))>=2
def test_unknowns(): assert any(x['quantity'] is None for x in ingest_package(ROOT/'development_tender'))
def test_idempotent(): assert len(ingest_package(ROOT/'development_tender'))==len(ingest_package(ROOT/'development_tender'))
def test_reserved_frozen(): assert (ROOT/'reserved_week4/frozen_reference.json').exists()
