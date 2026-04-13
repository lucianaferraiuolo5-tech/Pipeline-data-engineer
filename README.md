Data Pipeline - Crypto

Pipeline de datos que extrae información de una API de criptomonedas, la transforma y la guarda en una base de datos.

 Tecnologías
- Python
- Pandas
- SQLAlchemy
- SQLite

Flujo del pipeline
1. Extract: obtiene datos desde API (CoinGecko)
2. Transform: limpia y procesa los datos
3. Load: guarda en base de datos SQLite

Estructura
src/
- extract.py
- transform.py
- load.py
- main.py
- config.py

Automatización
El pipeline puede ejecutarse automáticamente mediante un archivo `.bat`.

Características
- Manejo de errores (try/except)
- Logging
- Configuración separada (config.py)

Cómo ejecutar

```bash
python -m src.main
