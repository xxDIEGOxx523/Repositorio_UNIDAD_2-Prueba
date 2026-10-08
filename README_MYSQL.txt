POOS - ECOTECH SOLUTIONS
========================

El proyecto utiliza exclusivamente MySQL y mysql-connector-python.
No contiene otro motor de base de datos.

1. Crear entorno virtual desde la carpeta del proyecto:
python -m venv venv
source venv/Scripts/activate

2. Instalar dependencias:
pip install -r requirements.txt

3. Crear un archivo .env en la carpeta del proyecto usando .env.example:
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=tu_contraseña
DB_NAME=ecotech_db

4. Ejecutar desde DOC_2/src:
python main.py

El programa crea la base de datos y las tablas automáticamente.
También se incluye ecotech_mysql.sql para crear la estructura manualmente.

Tablas:
departamento
empleado
proyecto
empleado_proyecto
registro_tiempo

El proyecto usa DAO, DAOFactory, encapsulamiento, relaciones entre
entidades, CRUD, validaciones y try-except.
