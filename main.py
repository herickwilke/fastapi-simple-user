from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Routing


@app.get("/")
def root():
    return {"Ola": "Mundo"}

# Modeling


class User(BaseModel):
    id: int
    email: str
    password: str


# Creating a database
database = [
    User(id=1, email="herick@teste.com", password="abc@123"),
    User(id=2, email="test@teste.com", password="test")
]

# Route to get all


@app.get("/users")
def get_all_users():
    return database

# Route get by ID


@app.get("/users/{user_id}")
def get_user_by_id(user_id: int):
    for user in database:
        if(user.id == user_id):
            return user
    return {"status": 404, "message": "Cannot find a user with given ID"}

# Route insert user


@app.post("/user")
def insert_user(user: User):
    # create use cases here
    database.append(user)
    return(user)
