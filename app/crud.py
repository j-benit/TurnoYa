# app/crud.py
from sqlalchemy.orm import Session
from . import models, schemas

def crear_usuario(db: Session, user: schemas.UserCreate):
    db_user = models.User(nombre=user.nombre, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def crear_cita(db: Session, cita: schemas.AppointmentCreate):
    db_cita = models.Appointment(
        fecha=cita.fecha,
        descripcion=cita.descripcion,
        user_id=cita.user_id
    )
    db.add(db_cita)
    db.commit()
    db.refresh(db_cita)
    return db_cita

def obtener_usuarios(db: Session):
    return db.query(models.User).all()

def obtener_citas(db: Session):
    return db.query(models.Appointment).join(models.User).all()

