from fastapi import FastAPI, HTTPException, Depends
from app.schemas import AllocationCreate, AllocationResponse
from app.services import allocate_vehicle, fetch_allocation_history
from app.db import setup_db
from datetime import date

app = FastAPI(title="Vehicle Allocation System")

@app.on_event("startup")
async def on_startup():
    await setup_db()

@app.post("/allocate", response_model=AllocationResponse)
async def create_allocation(allocation: AllocationCreate):
    success = await allocate_vehicle(allocation.employee_id, allocation.vehicle_id, allocation.date)
    if not success:
        raise HTTPException(status_code=400, detail="Vehicle already allocated on this date")
    return {"employee_id": allocation.employee_id, "vehicle_id": allocation.vehicle_id, "driver_id": allocation.vehicle_id, "date": allocation.date}

@app.get("/allocations")
async def get_allocations(employee_id: int = None, vehicle_id: int = None, date_from: date = None, date_to: date = None):
    filters = {}
    if employee_id:
        filters['employee_id'] = employee_id
    if vehicle_id:
        filters['vehicle_id'] = vehicle_id
    if date_from and date_to:
        filters['date'] = {"$gte": date_from, "$lte": date_to}

    return await fetch_allocation_history(filters)
