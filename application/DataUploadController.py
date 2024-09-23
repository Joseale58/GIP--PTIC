from io import BytesIO

from fastapi import UploadFile, APIRouter, HTTPException
from pandas import read_excel

from domain.DataUploadService import DataUploadService
from infrastructure.models.UserModel import User

DataUploadController = APIRouter(prefix="/data-upload")


@DataUploadController.post("/")
async def data_upload(rips: UploadFile, monthly: UploadFile):
    try:
        rips_file = await rips.read()
        rips_df = read_excel(BytesIO(rips_file))
        monthly_file = await monthly.read()
        monthly_df = read_excel(BytesIO(monthly_file))
    except HTTPException as e:
        # Captura las excepciones HTTP lanzadas desde el servicio
        raise e
    except Exception as e:
        raise HTTPException(status_code=404, detail="Error procesando los archivos enviados")

    return DataUploadService.clean_data(rips_df, monthly_df)


# Controlador de e.g. insertar usuario
# Esto debería ir en otro controller
@DataUploadController.post("/create-user")
def insert_user(user: User):
    return DataUploadService.insert_user(user)


# Controlador de e.g. traer todos los usuarios
# Esto también
@DataUploadController.get("/")
def get_data():
    return DataUploadService.get_data()
