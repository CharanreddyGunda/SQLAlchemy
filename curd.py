from pydantic import BaseModel
from dependency import db_dependency
import models

class CompanyDetailsBase(BaseModel):
    company_name : str
    website : str
    job_type : str
    company_type : str
    company_size : str
    linkedin_url : str



def create_company_details(company: CompanyDetailsBase, db: db_dependency):
    db_company_details = models.CompanyDetails(company_name = company.company_name, 
            website = company.website,job_type=company.job_type, company_type =  company.company_type,
            company_size=company.company_size, linkedin_url = company.linkedin_url)
    db.add(db_company_details)
    db.commit()
    db.refresh(db_company_details)
    return {"description":"Company details saved successfully"}

def get_company_details(db: db_dependency):
    db_all_company_details = db.query(models.CompanyDetails).all()
    return db_all_company_details

def get_company_details_by_id(company_id: int, db: db_dependency):
    db_company_details = db.query(models.CompanyDetails).filter(models.CompanyDetails.id == company_id).first()
    return db_company_details