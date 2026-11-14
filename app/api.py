from fastapi import FastAPI, HTTPException
from .ingestion import ingest_package
app=FastAPI(title='Tender Analysis Week 1')
@app.get('/health')
def health(): return {'status':'ok'}
@app.post('/ingest')
def ingest(path:str):
    try: return {'requirements':ingest_package(path)}
    except Exception as e: raise HTTPException(status_code=400,detail=str(e))
