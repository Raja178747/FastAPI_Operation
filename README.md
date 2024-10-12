# FastAPI_Operation
# This project involves developing a FastAPI application that provides CRUD operations for managing Items and User Clock-In Records, utilizing MongoDB for data storage. The application allows users to create, retrieve, filter, update, and delete items and clock-in records, with automated timestamp handling and MongoDB aggregation features for enhanced data insights.

## Technologies Used
- Python
- FastAPI
- MongoDB
- Pydantic

fastapi_crud/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── schemas.py
│   ├── database.py
│   ├── .env
│   └── routes/
│       ├── __init__.py
│       ├── items.py
│       └── clock_in.py
├── requirements.txt
└── README.md


### Install Requirement.txt file:
pip install -r requirements.txt

### Create a .env file in the root directory with the following content:
MONGO_DETAILS=<your_mongodb_connection_string>

### Connection MongoDB Atlas:
create account on MongoDB 
replace username and password .env file



### Run the application:
uvicorn app.main:app --reload

# POST /api/v1/items: Create a new item.

# json
{
    "email": "bab@example.com",
    "item_name": "21Sample Item",
    "quantity": 21,
    "expiry_date": "2054-12-31T00:00:00"
}



# GET /api/v1/items/{id}: Retrieve an item by ID.

 http://127.0.0.1:8000/api/v1/items/67091dd9ec9dded8d1253aab



# GET /api/v1/items/filter: Filter items based on parameters.
# data  bases on email
# Params
email bab@example.com
expiry_date  2024-10-11T12:00:00
insert_date  2024-09-01T12:00:00
quantity  5


### DELETE /api/v1/items/{id}: Delete an item by ID.
http://127.0.0.1:8000/api/v1/items/67091dd9ec9dded8d1253aab



### PUT /api/v1/items/{id}: Update an item by ID.
http://127.0.0.1:8000/api/v1/items/6708fc44994acc7af3daf32d

## Params
accept  application/json
Content-Type application/json
## json

{
  "email": "bab@example.com",
  "item_name": "21Sample Item",
  "quantity": 90909,
  "expiry_date": "2054-12-31T00:00:00"
}


# Clock-In Records API
# POST /api/v1/clock-in: Create a new clock-in entry.
http://127.0.0.1:8000/api/v1/clock-in
# json
{
    "email": "baba@example.com",
    "location":"India"

}
