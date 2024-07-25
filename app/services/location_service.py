import pandas as pd
from app.core.config import settings

def load_locations():
    return pd.read_csv(settings.LOCATIONS_CSV)

def get_locations_by_company_id(company_id: int):
    df = load_locations()
    locations = df[df['company_id'] == company_id]
    if locations.empty:
        return []
    return locations.to_dict(orient='records')
