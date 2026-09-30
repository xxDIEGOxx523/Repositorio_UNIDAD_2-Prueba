import os
import sqlite3
import pymysql
from dotenv import load_dotenv

load_dotenv()


def obtener_motor():
    # Forzamos a que el motor siempre sea mysql
    return "mysql"


def abrir_conexion():
    # Conexión directa a tu MySQL Workbench local
    return pymysql.connect(
        host="localhost",
        port=3307,
        user="root",
        password="",  # <-- ESCRIBE AQUÍ TU CONTRASEÑA REAL DE WORKBENCH
        database="ecotech_db",              # El nombre de la base de datos que creamos
        charset="utf8mb4",
    )

def marcador_sql():
    return "%s"
