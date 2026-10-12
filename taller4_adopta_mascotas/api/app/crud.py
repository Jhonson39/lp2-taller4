from sqlalchemy.orm import Session, joinedload
from . import models


def listar_mascotas(db: Session, categoria_id: int | None = None):
    consulta = db.query(models.Mascota).options(joinedload(models.Mascota.categoria))
    if categoria_id is not None:
        consulta = consulta.filter(models.Mascota.categoria_id == categoria_id)
    return consulta.all()


def buscar_mascota(db: Session, mascota_id: int):
    return (
        db.query(models.Mascota)
        .options(joinedload(models.Mascota.categoria))
        .filter(models.Mascota.id == mascota_id)
        .first()
    )


def listar_categorias(db: Session):
    return db.query(models.Categoria).all()
