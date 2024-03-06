# ETL_Workshop_01
---

# ETL Workshop: Flujo de Trabajo

## Propósito del Taller
Este taller está diseñado para simular un escenario real de procesamiento de datos, proporcionando a los participantes experiencia práctica en la implementación de un flujo de trabajo ETL (Extract, Transform, Load). El objetivo es equipar a los aspirantes a ingenieros de datos con las habilidades necesarias para manejar, transformar y analizar datos de manera efectiva, utilizando herramientas y técnicas que son esenciales en la industria del Big Data.

## Objetivos del Proyecto
- Familiarizar a los participantes con el proceso de importación y manipulación de datos utilizando Python y Pandas.
- Desarrollar habilidades en la creación y gestión de bases de datos utilizando SQL.
- Proporcionar experiencia práctica en la conexión y manipulación de datos a través de interfaces de línea de comandos.
- Analizar y extraer insights valiosos de conjuntos de datos reales o simulados.
- Preparar a los participantes para desafíos comunes en roles de ingeniería de datos y ciencia de datos.

## Etapas del Proceso

### Conceptos Clave
- **Cursor:** En bases de datos, un cursor es una estructura que permite recorrer y manipular las filas devueltas por las consultas SQL de manera secuencial. Es fundamental para operaciones detalladas sobre los datos.
- **Conexión:** Representa una sesión entre un programa de aplicación y una base de datos. Es el canal a través del cual el programa envía consultas y recibe resultados de la base de datos, establecida con parámetros específicos de conexión.

### Importar Datos desde CSV a PostgreSQL con Python
- Este script es una guía paso a paso para importar datos de un archivo CSV a una tabla en una base de datos PostgreSQL. La operación se realiza en varias etapas clave, garantizando una transferencia de datos eficiente y organizada.

- **Preparativos Iniciales**
- **-Preparativos Iniciales:**  El proceso inicia con la lectura de parámetros de conexión desde un archivo db_config.ini utilizando configparser. Esto incluye información como el nombre de la base de datos, usuario, contraseña, host y puerto.
- **Conexión a la Base de Datos:** Con estos parámetros, se establece una conexión a la base de datos PostgreSQL y se crea un cursor. Este cursor será esencial para ejecutar comandos SQL posteriormente.

- **Importación de Datos**
- **Apertura del Archivo CSV:** El script localiza y abre el archivo CSV especificado en csv_file_path. Es importante ajustar la ruta al entorno actual y asegurarse de que el delimitador en csv.reader coincida con el del archivo.
- **Lectura y Inserción de Datos:** 
- Se omite la primera línea del CSV (usualmente el encabezado) para evitar insertarla como un registro en la base de datos.
- Se lee cada fila del archivo CSV y se inserta en la tabla candidates de la base de datos utilizando una instrucción SQL INSERT. Cada valor de la fila se pasa como un parámetro a la consulta, correspondiendo a las columnas de la tabla.

- **Finalización y Limpieza**
- **Persistencia y Cierre:** 
- Se ejecuta un commit para hacer permanentes los cambios en la base de datos.
- Se cierran el cursor y la conexión para liberar recursos y asegurar la integridad de la sesión con la base de datos.

### Consulta Rápida en PostgreSQL con Python
Este script demuestra cómo realizar y procesar una consulta básica en PostgreSQL, extrayendo y visualizando los primeros 30 registros de la tabla candidates.

- **Pasos Clave**
- **Configuración:** Lee los detalles de conexión de db_config.ini usando configparser y establece una conexión a la base de datos PostgreSQL con psycopg2.
- **Consulta y Resultados:** 
- Ejecuta SELECT * FROM candidates LIMIT 30 para obtener los primeros 30 registros.
- Recupera y muestra los nombres de las columnas seguidos de cada registro, separando los valores con | para una visualización clara.
- **Manejo de Excepciones y Cierre:** 
- Captura errores durante la consulta para manejo de fallos.
- Cierra el cursor y la conexión al finalizar para liberar recursos.
----------------------

# ETL_Workshop_01
---

# ETL Workshop: Workflow

## Purpose of the Workshop
This workshop is designed to simulate a real-life data processing scenario, providing participants with hands-on experience in implementing an ETL (Extract, Transform, Load) workflow. The goal is to equip aspiring data engineers with the necessary skills to handle, transform, and analyze data effectively, using tools and techniques that are essential in the Big Data industry.

## Project Objectives
- To familiarize participants with the process of importing and manipulating data using Python and Pandas.
- To develop skills in creating and managing databases using SQL.
- To provide practical experience in connecting and manipulating data through command-line interfaces.
- To analyze and extract valuable insights from real or simulated datasets.
- To prepare participants for common challenges in data engineering and data science roles.

## Process Stages

### Key Concepts
- **Cursor:** In databases, a cursor is a structure that allows traversal and manipulation of the rows returned by SQL queries sequentially. It is essential for detailed operations on data.
- **Connection:** Represents a session between an application program and a database. It is the channel through which the program sends queries and receives results from the database, established with specific connection parameters.

### Importing Data from CSV to PostgreSQL with Python
- This script is a step-by-step guide to importing data from a CSV file into a table in a PostgreSQL database. The operation is performed in several key stages, ensuring an efficient and organized data transfer.

- **Initial Preparations**
  - **Initial Preparations:** The process begins with reading connection parameters from a db_config.ini file using configparser. This includes information such as the database name, user, password, host, and port.
  - **Connecting to the Database:** With these parameters, a connection to the PostgreSQL database is established, and a cursor is created. This cursor will be essential for executing SQL commands later on.

- **Data Importation**
  - **Opening the CSV File:** The script locates and opens the specified CSV file in csv_file_path. It is important to adjust the path to the current environment and ensure that the delimiter in csv.reader matches that of the file.
  - **Reading and Inserting Data:**
    - The first line of the CSV (usually the header) is skipped to avoid inserting it as a record in the database.
    - Each row from the CSV file is read and inserted into the candidates table in the database using an SQL INSERT statement. Each row's value is passed as a parameter to the query, corresponding to the table columns.

- **Finalization and Cleanup**
  - **Persistence and Closure:** 
    - A commit is executed to make the changes permanent in the database.
    - The cursor and connection are closed to release resources and ensure the integrity of the session with the database.

### Quick Query in PostgreSQL with Python
This script demonstrates how to perform and process a basic query in PostgreSQL, extracting and displaying the first 30 records from the candidates table.

- **Key Steps**
  - **Setup:** Reads connection details from db_config.ini using configparser and establishes a connection to the PostgreSQL database with psycopg2.
  - **Query and Results:** 
    - Executes SELECT * FROM candidates LIMIT 30 to obtain the first 30 records.
    - Retrieves and displays the column names followed by each record, separating values with | for clear visualization.
  - **Exception Handling and Closure:** 
    - Captures errors during the query for failure management.
    - Closes the cursor and connection at the end to release resources.

## Imagen Descriptiva del Proyecto
![ETL Workshop](https://media.licdn.com/dms/image/D4E22AQFzbHItrCQxSA/feedshare-shrink_800/0/1707950378509?e=1711584000&v=beta&t=p4_P3i7UuPEdx_lBHWLHWsaHKEMaO-cj5xlmZ2S5Hys)

## Publicaciones de LinkedIn
Para más información sobre este proyecto y su contexto, visita las siguientes publicaciones en LinkedIn:

- [ETL Workshop LinkedIn Post - Inglés](https://www.linkedin.com/posts/cesar-reyes-8a60622b2_dataengineering-python-etl-activity-7163663108039761921-RXsZ?utm_source=share&utm_medium=member_desktop)
- [ETL Workshop LinkedIn Post - Español](https://www.linkedin.com/posts/cesar-reyes-8a60622b2_dataengineering-python-etl-activity-7163662730439163905-LeX3?utm_source=share&utm_medium=member_desktop)

---
