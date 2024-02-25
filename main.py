import psycopg2
import pandas as pd
import configparser  # Importa el módulo configparser

# Leer el archivo de configuración
config = configparser.ConfigParser()
config.read('db_config.ini')

# Obtener las credenciales
host = config['postgresql']['host']
dbname = config['postgresql']['dbname']
user = config['postgresql']['user']
password = config['postgresql']['password']
port = config['postgresql']['port']

# Crear la conexión a la base de datos usando las credenciales leídas
conn = psycopg2.connect(
    host=host,
    dbname=dbname,
    user=user,
    password=password,
    port=port
)

# Consulta para seleccionar todo el contenido de la tabla 'candidates'
query = 'SELECT * FROM candidates;'

df = pd.read_sql(query, conn)

conn.close()

print(df.head())