import os

class Settings:
    PROJECT_NAME: str = "Supply-Chain-Data-Hub-Backend"
    API_V1_STR: str = "/api"
    COMPANIES_CSV: str = os.getenv("COMPANIES_CSV", "app/data/companies.csv")
    LOCATIONS_CSV: str = os.getenv("LOCATIONS_CSV", "app/data/locations.csv")

settings = Settings()
