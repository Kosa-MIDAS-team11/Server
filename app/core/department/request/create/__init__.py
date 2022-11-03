from pydantic import BaseModel


class CreateDepartmentRequest(BaseModel):
    name: str
    location: str
