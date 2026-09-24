from .empleado import Empleado


class Notificacion:
    def __init__(
        self,
        mensaje: str,
        empleado: Empleado,
        tipo: str = "General"
    ):
        self.mensaje = mensaje
        self.empleado = empleado
        self.tipo = tipo
        self._leida = False

    def marcar_leida(self):
        self._leida = True

    def esta_leida(self):
        return self._leida

    def mostrar(self):
        estado = "Leída" if self._leida else "No leída"

        return (
            f"Notificación para {self.empleado.nombre}: "
            f"{self.mensaje} | "
            f"Tipo: {self.tipo} | "
            f"Estado: {estado}"
        )
