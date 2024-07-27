from fastapi import APIRouter
from app.services.location_statistics_service import (
    # get_total_locations,
    # get_locations_per_company,
    # get_latitude_longitude_statistics,
    get_top_cities_with_most_jobs,
    get_top_states_with_most_jobs
)

router = APIRouter()

# @router.get("/total-locations")
# def total_locations():
#     return {"total_locations": get_total_locations()}

# @router.get("/locations-per-company")
# def locations_per_company():
#     return get_locations_per_company()

@router.get("/top-cities-with-most-jobs")
def top_cities_with_most_jobs():
    return get_top_cities_with_most_jobs()

@router.get("/top-states-with-most-jobs")
def top_states_with_most_jobs():
    return get_top_states_with_most_jobs()
