from pydantic import BaseModel


class EmployeeListRequest(BaseModel):
    department_id: int

