from .empleado import Empleado
from .proyecto import Proyecto


class RegistroTiempo:
    def __init__(self):
        self._registros = []

    def agregar_registro(self, empleado: Empleado, proyecto: Proyecto, horas: int):
        self._registros.append({
            "empleado": empleado,
            "proyecto": proyecto,
            "horas": horas
        })

    @property
    def registros(self):
        return tuple(self._registros)

    def mostrar_registros(self):
        for registro in self._registros:
            print(
                f"Empleado: {registro['empleado'].nombre}, "
                f"Proyecto: {registro['proyecto'].nombre}, "
                f"Horas: {registro['horas']}"
            )
