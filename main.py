from fastapi import FastAPI

from application.DataUploadController import DataUploadController
from core.config import settings

app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)

app.include_router(DataUploadController)
