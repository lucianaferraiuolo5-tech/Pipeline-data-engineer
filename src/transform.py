import logging
logging.basicConfig(level=logging.INFO)

def transform(df):
    try:
        if df is None:
            return None
        
        df = df[["name", "current_price","market_cap"]]
        
        df = df[df["current_price"] > 0]
        
        df["price_category"] = df["current_price"].apply(lambda x: "alto" if x > 1000 else "bajo")
        
        return df
    
    except Exception as e:
        logging.error(f"Error en transform: {e}")
        
        return None