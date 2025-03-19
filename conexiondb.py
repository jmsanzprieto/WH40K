from pymongo import MongoClient

# Conexión a la base de datos MongoDB
client = MongoClient("mongodb://localhost:27017")
db = client["primarcas_db"]
collection = db["primarcas"]

def get_collection():
    return collection
