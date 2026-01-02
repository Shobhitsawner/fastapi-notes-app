from fastapi import FastAPI, Request, Depends, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from database import Base, engine, get_db
from models import Note

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request, db: Session = Depends(get_db)):
    notes = db.query(Note).all()
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "notes": notes}
    )


@app.post("/add")
def add_note(
    title: str = Form(...),
    content: str = Form(...),
    db: Session = Depends(get_db)
):
    note = Note(title=title, content=content)
    db.add(note)
    db.commit()
    return RedirectResponse("/", status_code=303)


@app.get("/edit/{note_id}", response_class=HTMLResponse)
def edit_note(note_id: int, request: Request, db: Session = Depends(get_db)):
    note = db.query(Note).filter(Note.id == note_id).first()
    return templates.TemplateResponse(
        "edit.html",
        {"request": request, "note": note}
    )


@app.post("/update/{note_id}")
def update_note(
    note_id: int,
    title: str = Form(...),
    content: str = Form(...),
    db: Session = Depends(get_db)
):
    note = db.query(Note).filter(Note.id == note_id).first()
    if note:
        note.title = title
        note.content = content
        db.commit()
    return RedirectResponse("/", status_code=303)


@app.get("/delete/{note_id}")
def delete_note(note_id: int, db: Session = Depends(get_db)):
    note = db.query(Note).filter(Note.id == note_id).first()
    if note:
        db.delete(note)
        db.commit()
    return RedirectResponse("/", status_code=303)
