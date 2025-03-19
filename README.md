# FastAPI con MongoDB

Este proyecto es una API REST desarrollada con **FastAPI** y **MongoDB** para gestionar información sobre primarcas del universo de Warhammer 40K.

## Requisitos

Antes de ejecutar la aplicación, asegúrate de tener instalados los siguientes requisitos:

- **Python 3.8+**
- **MongoDB** (en ejecución en `localhost:27017` o configurado en un servidor remoto)
- **Dependencias del proyecto** (instaladas con `pip`)

## Instalación

1. Clona este repositorio:

   ```sh
   git clone https://github.com/tu-usuario/tu-repositorio.git
   cd tu-repositorio
   ```

2. Crea un entorno virtual y actívalo:

   ```sh
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. Instala las dependencias:

   ```sh
   pip install -r requirements.txt
   ```

## Estructura del Proyecto

```
.
├── main.py          # Archivo principal de la API
├── database.py      # Configuración de la conexión a MongoDB
├── models.py        # Definición del modelo de datos con Pydantic
├── requirements.txt # Lista de dependencias
├── README.md        # Documentación del proyecto
```

## Configuración de la Base de Datos

El archivo `database.py` maneja la conexión a MongoDB:

```python
from pymongo import MongoClient

def get_collection():
    client = MongoClient("mongodb://localhost:27017")
    db = client["primarcas_db"]
    return db["primarcas"]
```

## Uso

### Iniciar la API

Ejecuta el siguiente comando para iniciar el servidor:

```sh
uvicorn main:app --reload
```

La API estará disponible en:

- **Documentación interactiva**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **Redoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

### Endpoints

| Método  | Ruta             | Descripción                        |
|---------|-----------------|------------------------------------|
| `POST`  | `/items/`       | Crea un nuevo item                |
| `GET`   | `/items/`       | Obtiene todos los items           |
| `GET`   | `/items/{id}`   | Obtiene un item por ID            |
| `PUT`   | `/items/{id}`   | Actualiza un item por ID          |
| `DELETE`| `/items/{id}`   | Elimina un item por ID            |

### Ejemplo de Petición POST

```json
{
  "nombre": "Sanguinius",
  "planeta_origen": "Baal",
  "legion": "Ángeles Sangrientos",
  "bando": "Leal",
  "historia": "Murió en combate contra Horus en la Herejía de Horus.",
  "emblema": "https://wh40k.lexicanum.com/mediawiki/images/9/9a/Bloodangelsymbol.png"
}
```

## Autores

- [Tu Nombre](https://github.com/jmsanzprieto)



