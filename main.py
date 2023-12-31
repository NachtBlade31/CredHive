from fastapi import FastAPI, Depends, HTTPException
from fastapi_limiter.depends import RateLimiter
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy import create_engine, Column, Integer, String, MetaData, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel
from typing import List


DATABASE_URL = "sqlite:///./credhive.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
metadata = MetaData()

Base = declarative_base()

# Define the SQLAlchemy model for credit information
class CreditInfoModel(Base):
    __tablename__ = "credit_info"

    id = Column(Integer, primary_key=True, index=True)
    company_name = Column(String, index=True)
    address = Column(String)
    registration_date = Column(String)
    number_of_employees = Column(Integer)
    raised_capital = Column(Float)
    turnover = Column(Float)
    net_profit = Column(Float)
    contact_number = Column(String)
    contact_email = Column(String)
    company_website = Column(String)
    loan_amount = Column(Float)
    loan_interest = Column(Float)
    account_status = Column(Boolean)

# Create the database tables
Base.metadata.create_all(bind=engine)

# Pydantic model for credit information
class CreditInfo(BaseModel):
    id: int
    company_name: str
    address: str
    registration_date: str
    number_of_employees: int
    raised_capital: float
    turnover: float
    net_profit: float
    contact_number: str
    contact_email: str
    company_website: str
    loan_amount: float
    loan_interest: float
    account_status: bool

# Pydantic model for credit information update
class CreditInfoUpdate(BaseModel):
    company_name: str = None
    address: str = None
    registration_date: str = None
    number_of_employees: int = None
    raised_capital: float = None
    turnover: float = None
    net_profit: float = None
    contact_number: str = None
    contact_email: str = None
    company_website: str = None
    loan_amount: float = None
    loan_interest: float = None
    account_status: bool = None

# OAuth2 token for authentication
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Create the database session using sessionmaker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Function to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Function to validate the token
def get_current_user(token: str = Depends(oauth2_scheme)):
    # This function can be extended to validate the token against a user database
    if token != "fake-token":
        raise HTTPException(status_code=401, detail="Invalid token")
    return token

app = FastAPI()

# API endpoint to retrieve a list of all credit information
@app.get("/credits", response_model=List[CreditInfo])
async def get_all_credits(db: Session = Depends(get_db)):
    credits = db.query(CreditInfoModel).all()
    return credits

# API endpoint to retrieve credit information for a specific user by ID
@app.get("/credits/{id}", response_model=CreditInfo)
async def get_credit_by_id(id: int, db: Session = Depends(get_db)):
    credit_info = db.query(CreditInfoModel).filter(CreditInfoModel.id == id).first()
    if credit_info is None:
        raise HTTPException(status_code=404, detail="Credit information not found")
    return CreditInfo(**credit_info.__dict__)

# API endpoint to add new credit information
@app.post("/credits", response_model=CreditInfo)
async def add_credit_info(
    credit_info: CreditInfo,
    current_user: str = Depends(get_current_user),
    rate_limiter: RateLimiter = Depends(),
    db: Session = Depends(get_db),
):
    # Check if the entry already exists
    existing_entry = (
        db.query(CreditInfoModel)
        .filter(CreditInfoModel.company_name == credit_info.company_name)
        .first()
    )
    existing_entry_by_id=(
        db.query(CreditInfoModel)
        .filter(CreditInfoModel.id == credit_info.id)
        .first()
    )
    if existing_entry :
        raise HTTPException(status_code=400, detail="Entry with this company name already exists")

    if existing_entry_by_id:
        raise HTTPException(status_code=400, detail="Entry with this ID already exists")

    # Save the credit information to the database
    db_credit_info = CreditInfoModel(**credit_info.dict())
    db.add(db_credit_info)
    db.commit()
    db.refresh(db_credit_info)
    return CreditInfo(**db_credit_info.__dict__)

# API endpoint to update credit information for a specific user
@app.put("/credits/{id}", response_model=CreditInfo)
async def update_credit_info(
    id: int,
    credit_info_update: CreditInfoUpdate,
    current_user: str = Depends(get_current_user),
    rate_limiter: RateLimiter = Depends(),
    db: Session = Depends(get_db),
):
    # Check if the entry exists
    db_credit_info = db.query(CreditInfoModel).filter(CreditInfoModel.id == id).first()
    if db_credit_info is None:
        raise HTTPException(status_code=404, detail="Credit information not found")

    # Update the credit information in the database
    for field, value in credit_info_update.dict(exclude_unset=True).items():
        setattr(db_credit_info, field, value)

    db.commit()
    db.refresh(db_credit_info)
    return CreditInfo(**db_credit_info.__dict__)

# API endpoint to delete credit information for a specific user
@app.delete("/credits/{id}")
async def delete_credit_info(
    id: int,
    current_user: str = Depends(get_current_user),
    rate_limiter: RateLimiter = Depends(),
    db: Session = Depends(get_db),
):
    # Check if the entry exists
    db_credit_info = db.query(CreditInfoModel).filter(CreditInfoModel.id == id).first()
    if db_credit_info is None:
        raise HTTPException(status_code=404, detail="Credit information not found")

    # Delete the credit information from the database
    db.delete(db_credit_info)
    db.commit()
    return {"message": "Credit information deleted successfully"}
