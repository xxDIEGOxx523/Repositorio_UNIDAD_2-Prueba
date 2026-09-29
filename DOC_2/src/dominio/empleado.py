class Empleado:
    def __init__(self, nombre: str, correo: str, id: int = None):
        self.id = id
        self.nombre = nombre
        self.correo = correo
    def __str__(self):
        return f"Empleado [ID: {self.id} | Nombre: {self.nombre} | Correo: {self.correo}]"
    def mostrar_datos(self) -> str:
        return f"Empleado: {self.nombre} | Correo: {self.correo}"
