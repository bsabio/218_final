from sqlalchemy import Column, Integer, Float, String
from database import Base
class CalculationHistory(Base):
    
    __tablename__ = 'calculation_history'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    operation = Column(String, nullable=False)
    operand1 = Column(Float, nullable=False)
    operand2 = Column(Float, nullable=False)
    result = Column(Float, nullable=False)