from pydantic import BaseModel, EmailStr

# Modelo de Pydantic para la tabla en la base de datos
class User(BaseModel):
    name: str  # Campo obligatorio, texto
    lastname: str  # Campo obligatorio, texto
    dob: str  # Campo obligatorio, tipo fecha
    email: EmailStr  # Validamos el email usando EmailStr para asegurar que es un formato correcto


