import pandas as pd
from app.core.config import settings
import logging

logger = logging.getLogger(__name__)

def load_companies():
    try:
        df = pd.read_csv(settings.COMPANIES_CSV)
        return df
    except Exception as e:
        logger.error(f"Error loading companies: {e}")
        return pd.DataFrame()

def get_all_companies():
    df = load_companies()
    return df.to_dict(orient='records')

def get_company_by_id(company_id: int):
    df = load_companies()
    company = df[df['company_id'] == company_id]
    if company.empty:
        logger.warning(f"Company with ID {company_id} not found.")
        return None
    return company.to_dict(orient='records')[0]
