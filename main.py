from fastapi import Depends, FastAPI
from typing import Annotated
from database import SessionLocal, create_db
from sqlalchemy.orm import Session
from dependency import db_dependency
import models
from curd import CompanyDetailsBase, create_company_details, get_company_details, get_company_details_by_id

app = FastAPI()

# Call create_db() to create tables at startup
create_db()

@app.get("/")
async def home():
    return {"key": "welcome"}


@app.post("/api/companydetails")
async def add_company(comp : CompanyDetailsBase, db: db_dependency):
    return create_company_details(company=comp,db=db)


@app.get("/api/companydetails/get")
async def get_company(db: db_dependency):
    return get_company_details(db=db)


@app.get("/api/companydetails/get/{company_id}")
async def get_company(company_id: int, db: db_dependency):
    return get_company_details_by_id()