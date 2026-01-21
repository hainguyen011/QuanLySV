from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List
from bson import ObjectId

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __get_pydantic_json_schema__(cls, field_schema):
        field_schema.update(type="string")

class User(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    username: str
    email: EmailStr
    full_name: str
    hashed_password: str
    role: str = "student" # student, admin

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

class Subject(BaseModel):
    name: str
    code: str
    time: str # e.g. "08:00 - 10:00"
    location: str
    day_of_week: int # 1 (Mon) to 7 (Sun)

class Schedule(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    student_id: PyObjectId
    semester: str
    subjects: List[Subject]

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
