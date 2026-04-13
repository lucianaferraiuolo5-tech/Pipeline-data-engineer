Data Pipeline - Crypto

Pipeline de datos que extrae información de una API de criptomonedas, la transforma y la guarda en una base de datos.

Tecnologías
Python
Pandas
SQLAlchemy
SQLite
AWS EC2
Cron (automatización)

Flujo del pipeline
Extract: obtiene datos desde API (CoinGecko)
Transform: limpia y procesa los datos
Load: guarda en base de datos SQLite

Estructura
src/
- extract.py
- transform.py
- load.py
- main.py
- config.py
  
Automatización en AWS
El pipeline está desplegado en una instancia de AWS EC2 y se ejecuta automáticamente mediante un cron job cada 5 minutos.
Este proceso permite la ingesta, transformación y almacenamiento continuo de datos sin intervención manual.
La ejecución se realiza en un entorno Linux utilizando un entorno virtual de Python, y cuenta con un sistema de logs para el monitoreo del pipeline.

Automatización local
El pipeline también puede ejecutarse automáticamente en entorno local mediante un archivo .bat.

 Características
Manejo de errores (try/except)
Logging
Configuración separada (config.py)
Ejecución automática (local y en la nube)
▶️ Cómo ejecutar
python -m src.main
