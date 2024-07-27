import pandas as pd
from app.core.config import settings

def load_locations():
    return pd.read_csv(settings.LOCATIONS_CSV)

def parse_address(address):
    try:
        parts = address.split(',')
        city = parts[1].strip()
        state_zip = parts[2].strip() if len(parts) > 1 else ''
        state = state_zip.split(' ')[0].strip() if state_zip else ''
        print(f'City: {city}, State: {state}')
        return city, state
    except Exception as e:
        return '', ''

def get_top_states_with_most_jobs(top_n=10):
    df = load_locations()
    df['state'] = df['address'].apply(lambda x: parse_address(x)[1])
    top_states = df['state'].value_counts().head(top_n).to_dict()
    return top_states

def get_top_cities_with_most_jobs(top_n=10):
    df = load_locations()
    df['city'] = df['address'].apply(lambda x: parse_address(x)[0])
    top_cities = df['city'].value_counts().head(top_n).to_dict()
    return top_cities
