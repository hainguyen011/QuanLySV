from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .db.mongodb import connect_to_mongo, close_mongo_connection
from .api import auth, schedules

app = FastAPI(title="QuanLySV API", version="1.0.0")

app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
app.include_router(schedules.router, prefix="/api/schedules", tags=["schedules"])

@app.on_event("startup")
async def startup_db_client():
    await connect_to_mongo()

@app.on_event("shutdown")
async def shutdown_db_client():
    await close_mongo_connection()

# Cấu hình CORS cho mạng LAN
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Tạm thời để * để dễ phát triển trong LAN, sẽ siết chặt sau
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Chào mừng bạn đến với QuanLySV API"}
