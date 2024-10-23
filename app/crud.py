from app.db import db
from app.models import VehicleAllocation
from pymongo.errors import DuplicateKeyError
from datetime import datetime

async def create_allocation(allocation: VehicleAllocation):
    try:
        await db['allocations'].insert_one(allocation.dict())
        return True
    except DuplicateKeyError:
        return False

async def update_allocation(allocation_id, update_data):
    result = await db['allocations'].update_one(
        {"_id": allocation_id, "date": {"$gte": datetime.now().date()}},
        {"$set": update_data}
    )
    return result.modified_count > 0

async def delete_allocation(allocation_id):
    result = await db['allocations'].delete_one(
        {"_id": allocation_id, "date": {"$gte": datetime.now().date()}}
    )
    return result.deleted_count > 0

async def get_allocations(filter_params):
    allocations = await db['allocations'].find(filter_params).to_list(length=None)
    return allocations
