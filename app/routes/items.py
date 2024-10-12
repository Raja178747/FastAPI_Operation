
from fastapi import APIRouter, HTTPException,Query
from bson import ObjectId
from app.database import item_collection
from app.schemas import ItemCreate, ItemResponse
from datetime import datetime
from typing import List,Optional

router = APIRouter()

@router.post("/items", response_model=ItemResponse)
def create_item(item: ItemCreate):
    item_dict = item.dict()
    print(item_dict,'item_dict')
    item_dict['insert_date'] = datetime.utcnow()
    item_id = item_collection.insert_one(item_dict).inserted_id
    return {**item_dict, "id": str(item_id)}

@router.get("/items/{id}", response_model=ItemResponse)
def get_item(id: str):
    item = item_collection.find_one({"_id": ObjectId(id)})
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return {**item, "id": str(item["_id"])}

@router.get("/items/filter", response_model=List[ItemResponse])
def filter_items(email: str = None, expiry_date_str: str = None, insert_date_str: str = None, quantity: int = None):
    print("Filtering:", email, expiry_date_str, insert_date_str, quantity)

    query = {}
    if email:
        query["email"] = email

    if expiry_date_str:
        try:
            expiry_date = datetime.strptime(expiry_date_str, "%Y-%m-%d")  
            query["expiry_date"] = {"$gt": expiry_date}
        except ValueError:
            print("Invalid expiry_date format") 

    if insert_date_str:
        try:
            insert_date = datetime.strptime(insert_date_str, "%Y-%m-%d")  
            query["insert_date"] = {"$gte": insert_date}
        except ValueError:
            print("Invalid insert_date format")

    if quantity:
        query["quantity"] = {"$gte": quantity}

    print("Query:", query)

    items = item_collection.find(query)

    return [{**item, "id": str(item["_id"])} for item in items]


@router.delete("/items/{id}")
def delete_item(id: str):
    result = item_collection.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"detail": "Item deleted"}



@router.put("/items/{id}", response_model=ItemResponse)
def update_item(id: str, item: ItemCreate):
    updated_item = item.dict()
    # print(updated_item, "=-==========updated_item=========", id, type(id))
    
    result = item_collection.update_one({"_id": ObjectId(id)}, {"$set": updated_item})
    
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Item not found")

    updated_item_data = item_collection.find_one({"_id": ObjectId(id)})
    
    if not updated_item_data:
        raise HTTPException(status_code=404, detail="Item not found after update")

    response_item = ItemResponse(
        id=str(updated_item_data["_id"]),
        email=updated_item_data["email"],
        item_name=updated_item_data["item_name"],
        quantity=updated_item_data["quantity"],
        expiry_date=updated_item_data["expiry_date"],
        insert_date=updated_item_data["insert_date"]  
    )

    return response_item
