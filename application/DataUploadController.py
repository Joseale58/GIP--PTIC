from fastapi import UploadFile, APIRouter

from domain.DataUploadService import DataUploadService

DataUploadController = APIRouter(prefix="/data-upload")


@DataUploadController.post("/")
def data_upload(file: UploadFile):
    print(file.filename)
    # Acá irá la lógica para convertir el archivo a un arreglo de objetos de tipo BaseFileEntity
    # Ese arreglo se lo debo enviar a la función clean data en vez del arreglo vacío

    return DataUploadService.clean_data([])
