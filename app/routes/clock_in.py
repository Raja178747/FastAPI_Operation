from fastapi import APIRouter, HTTPException
from bson import ObjectId
from app.database import clock_in_collection
from app.schemas import ClockInCreate, ClockInResponse
from datetime import datetime
from typing import List


router = APIRouter()

@router.post("/clock-in", response_model=ClockInResponse)
def create_clock_in(clock_in: ClockInCreate):
    clock_in_dict = clock_in.dict()
    clock_in_dict['insert_date'] = datetime.utcnow()
    clock_in_id = clock_in_collection.insert_one(clock_in_dict).inserted_id
    return {**clock_in_dict, "id": str(clock_in_id)}

@router.get("/clock-in/{id}", response_model=ClockInResponse)
def get_clock_in(id: str):
    clock_in_record = clock_in_collection.find_one({"_id": ObjectId(id)})
    if clock_in_record is None:
        raise HTTPException(status_code=404, detail="Clock-in record not found")
    return {**clock_in_record, "id": str(clock_in_record["_id"])}

@router.get("/clock-in/filter", response_model=List[ClockInResponse])
def filter_clock_ins(email: str = None, location: str = None, insert_date: str = None):
    query = {}
    if email:
        query["email"] = email
    if location:
        query["location"] = location
    if insert_date:
        try:
            insert_date_format = datetime.strptime(insert_date, "%Y-%m-%d")
            query["insert_date"] = {"$gte": insert_date_format}
        except ValueError:
            raise HTTPException(status_code=400, detail="Invalid insert_date format")

    clock_in_records = clock_in_collection.find(query)
    return [{**record, "id": str(record["_id"])} for record in clock_in_records]


@router.delete("/clock-in/{id}")
def delete_clock_in(id: str):
    result = clock_in_collection.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Clock-in record not found")
    return {"detail": "Clock-in record deleted"}

@router.put("/clock-in/{id}", response_model=ClockInResponse)
def update_clock_in(id: str, clock_in: ClockInCreate):
    updated_record = clock_in.dict()
    result = clock_in_collection.update_one({"_id": ObjectId(id)}, {"$set": updated_record})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Clock-in record not found")
    
    updated_record["id"] = id
    return updated_record
