import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from passlib.context import CryptContext
from bson import ObjectId

MONGODB_URL = "mongodb://localhost:27017"
DATABASE_NAME = "quanlysv"

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

async def seed_data():
    client = AsyncIOMotorClient(MONGODB_URL)
    db = client[DATABASE_NAME]

    # Xóa dữ liệu cũ
    await db.users.delete_many({})
    await db.schedules.delete_many({})

    # Tạo user mẫu
    hashed_password = pwd_context.hash("123456")
    user = {
        "username": "sinhvien1",
        "email": "sv1@example.com",
        "full_name": "Nguyễn Văn A",
        "hashed_password": hashed_password,
        "role": "student"
    }
    result = await db.users.insert_one(user)
    student_id = result.inserted_id

    # Tạo lịch học mẫu
    schedule = {
        "student_id": student_id,
        "semester": "Học kỳ 2 - 2024",
        "subjects": [
            {"name": "Toán Cao Cấp", "code": "MATH101", "time": "08:00 - 10:00", "location": "P.101", "day_of_week": 2},
            {"name": "Lập trình Python", "code": "IT102", "time": "13:30 - 15:30", "location": "Lab 2", "day_of_week": 3},
            {"name": "Mạng máy tính", "code": "IT103", "time": "08:00 - 10:00", "location": "P.202", "day_of_week": 5},
        ]
    }
    await db.schedules.insert_one(schedule)

    print("Đã tạo dữ liệu mẫu thành công!")
    print("Tài khoản: sinhvien1 / Mật khẩu: 123456")
    client.close()

if __name__ == "__main__":
    asyncio.run(seed_data())
