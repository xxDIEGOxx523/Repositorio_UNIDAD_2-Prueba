lass Empleado:
def __init__(self, nombre, correo, id=None):
    self.id = id
    self.nombre = nombre
    self.correo = correo

    # Asegúrate de que este nombre tenga los guiones bajos completos:
    def mostrar_datos(self) -> str:
        return f"Empleado: {self.nombre} | Correo: {self.correo}"   