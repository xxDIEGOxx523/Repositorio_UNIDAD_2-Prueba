import sqlite3
from datetime import datetime
from typing import List, Dict, Any
from .modelo import RegistroTiempo

class RegistroTiempoDAO:
    def __init__(self, db_path: str = "gestion_tiempo.db"):
        self.db_path = db_path
        self._crear_tabla_si_no_existe()

    def _get_connection(self):
        """Establece la conexión con la base de datos."""
        return sqlite3.connect(self.db_path)

    def _crear_tabla_si_no_existe(self):
        """Inicializa las tablas base si el archivo .db es nuevo."""
        with self._get_connection() as conn:
            cursor = conn.cursor()
            
            # Tablas simuladas de Empleado y Proyecto para mantener integridad referencial
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS empleado (
                    id_empleado INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL
                )
            """)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS proyecto (
                    id_proyecto INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL
                )
            """)
            
            # Tabla Principal de Registro de Tiempo
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS registro_tiempo (
                    id_registro INTEGER PRIMARY KEY AUTOINCREMENT,
                    id_empleado INTEGER NOT NULL,
                    id_proyecto INTEGER NOT NULL,
                    horas REAL NOT NULL,
                    fecha TEXT NOT NULL,
                    FOREIGN KEY (id_empleado) REFERENCES empleado (id_empleado),
                    FOREIGN KEY (id_proyecto) REFERENCES proyecto (id_proyecto)
                )
            """)
            
            # Insertar datos de prueba si están vacías
            cursor.execute("SELECT COUNT(*) FROM empleado")
            if cursor.fetchone()[0] == 0:
                cursor.executemany("INSERT INTO empleado (nombre) VALUES (?)", [("Juan Pérez",), ("María López",)])
                cursor.executemany("INSERT INTO proyecto (nombre) VALUES (?)", [("Sistema ERP",), ("App Móvil",)])
            
            conn.commit()

    def insertar(self, registro: RegistroTiempo) -> bool:
        """Inserta un nuevo registro de tiempo en la base de datos."""
        query = """
            INSERT INTO registro_tiempo (id_empleado, id_proyecto, horas, fecha)
            VALUES (?, ?, ?, ?)
        """
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(query, (
                    registro.id_empleado, 
                    registro.id_proyecto, 
                    registro.horas, 
                    registro.fecha.strftime("%Y-%m-%d")
                ))
                conn.commit()
                return True
        except sqlite3.Error as e:
            print(f"\n❌ Error de Base de Datos al insertar: {e}")
            return False

    def obtener_todos_con_detalles(self) -> List[Dict[str, Any]]:
        """Realiza un JOIN para traer los nombres reales en lugar de solo IDs numéricos."""
        query = """
            SELECT r.fecha, e.nombre, p.nombre, r.horas
            FROM registro_tiempo r
            JOIN empleado e ON r.id_empleado = e.id_empleado
            JOIN proyecto p ON r.id_proyecto = p.id_proyecto
            ORDER BY r.fecha DESC, r.id_registro DESC
        """
        resultados = []
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(query)
                for fila in cursor.fetchall():
                    resultados.append({
                        "fecha": fila[0],
                        "empleado": fila[1],
                        "proyecto": fila[2],
                        "horas": fila[3]
                    })
        except sqlite3.Error as e:
            print(f"\n❌ Error al consultar registros: {e}")
        return resultados
