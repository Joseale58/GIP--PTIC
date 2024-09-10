from pydantic import BaseModel


# Esta es una clase de ejemplo de como sería el modelo del excel/csv inicial, no es que vayan estos campos
class BaseFileEntity(BaseModel):
    id: int
    useless_field_1: str
    age: int
    career: str
    diagnostic: str
