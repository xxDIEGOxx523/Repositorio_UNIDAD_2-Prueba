class Notificacion:
    def __init__(self, mensaje, tipo="General"):
        self.mensaje = mensaje
        self.tipo = tipo
        self._leida = False

    def marcar_leida(self):
        self._leida = True

    def esta_leida(self):
        return self._leida

    def mostrar(self):
        estado = "Leída" if self._leida else "No leída"
        return f"[{self.tipo}] {self.mensaje} - {estado}"
