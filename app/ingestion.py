from pathlib import Path
import json
from .register_service import build_register
SUPPORTED={".pdf",".xlsx"}
def ingest_package(folder:str):
    p=Path(folder)
    if not p.exists(): raise FileNotFoundError(folder)
    files=[x for x in p.iterdir() if x.is_file()]
    bad=[x.name for x in files if x.suffix.lower() not in SUPPORTED and x.name!="reference.json"]
    if bad: raise ValueError(f"Unsupported file(s): {', '.join(bad)}")
    return build_register(p)
