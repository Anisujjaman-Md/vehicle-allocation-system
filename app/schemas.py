from pydantic import BaseModel
from datetime import date

class AllocationCreate(BaseModel):
    employee_id: int
    vehicle_id: int
    date: date

class AllocationResponse(BaseModel):
    employee_id: int
    vehicle_id: int
    driver_id: int
    date: date
