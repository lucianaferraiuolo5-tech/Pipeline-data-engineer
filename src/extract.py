from src.config import API_URL, PARAMS
import requests
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)

def extract_api():
    try:
        response = requests.get(API_URL, params=PARAMS)
        data = response.json()
    
        df = pd.DataFrame(data)
        return df 
    
    except Exception as e:
        logging.error(f"Error en extract: {e}")
        return None