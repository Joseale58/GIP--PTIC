from pydantic import BaseModel


class Consultation(BaseModel):
    age: int
    career: str
    diagnostic: str
