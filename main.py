from fastapi import FastAPI, HTTPException
from app.calculations import add, subtract, multiply, divide

app = FastAPI()

@app.get("/add")
def perform_addition(a: float, b:float):
    return {"result": add(a,b)}

@app.get("/subtract")
def perform_subtraction(a: float, b:float):
    return {"result": subtract(a,b)}

@app.get("/multiply")
def perform_multiplication(a: float, b:float):
    return {"result": multiply(a,b)}

@app.get("/divide")
def perform_division(a: float, b:float):
    try:
        return {"result": divide(a,b)}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

