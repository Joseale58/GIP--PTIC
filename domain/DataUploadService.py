from pandas import DataFrame

from infrastructure.DataUploadRepository import DataUploadRepository


class DataUploadService:
    @staticmethod
    def clean_data(rips_df: DataFrame, monthly_df: DataFrame):
        print(rips_df.info())
        print(monthly_df.info())
        # Acá te mando los dos dataframes que se envían de los archivos de excel
        # Leete el readme de como probar esto desde un postman

        return DataUploadRepository.insert([])

    # Método de e.g. insertar usuario
    @staticmethod
    def insert_user(user):
        # Se deben todas las validaciones correspondientes
        return DataUploadRepository.insert_user(user)

    # Método de e.g. para traer todos los usuarios
    @staticmethod
    def get_data():
        return DataUploadRepository.get()
