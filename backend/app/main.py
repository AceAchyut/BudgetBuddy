from fastapi import FastAPI

from app import models
from app.database import Base, engine
from app.routers.auth import router as auth_router
from fastapi.middleware.cors import CORSMiddleware
Base.metadata.create_all(bind=engine)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app = FastAPI(
    title="BudgetBuddy API",
    description="Personal budget planning and expense management",
    version="1.0.0",
)

app.include_router(auth_router)


@app.get("/")
def home():
    return {"message": "Welcome to BudgetBuddy API"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.get("/db-health")
def database_health():
    return {
        "status": "connected",
        "tables": list(Base.metadata.tables.keys()),
    }
