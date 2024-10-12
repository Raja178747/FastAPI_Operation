from fastapi import FastAPI
from app.routes import items, clock_in
import os
import uvicorn

app = FastAPI()

app.include_router(items.router, prefix="/api/v1")
app.include_router(clock_in.router, prefix="/api/v2")

@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI CRUD application!"}

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000)) 
    uvicorn.run(app, host="0.0.0.0", port=port)
