from datetime import date, datetime
import sys

from dominio.empleado import Empleado
from dominio.departamento import Departamento
from dominio.proyecto import Proyecto
from dominio.registrotiempo import RegistroTiempo


class TerminalInterface:
    def __init__(self, registro_dao, empleado_dao, proyecto_dao, departamento_dao):
        self.registro_dao = registro_dao
        self.empleado_dao = empleado_dao
        self.proyecto_dao = proyecto_dao
        self.departamento_dao = departamento_dao

    def mostrar_menu(self):
        print("\n=== ECOTECH SOLUTIONS ===")
        print("1. Registrar empleado")
        print("2. Listar empleados")
        print("3. Registrar departamento")
        print("4. Listar departamentos")
        print("5. Registrar proyecto")
        print("6. Listar proyectos")
        print("7. Registrar tiempo")
        print("8. Listar registros de tiempo")
        print("9. Salir")

    def iniciar(self):
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ").strip()
            try:
                acciones = {
                    "1": self._registrar_empleado,
                    "2": lambda: self._listar(self.empleado_dao, "EMPLEADOS"),
                    "3": self._registrar_departamento,
                    "4": lambda: self._listar(self.departamento_dao, "DEPARTAMENTOS"),
                    "5": self._registrar_proyecto,
                    "6": lambda: self._listar(self.proyecto_dao, "PROYECTOS"),
                    "7": self._registrar_tiempo,
                    "8": self._mostrar_listado_tiempos,
                }
                if opcion == "9":
                    print("Sistema finalizado.")
                    sys.exit()
                accion = acciones.get(opcion)
                if accion:
                    accion()
                else:
                    print("Opción no válida.")
            except Exception as e:
                print(f"Error: {e}")

    def _registrar_empleado(self):
        print("\n--- NUEVO EMPLEADO ---")
        empleado = Empleado(
            input("Nombre: ").strip(),
            input("Dirección: ").strip(),
            input("Teléfono: ").strip(),
            input("Correo: ").strip(),
            self._pedir_fecha("Fecha de inicio (YYYY-MM-DD): "),
            self._pedir_float("Salario: "),
        )
        self.empleado_dao.insertar(empleado)
        print(f"Empleado registrado con ID {empleado.id_empleado}.")

    def _registrar_departamento(self):
        departamento = Departamento(input("Nombre del departamento: ").strip())
        self.departamento_dao.insertar(departamento)
        print(f"Departamento registrado con ID {departamento.id_departamento}.")

    def _registrar_proyecto(self):
        proyecto = Proyecto(
            input("Nombre: ").strip(),
            input("Descripción: ").strip(),
            self._pedir_fecha("Fecha de inicio (YYYY-MM-DD): "),
        )
        self.proyecto_dao.insertar(proyecto)
        print(f"Proyecto registrado con ID {proyecto.id_proyecto}.")

    def _registrar_tiempo(self):
        registro = RegistroTiempo(
            self._pedir_fecha("Fecha (YYYY-MM-DD): "),
            self._pedir_float("Horas trabajadas: "),
            input("Descripción del trabajo: ").strip(),
            self._pedir_int("ID empleado: "),
            self._pedir_int("ID proyecto: "),
        )
        self.registro_dao.insertar(registro)
        print(f"Registro de tiempo guardado con ID {registro.id_registro}.")

    def _listar(self, dao, titulo):
        print(f"\n--- {titulo} ---")
        datos = dao.obtener_todos()
        if not datos:
            print("No hay registros.")
            return
        for dato in datos:
            print(dato)

    def _mostrar_listado_tiempos(self):
        print("\n--- REGISTROS DE TIEMPO ---")
        registros = self.registro_dao.obtener_todos_con_detalles()
        if not registros:
            print("No hay registros.")
            return
        for registro in registros:
            print(
                f"ID: {registro['id_registro']} | Fecha: {registro['fecha']} | "
                f"Empleado: {registro['empleado']} | Proyecto: {registro['proyecto']} | "
                f"Horas: {registro['horas']} | Descripción: {registro['descripcion']}"
            )

    @staticmethod
    def _pedir_int(mensaje):
        while True:
            try:
                return int(input(mensaje))
            except ValueError:
                print("Ingrese un número entero válido.")

    @staticmethod
    def _pedir_float(mensaje):
        while True:
            try:
                valor = float(input(mensaje))
                if valor < 0:
                    raise ValueError
                return valor
            except ValueError:
                print("Ingrese un número válido mayor o igual a 0.")

    @staticmethod
    def _pedir_fecha(mensaje):
        while True:
            try:
                return datetime.strptime(input(mensaje).strip(), "%Y-%m-%d").date()
            except ValueError:
                print("Formato inválido. Use YYYY-MM-DD.")
