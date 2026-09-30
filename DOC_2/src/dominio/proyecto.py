from .empleado import Empleado


class Proyecto:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self._empleados = []

    def agregar_empleado(self, empleado: Empleado):
        if empleado not in self._empleados:
            self._empleados.append(empleado)

    @property
    def empleados(self):
        return tuple(self._empleados)
