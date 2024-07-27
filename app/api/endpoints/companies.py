from fastapi import APIRouter, HTTPException
from typing import List
from app.services.company_service import get_all_companies, get_company_by_id
from app.models.company import Company

router = APIRouter()

@router.get("/", response_model=List[Company])
def read_companies():
    companies = get_all_companies()
    if not companies:
        raise HTTPException(status_code=404, detail="No companies found")
    return companies

@router.get("/{company_id}", response_model=Company)
def read_company(company_id: int):
    company = get_company_by_id(company_id)
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")
    return company
