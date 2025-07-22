from typing import List
from fastapi import FastAPI, Depends, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

import models
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
templates = Jinja2Templates(directory="templates")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root(request: Request, db: Session = Depends(get_db)):
    candidates = db.query(models.Candidate).all()
    return templates.TemplateResponse("index.html", {"request": request, "candidates": candidates})

@app.post("/vote")
def vote(candidate_ids: List[int] = Form(...), db: Session = Depends(get_db)):
    for candidate_id in candidate_ids:
        candidate = db.query(models.Candidate).filter(models.Candidate.id == candidate_id).first()
        if candidate:
            candidate.votes += 1
    db.commit()
    return RedirectResponse("/", status_code=303)

@app.get("/results")
def get_results(db: Session = Depends(get_db)):
    candidates = db.query(models.Candidate).all()
    return {c.name: c.votes for c in candidates}
