from typing import List
from infrastructure.models.UserModel import User
from infrastructure.models.ConsultationModel import Consultation
from pandas import DataFrame 
from dotenv import load_dotenv
load_dotenv()
from core import infrastructure_constants as constants


import os 
from supabase import create_client, Client

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)


class DataUploadRepository:
    @staticmethod
    def insert(data : DataFrame):
        try:
            # Convertir las columnas de tipo fecha a formato de texto (string) para ser JSON serializable
            for col in data.select_dtypes(include=['datetime64[ns]', 'datetime64[ns, UTC]']).columns:
                data[col] = data[col].dt.strftime('%Y-%m-%d')  # Convertir a formato 'YYYY-MM-DD'
            
            # Insertar cada fila en la tabla de Supabase
            for index, row in data.iterrows():
                row_dic = row.to_dict()  # Convertir la fila a diccionario
                res = supabase.table(constants.TABLA_CONSULTA).insert(row_dic).execute()

            # Si todo sale bien, retornar un mensaje de éxito
            return {
                "status": 200,
                "message": "Datos insertados en la Base de Datos exitosamente"
            }

        except Exception as e:
            # Si ocurre un error, capturar la excepción y devolver un mensaje de error
            return {
                "status": 500,
                "message": f"Error durante la inserción de datos: {str(e)}"
            }
    
    
    #Método de e.g. insertar usuario capa Infraestructura
    @staticmethod
    def insert_user(user: User):
        data = supabase.table("User").insert({"name":user.name,"lastname":user.lastname, "dob":user.dob, "email":user.email}).execute()
        return {
            "status": 200,
            "message": "Datos insertados en la Base de Datos exitosamente: " + str(data)
        }
    
    #Método de e.g. traer todos los usuario capa Infraestructura
    @staticmethod
    def get():
        users = supabase.table("User").select("*").execute()
        return {
            "status": 200,
            "message": users
        }
