from __future__ import annotations
import csv
import json
from pathlib import Path
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter

HEADERS = ["requirement_id","bidder_id","category","mandatory","status","tender_reference","tender_source","bid_evidence","bid_source","rationale","unresolved_question","searched_documents","deviation_type","scope_justification","contradiction"]

def export_csv(findings, path):
    path = Path(path); path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=HEADERS)
        w.writeheader()
        for x in findings:
            d = x.to_dict(); d["searched_documents"] = " | ".join(d["searched_documents"])
            w.writerow({h:d.get(h) for h in HEADERS})

def export_json(findings, path):
    path = Path(path); path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps([x.to_dict() for x in findings], indent=2), encoding="utf-8")

def export_xlsx(findings, path):
    path = Path(path); path.parent.mkdir(parents=True, exist_ok=True)
    wb = Workbook(); ws = wb.active; ws.title = "Compliance Matrix"
    ws.append(HEADERS)
    header_fill = PatternFill("solid", fgColor="1F4E78")
    for c in ws[1]:
        c.font = Font(color="FFFFFF", bold=True); c.fill = header_fill; c.alignment = Alignment(horizontal="center")
    fills = {
        "met":"C6EFCE", "partially met":"FFEB9C", "not met":"FFC7CE",
        "not evidenced":"F4B183", "not applicable":"D9EAD3"
    }
    for f in findings:
        d=f.to_dict(); d["searched_documents"]=" | ".join(d["searched_documents"])
        ws.append([d.get(h) for h in HEADERS])
        ws.cell(ws.max_row, 5).fill = PatternFill("solid", fgColor=fills.get(f.status,"FFFFFF"))
    ws.freeze_panes = "A2"; ws.auto_filter.ref = ws.dimensions
    widths = {1:16,2:12,3:18,4:11,5:18,6:22,7:30,8:48,9:32,10:48,11:48,12:44,13:22,14:32,15:13}
    for i,w in widths.items(): ws.column_dimensions[get_column_letter(i)].width=w
    for row in ws.iter_rows(min_row=2):
        for c in row: c.alignment=Alignment(vertical="top", wrap_text=True)
    wb.save(path)
