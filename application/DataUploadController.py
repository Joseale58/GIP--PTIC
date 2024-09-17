from fastapi import UploadFile, APIRouter
from pydantic import BaseModel
from infrastructure.models.UserModel import User
from domain.DataUploadService import DataUploadService

DataUploadController = APIRouter(prefix="/data-upload")

@DataUploadController.post("/")
def data_upload(file: UploadFile):
    print(file.filename)
    # Acá irá la lógica para convertir el archivo a un arreglo de objetos de tipo BaseFileEntity
    # Ese arreglo se lo debo enviar a la función clean data en vez del arreglo vacío

    return DataUploadService.clean_data([])


#Controlador de e.g. insertar usuario
@DataUploadController.post("/create-user")
def insert_user(user: User):
    return DataUploadService.insert_user(user)

#Controlador de e.g. traer todos los usuarios
@DataUploadController.get("/")
def get_data():
    return DataUploadService.get_data()
