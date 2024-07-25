import pandas as pd
from app.core.config import settings

def load_companies():
    return pd.read_csv(settings.COMPANIES_CSV)

def get_all_companies():
    df = load_companies()
    return df.to_dict(orient='records')

def get_company_by_id(company_id: int):
    df = load_companies()
    company = df[df['company_id'] == company_id]
    if company.empty:
        return None
    return company.to_dict(orient='records')[0]
