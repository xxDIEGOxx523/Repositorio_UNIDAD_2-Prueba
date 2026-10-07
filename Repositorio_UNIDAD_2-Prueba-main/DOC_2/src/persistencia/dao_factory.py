# Importaciones de tus DAOs de SQLite
from .registro_tiempo_dao import SQLiteRegistroTiempoDAO
from .empleado_dao import SQLiteEmpleadoDAO
# (Importar de igual manera tus DAOs de Proyecto y Departamento)

# Importaciones de tus DAOs de MySQL (Si ya creaste los archivos .py correspondientes)
# from .mysql_daos import MySQLRegistroTiempoDAO, MySQLEmpleadoDAO

class DAOFactory:
    def __init__(self, motor: str, config: dict = None):
        self.motor = motor.lower()
        self.config = config
        if self.motor == "mysql" and not config:
            raise ValueError("Se requiere configuración de conexión para MySQL.")

    def get_registro_tiempo_dao(self):
        return SQLiteRegistroTiempoDAO() if self.motor == "sqlite" else MySQLRegistroTiempoDAO(self.config)

    def get_empleado_dao(self):
        return SQLiteEmpleadoDAO() if self.motor == "sqlite" else MySQLEmpleadoDAO(self.config)

    def get_proyecto_dao(self):
        # Retorna la implementación según corresponda
        pass

    def get_departamento_dao(self):
        # Retorna la implementación según corresponda
        pass
