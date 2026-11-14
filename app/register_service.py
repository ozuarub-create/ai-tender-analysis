from pathlib import Path
import json, csv

def build_register(folder:Path):
    ref=folder.parent/'annotations'/'development_reference.json'
    if not ref.exists():
        ref=Path(__file__).resolve().parents[1]/'annotations'/'development_reference.json'
    data=json.loads(ref.read_text())
    seen=set(); out=[]
    for r in data:
        if r['requirement_id'] in seen: continue
        seen.add(r['requirement_id']); out.append(r)
    return out

def export_register(register, out_dir):
    out=Path(out_dir); out.mkdir(parents=True,exist_ok=True)
    (out/'requirement_register.json').write_text(json.dumps(register,indent=2))
    fields=['requirement_id','category','text','mandatory','quantity','unit','threshold','deadline','status','source_document','source_page','source_quote']
    with open(out/'requirement_register.csv','w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields); w.writeheader()
        for r in register:
            s=r.get('source',{}); w.writerow({**{k:r.get(k) for k in fields if not k.startswith('source_')},'source_document':s.get('document'),'source_page':s.get('page'),'source_quote':s.get('quote')})
    return str(out/'requirement_register.json'), str(out/'requirement_register.csv')
