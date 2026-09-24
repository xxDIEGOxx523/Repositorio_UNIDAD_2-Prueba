class Tarea:
    def __init__(self, nombre, descripcion, estado="Pendiente"):
        self.nombre = nombre
        self.descripcion = descripcion
        self.estado = estado

    def completar(self):
        self.estado = "Completada"

    def mostrar_datos(self):
        return f"Tarea: {self.nombre} | Estado: {self.estado}"
