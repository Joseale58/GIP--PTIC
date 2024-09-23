from typing import List
from infrastructure.models.UserModel import User
from infrastructure.models.ConsultationModel import Consultation
from pandas import DataFrame 
from dotenv import load_dotenv
load_dotenv()


import os 
from supabase import create_client, Client

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)


class DataUploadRepository:
    @staticmethod
    def insert(data : DataFrame):
        for index, row in data.iterrows():
            row_dic = row.to_dict()  # Convertir la fila a diccionario

            print (row_dic)
            # Insertar la fila en la tabla de Supabase
            # res = supabase.table("nombre_tabla").insert(row).execute()

            # # Verificar la respuesta
            # if res.status_code == 201:
            #     print(f"Fila {index} insertada correctamente.")
            # else:
            #print(f"Error al insertar la fila {index}: {res}")
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
