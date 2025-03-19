from pydantic import BaseModel
from typing import Optional

class Item(BaseModel):
    id: Optional[int]  # El campo ID es opcional, ya que es generado por la base de datos
    nombre: str
    planeta_origen: str
    legion: str
    bando: str
    historia: str
    emblema: str

    class Config:
        # Esto permite que los campos que se pasan desde MongoDB, como ObjectId, sean convertidos correctamente.
        orm_mode = True
