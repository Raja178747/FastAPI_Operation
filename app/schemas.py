from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class ItemBase(BaseModel):
    email: EmailStr
    item_name: str
    quantity: int
    expiry_date: datetime

class ItemCreate(ItemBase):
    pass

class ItemResponse(ItemBase):
    id: str
    insert_date: datetime

    class Config:
        orm_mode = True

class ClockInBase(BaseModel):
    email: EmailStr
    location: str

class ClockInCreate(ClockInBase):
    pass

class ClockInResponse(ClockInBase):
    id: str
    insert_date: datetime

    class Config:
        orm_mode = True
