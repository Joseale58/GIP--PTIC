# API Proyecto GIP

## Pasos para levantar el proyecto

1. Tener python instalado
2. Recomendablemente, usar un virtual env ([documentación oficial](https://fastapi.tiangolo.com/virtual-environments/))
    1. Ejecutar el comando `.venv\Scripts\Activate.ps1` en una terminal estando sobre la ruta del proyecto
    2. Validar que esté activo el entorno virtual `Get-Command python`
    3. Actualizar pip `python -m pip install --upgrade pip`
3. Instalar dependencias con `pip install -r requirements.txt`
4. Levantar el API con `uvicorn main:app --reload`