from ..db.mongodb import db
from ..models.user import Schedule, Subject
from bson import ObjectId

async def get_student_schedule(student_id: str):
    schedule = await db.db.schedules.find_one({"student_id": ObjectId(student_id)})
    if schedule:
        schedule["id"] = str(schedule["_id"])
        schedule["student_id"] = str(schedule["student_id"])
        return schedule
    return None

async def create_or_update_schedule(student_id: str, schedule_data: dict):
    schedule_data["student_id"] = ObjectId(student_id)
    result = await db.db.schedules.update_one(
        {"student_id": ObjectId(student_id)},
        {"$set": schedule_data},
        upsert=True
    )
    return str(result.upserted_id) if result.upserted_id else "Updated"
