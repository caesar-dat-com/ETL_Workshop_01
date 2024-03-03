import configparser
import psycopg2

config = configparser.ConfigParser()
config.read(r'C:\Users\cesar\Desktop\platzi\ETL_Workshop_01\db_config.ini')

dbname = config.get('postgresql', 'dbname')
user = config.get('postgresql', 'user')
password = config.get('postgresql', 'password')
host = config.get('postgresql', 'host')
port = config.get('postgresql', 'port')

try:
    # Establecer conexión a la base de datos
    conn = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port
    )
    conn.autocommit = True  # Importante para asegurar que los comandos se ejecuten sin necesidad de un commit explícito
    cur = conn.cursor()

    # Obtener una lista de todas las tablas en la base de datos
    cur.execute("""SELECT table_name FROM information_schema.tables
                   WHERE table_schema = 'public'""")
    tables = cur.fetchall()

    # Borrar todos los datos de cada tabla
    for table in tables:
        cur.execute(f"DELETE FROM {table[0]}")
        print(f"Todos los datos de la tabla {table[0]} han sido eliminados.")

except psycopg2.Error as e:
    print(f"Error al limpiar la base de datos: {e}")
finally:
    if cur:
        cur.close()
    if conn:
        conn.close()
