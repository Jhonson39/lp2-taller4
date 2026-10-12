from pydantic import BaseModel, ConfigDict


class CategoriaSalida(BaseModel):
    id: int
    nombre: str
    model_config = ConfigDict(from_attributes=True)


class MascotaSalida(BaseModel):
    id: int
    nombre: str
    edad: str
    descripcion: str
    categoria_id: int
    categoria: CategoriaSalida
    model_config = ConfigDict(from_attributes=True)
