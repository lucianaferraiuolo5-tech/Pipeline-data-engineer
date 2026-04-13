import logging
from sqlalchemy import create_engine
from src.config import DB_URL

logging.basicConfig(level=logging.INFO)

def load_db(df):
    try:
        if df is None:
            return
        
        engine = create_engine(DB_URL)
        df.to_sql("crypto", engine, if_exists="append", index=False)

        logging.info("Datos guardados en SQLite")
        
    except Exception as e:
        logging.error(f"Error en load: {e}")
        
    