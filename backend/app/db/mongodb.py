from motor.motor_asyncio import AsyncIOMotorClient
from ..core.config import settings

class Database:
    client: AsyncIOMotorClient = None
    db = None

db = Database()

async def connect_to_mongo():
    db.client = AsyncIOMotorClient(settings.MONGODB_URL)
    db.db = db.client[settings.DATABASE_NAME]
    print(f"Đã kết nối tới MongoDB: {settings.DATABASE_NAME}")

async def close_mongo_connection():
    db.client.close()
    print("Đã đóng kết nối MongoDB")
