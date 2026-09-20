from fastapi import FastAPI

app = FastAPI()

notes = []

@app.get("/")
def home():
    return {"message": "Welcome Aditya!"}

@app.get("/notes")
def get_notes():
    return notes

@app.post("/notes")
def create_note(note: dict):
    notes.append(note)
    return {"message": "Note added successfully"}

