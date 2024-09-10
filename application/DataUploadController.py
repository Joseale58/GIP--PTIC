from fastapi import UploadFile, APIRouter

DataUploadController = APIRouter(prefix="/data-upload")


@DataUploadController.post("/")
def data_upload(file: UploadFile):
    print(file.filename)
    return {'fileName': file.filename}
