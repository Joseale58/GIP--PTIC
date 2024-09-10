from typing import List

from infrastructure.models.ConsultationModel import Consultation


class DataUploadRepository:
    @staticmethod
    def insert(consultations: List[Consultation]):
        print("Acá irá el código que insertará los datos en la bd")
        return {
            "status": 200,
            "message": "Datos insertados en la Base de Datos exitosamente"
        }
