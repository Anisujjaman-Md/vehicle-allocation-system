from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import ASCENDING
from pymongo.errors import DuplicateKeyError

client = AsyncIOMotorClient("mongodb://mongo:27017")
db = client['vehicle_allocation']

async def setup_db():
    await db['allocations'].create_index([("vehicle_id", ASCENDING), ("date", ASCENDING)], unique=True)