from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import Base, engine, obtener_db
from . import crud, schemas

Base.metadata.create_all(bind=engine)
app = FastAPI(title="API Adopta una Mascota", version="1.0")


@app.get("/")
def inicio():
    return {"mensaje": "API de Adopta una Mascota funcionando"}


@app.get("/mascotas", response_model=list[schemas.MascotaSalida])
def obtener_mascotas(categoria_id: int | None = None, db: Session = Depends(obtener_db)):
    return crud.listar_mascotas(db, categoria_id)


@app.get("/mascotas/{mascota_id}", response_model=schemas.MascotaSalida)
def obtener_mascota(mascota_id: int, db: Session = Depends(obtener_db)):
    mascota = crud.buscar_mascota(db, mascota_id)
    if mascota is None:
        raise HTTPException(status_code=404, detail="Mascota no encontrada")
    return mascota


@app.get("/categorias", response_model=list[schemas.CategoriaSalida])
def obtener_categorias(db: Session = Depends(obtener_db)):
    return crud.listar_categorias(db)
