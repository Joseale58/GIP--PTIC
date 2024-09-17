from typing import List
from infrastructure.models.UserModel import User



from infrastructure.models.ConsultationModel import Consultation

from dotenv import load_dotenv
load_dotenv()


import os 
from supabase import create_client, Client

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)


class DataUploadRepository:
    @staticmethod
    def insert(consultations: List[Consultation]):
        print("Acá irá el código que insertará los datos en la bd")
        return {
            "status": 200,
            "message": "Datos insertados en la Base de Datos exitosamente"
        }
    
    #Método de e.g. insertar usuario capa Infraestructura
    @staticmethod
    def insert_user(user: User):
        data = supabase.table("User").insert({"name":user.name,"lastname":user.lastname, "dob":user.dob, "email":user.email}).execute()
        return {
            "status": 200,
            "message": "Datos insertados en la Base de Datos exitosamente Fuck yeah!"
        }
    
    #Método de e.g. traer todos los usuario capa Infraestructura
    @staticmethod
    def get():
        users = supabase.table("User").select("*").execute()
        return {
            "status": 200,
            "message": users
        }
