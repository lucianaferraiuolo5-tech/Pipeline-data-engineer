import time
import logging
from src.extract import extract_api
from src.transform import transform
from src.load import load_db

logging.basicConfig(level=logging.INFO)

def main():
  
    df = extract_api() # trae datos
    df = transform(df) # limpiar/transformar
    load_db(df)           # guardar
        
        
    logging.info("Pipeline ejecutandose una vez")
    logging.info("Pipeline ejecutandose correctamente")
        
    time.sleep(60); # espera un minuto
        
if __name__ == "__main__":
    main() 