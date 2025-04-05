# app/main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import engine, SessionLocal, Base
from typing import List

print("💡 ESTA ES LA VERSIÓN CORRECTA DEL MAIN.PY")


Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"mensaje": "Bienvenido a la versión correcta de de la aplicacion"}

@app.post("/usuarios/", response_model=schemas.UserOut)
def crear_usuario(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.crear_usuario(db, user)

@app.get("/usuarios/", response_model=list[schemas.UserOut])
def listar_usuarios(db: Session = Depends(get_db)):
    return crud.obtener_usuarios(db)

@app.post("/citas/", response_model=schemas.AppointmentOut)
def crear_cita(cita: schemas.AppointmentCreate, db: Session = Depends(get_db)):
    return crud.crear_cita(db, cita)

@app.get("/citas/", response_model=list[schemas.AppointmentOut])
def listar_citas(db: Session = Depends(get_db)):
    return crud.obtener_citas(db)

@app.get("/prueba")
def ruta_de_prueba():
    return {"mensaje": "Esto es una prueba nueva"}
