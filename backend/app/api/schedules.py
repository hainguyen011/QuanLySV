from fastapi import APIRouter, Depends, HTTPException
from ..services import schedule_service
from ..core.security import verify_password # Sẽ cần dependency check token sau
from typing import List

router = APIRouter()

# Tạm thời chưa có middleware auth để test cho nhanh
@router.get("/{student_id}")
async def get_schedule(student_id: str):
    schedule = await schedule_service.get_student_schedule(student_id)
    if not schedule:
        raise HTTPException(status_code=404, detail="Không tìm thấy lịch học")
    return schedule

@router.post("/{student_id}")
async def update_schedule(student_id: str, schedule_data: dict):
    result = await schedule_service.create_or_update_schedule(student_id, schedule_data)
    return {"message": "Cập nhật thành công", "status": result}
