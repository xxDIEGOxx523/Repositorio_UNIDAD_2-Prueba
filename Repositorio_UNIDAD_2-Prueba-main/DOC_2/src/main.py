from persistencia.dao_factory import DAOFactory
from ux.interfaz import TerminalInterface

def main():
    # CONFIGURACIÓN DINÁMICA: Cambia a "sqlite" o "mysql" según requieras
    MOTOR_BD = "sqlite" 
    
    # Credenciales en caso de levantar el entorno de MySQL
    MYSQL_CONFIG = {
        "host": "localhost",
        "user": "root",
        "password": "tu_password",
        "database": "ecotech_db"
    }

    # 1. Instanciar la fábrica con el motor configurado
    factory = DAOFactory(MOTOR_BD, config=MYSQL_CONFIG)

    # 2. Obtener los DAOs correspondientes de forma transparente
    registro_dao = factory.get_registro_tiempo_dao()
    empleado_dao = factory.get_empleado_dao()
    proyecto_dao = factory.get_proyecto_dao()
    departamento_dao = factory.get_departamento_dao()

    # 3. Encender la interfaz inyectándole los accesos a datos
    app = TerminalInterface(registro_dao, empleado_dao, proyecto_dao, departamento_dao)
    app.iniciar()

if __name__ == "__main__":
    main()





