import logging
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from pathlib import Path
from app.operations import add,subtract, multiply, divide
from app.model.history import CalculationHistory
from database import SessionLocal, engine, Base
# Configure logging
logging.basicConfig(level=logging.INFO)
# Create tables in the database (ensure it happens at app startup)
Base.metadata.create_all(bind=engine)
# Create FastAPI instance
app = FastAPI()
# Health check endpoint
@app.get("/health")
async def health():
    return {"status": "OK"}
# Allow CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Serve static files
app.mount("/componets", StaticFiles(directory=Path(__file__).parent / "componets"), name="componets")
# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
# Pydantic schema for input
class CalculationRequest(BaseModel):
    operand1: float
    operand2: float
    operation: str
# Pydantic schema for returning history
class CalculationHistoryResponse(BaseModel):
    id: int
    operation: str
    operand1: float
    operand2: float
    result: float
# Serve the index page
@app.get("/", response_class=HTMLResponse)
async def index():
    homepage_path = Path(__file__).parent / "homepage" / "index.html"
    with open(homepage_path) as f:
        return HTMLResponse(content=f.read(), status_code=200)
# Perform and store the calculation
@app.post("/", response_model=dict)
async def calculate(request: CalculationRequest, db: Session = Depends(get_db)):
    operand1 = request.operand1
    operand2 = request.operand2
    operation = request.operation
    # Log received data
    logging.info(f"Received request: operand1={operand1}, operand2={operand2}, operation={operation}")
    # Operation mapping
    operations = {
        "Add": add(),
        "Subtract": subtract(),
        "Multiply": multiply(),
        "Divide": divide(),
    }
    if operation not in operations:
        raise HTTPException(status_code=400, detail="Invalid operation")
    if operation == "Divide" and operand2 == 0:
        raise HTTPException(status_code=400, detail="Cannot divide by zero")
    
    # Perform the calculation
    try:
        result = operations[operation].calculate(operand1, operand2)
    except Exception as e:
        logging.error(f"Error in calculation: {e}")
        raise HTTPException(status_code=500, detail="Calculation error")
    # Log the result
    logging.info(f"Calculated result: {operand1} {operation} {operand2} = {result}")
    # Save to the database
    calculation = CalculationHistory(
        operation=operation,
        operand1=operand1,
        operand2=operand2,
        result=result
    )
    db.add(calculation)
    db.commit()
    db.refresh(calculation)
    return {"result": result}
# Retrieve the calculation history
@app.get("/history", response_model=list[CalculationHistoryResponse])
async def get_history(db: Session = Depends(get_db)):
    history = db.query(CalculationHistory).all()
    return history