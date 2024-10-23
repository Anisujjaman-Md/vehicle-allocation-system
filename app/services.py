from app.crud import create_allocation, update_allocation, delete_allocation, get_allocations
from app.models import VehicleAllocation

async def allocate_vehicle(employee_id: int, vehicle_id: int, date):
    driver_id = vehicle_id  # Assuming driver_id is the same as vehicle_id for simplicity
    allocation = VehicleAllocation(employee_id=employee_id, vehicle_id=vehicle_id, driver_id=driver_id, date=date)
    success = await create_allocation(allocation)
    return success

async def fetch_allocation_history(filters):
    return await get_allocations(filters)
