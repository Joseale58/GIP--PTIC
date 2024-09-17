from fastapi import UploadFile, APIRouter

from domain.DataUploadService import DataUploadService
from infrastructure.models.UserModel import User

DataUploadController = APIRouter(prefix="/data-upload")


@DataUploadController.post("/")
def data_upload(rips: UploadFile, monthly: UploadFile):
    print(rips.filename)
    print(monthly.filename)
    # Acá irá la lógica para convertir el archivo a un arreglo de objetos de tipo BaseFileEntity
    # Ese arreglo se lo debo enviar a la función clean data en vez del arreglo vacío

    return DataUploadService.clean_data([])


# Controlador de e.g. insertar usuario
@DataUploadController.post("/create-user")
def insert_user(user: User):
    return DataUploadService.insert_user(user)


# Controlador de e.g. traer todos los usuarios
@DataUploadController.get("/")
def get_data():
    return DataUploadService.get_data()
