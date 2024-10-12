from fastapi import FastAPI
from app.routes import items, clock_in

app = FastAPI()

app.include_router(items.router, prefix="/api/v1")
app.include_router(clock_in.router, prefix="/api/v2")

@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI CRUD application!"}
