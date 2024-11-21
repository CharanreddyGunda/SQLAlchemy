from sqlalchemy import Integer, Column, String
from database import Base

class CompanyDetails(Base):
    __tablename__ = 'company_details'

    id = Column(Integer, primary_key=True, index=True)
    company_name = Column(String(255), index=True)
    website = Column(String(255), index=True)
    job_type = Column(String, index = True)
    company_type = Column(String, index =True)
    company_size = Column(Integer)
    linkedin_url = Column(String, index=True)

