# main.py
from fastapi import FastAPI, HTTPException
from bson import ObjectId
from conexiondb import get_collection  # Importar la conexión
from model import Item  # Importar el modelo de datos

app = FastAPI()

# Obtener la colección de la base de datos
collection = get_collection()

# Crear un nuevo item
@app.post("/items/", response_model=dict)
def create_item(item: Item):
    item_dict = item.dict()
    result = collection.insert_one(item_dict)
    return {"id": str(result.inserted_id), "mensaje": "Item creado exitosamente"}

# Obtener todos los items
@app.get("/items/")
def get_items():
    items = list(collection.find())
    for item in items:
        item["id"] = str(item["_id"])
        del item["_id"]
    return items

# Obtener un item por ID
@app.get("/items/{item_id}")
def get_item(item_id: str):
    item = collection.find_one({"_id": ObjectId(item_id)})
    if not item:
        raise HTTPException(status_code=404, detail="Item no encontrado")
    item["id"] = str(item["_id"])
    del item["_id"]
    return item

# Actualizar un item por ID
@app.put("/items/{item_id}")
def update_item(item_id: str, item: Item):
    result = collection.update_one({"_id": ObjectId(item_id)}, {"$set": item.dict()})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Item no encontrado")
    return {"mensaje": "Item actualizado exitosamente"}

# Eliminar un item por ID
@app.delete("/items/{item_id}")
def delete_item(item_id: str):
    result = collection.delete_one({"_id": ObjectId(item_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Item no encontrado")
    return {"mensaje": "Item eliminado exitosamente"}
