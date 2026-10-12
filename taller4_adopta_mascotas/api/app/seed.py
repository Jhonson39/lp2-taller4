from .database import Base, engine, SessionLocal
from . import models

Base.metadata.create_all(bind=engine)
db = SessionLocal()

try:
    if db.query(models.Categoria).count() == 0:
        perros = models.Categoria(nombre="Perros")
        gatos = models.Categoria(nombre="Gatos")
        otros = models.Categoria(nombre="Otros")
        db.add_all([perros, gatos, otros])
        db.commit()
        db.refresh(perros)
        db.refresh(gatos)
        db.refresh(otros)

        db.add_all([
            models.Mascota(
                nombre="Luna",
                edad="2 años",
                descripcion="Es cariñosa y le gusta salir a caminar.",
                categoria_id=perros.id
            ),
            models.Mascota(
                nombre="Max",
                edad="1 año",
                descripcion="Es juguetón y aprende rápido.",
                categoria_id=perros.id
            ),
            models.Mascota(
                nombre="Michi",
                edad="3 años",
                descripcion="Es tranquilo y disfruta dormir al sol.",
                categoria_id=gatos.id
            ),
            models.Mascota(
                nombre="Canela",
                edad="6 meses",
                descripcion="Es curiosa y necesita un hogar paciente.",
                categoria_id=gatos.id
            ),
            models.Mascota(
                nombre="Toby",
                edad="4 años",
                descripcion="Es un conejo tranquilo y fácil de cuidar.",
                categoria_id=otros.id
            ),
        ])
        db.commit()
        print("Datos de ejemplo agregados.")
    else:
        print("Ya existen datos; no se agregaron duplicados.")
finally:
    db.close()
