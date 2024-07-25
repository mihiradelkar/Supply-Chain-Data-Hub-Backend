from fastapi import APIRouter, HTTPException
from typing import List
from app.services.location_service import get_locations_by_company_id
from app.models.location import Location

router = APIRouter()

@router.get("/{company_id}", response_model=List[Location])
def read_locations(company_id: int):
    locations = get_locations_by_company_id(company_id)
    if not locations:
        raise HTTPException(status_code=404, detail="No locations found for this company")
    return locations
