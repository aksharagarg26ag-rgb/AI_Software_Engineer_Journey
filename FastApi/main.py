# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()

# class User(BaseModel):
#     name: str
#     age: int

# @app.post("/greet")
# def greet(user: User):

#     return {
#         "message": f"Hello {user.name}, Age {user.age}"
#     }
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Numbers(BaseModel):
    num1: int
    num2: int

@app.post("/add")
def add(numbers: Numbers):

    result = numbers.num1 + numbers.num2

    return {
        "result": result
    }
