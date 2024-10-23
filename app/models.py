from pydantic import BaseModel
from datetime import date

class VehicleAllocation(BaseModel):
    employee_id: int
    vehicle_id: int
    driver_id: int
    date: date
