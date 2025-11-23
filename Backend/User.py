# Clase de Programacion 3, los Jueves de 20:00 PM a 22:00 PM

# Mi nombre es Yoskal Garcia Contreras
# Matricula: 2022-0497

# Este es un proyecto creado con FasatAPI, CRUD de usuarios con get, post, put y delete 

from fastapi import  FastAPI, HTTPException, status

from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    surname: str
    age: int
    educacion: str
    
databese_users = [User(id=1, name="Dayelin", surname="Ramirez", age= 26, educacion="Ingenieria Civil"),
                User(id=2, name="Juan", surname="Perez", age=29, educacion="Ingenieria en Sistemas"),
                User(id=3, name="Maria", surname="Lopez", age=37, educacion="Contabilidad")
                ]


# Get
# =================== # ruta principal con get que devuelve todos los usuarios # =================== #
@app.get("/")
async def get_users():
    return databese_users

# ======================= # path que se usa para buscar un usuario por su id # ===================== #
@app.get("/user_path/{user_id}")
async def get_user(user_id: int):
    for user in databese_users:
        if user.id == user_id:
            return {"Usuario encontrado con exito ✅": user}
    return {"Error ❌": "User not found"}

