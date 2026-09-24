from .empleado import Empleado
from .proyecto import Proyecto


class Tarea:
    def __init__(
        self,
        nombre: str,
        descripcion: str,
        empleado: Empleado,
        proyecto: Proyecto,
        estado: str = "Pendiente"
    ):
        self.nombre = nombre
        self.descripcion = descripcion
        self.empleado = empleado
        self.proyecto = proyecto
        self.estado = estado

    def completar(self):
        self.estado = "Completada"

    def mostrar_datos(self):
        return (
            f"Tarea: {self.nombre} | "
            f"Proyecto: {self.proyecto.nombre} | "
            f"Empleado: {self.empleado.nombre} | "
            f"Estado: {self.estado}"
        )
