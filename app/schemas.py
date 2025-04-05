# app/schemas.py
from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserCreate(BaseModel):
    nombre: str
    email: EmailStr

class UserOut(BaseModel):
    id: int
    nombre: str
    email: EmailStr

    class Config:
        from_attributes = True  # ✅ CORREGIDO para Pydantic v2

class AppointmentCreate(BaseModel):
    fecha: datetime
    descripcion: str
    user_id: int

class AppointmentOut(BaseModel):
    id: int
    fecha: datetime
    descripcion: str
    user_id: int

    class Config:
        from_attributes = True  # ✅ CORREGIDO para Pydantic v2
