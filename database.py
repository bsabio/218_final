from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the database URL (SQLite for simplicity)
DATABASE_URL = "sqlite:///calculator.db"

# Create the database engine
engine = create_engine(DATABASE_URL, echo=True)

# Define a base class for declarative models
Base = declarative_base()

# Define the CalculationHistory model
class CalculationHistory(Base):
    __tablename__ = "calculation_history"

    id = Column(Integer, primary_key=True, autoincrement=True)
    operation = Column(String, nullable=False)
    input_1 = Column(Float, nullable=False)
    input_2 = Column(Float, nullable=False)
    result = Column(Float, nullable=False)

    def __repr__(self):
        return (
            f"<CalculationHistory(id={self.id}, operation={self.operation}, "
            f"input_1={self.input_1}, input_2={self.input_2}, result={self.result})>"
        )

# Create the table
Base.metadata.create_all(engine)

# Create a session maker
Session = sessionmaker(bind=engine)

# Function to add a calculation to the history
def add_calculation(operation, input_1, input_2, result):
    session = Session()
    new_calculation = CalculationHistory(
        operation=operation, input_1=input_1, input_2=input_2, result=result
    )
    session.add(new_calculation)
    session.commit()
    session.close()

# Function to retrieve all calculations
def get_calculations():
    session = Session()
    calculations = session.query(CalculationHistory).all()
    session.close()
    return calculations

if __name__ == "__main__":
    # Example usage
    add_calculation("add", 2.5, 3.5, 6.0)
    add_calculation("multiply", 4.0, 2.0, 8.0)
    print(get_calculations())
