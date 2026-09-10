class Empleado:
    def __init__(self, nombre, id_empleado):
        self.nombre = nombre
        self.id_empleado = id_empleado
        self.registros_tiempo = []

    def agregar_registro_tiempo(self, registro):
        self.registros_tiempo.append(registro)


class RegistroTiempo:
    def __init__(self, fecha, horas_trabajadas):
        self.fecha = fecha
        self.horas_trabajadas = horas_trabajadas


# Ejemplo de uso
empleado1 = Empleado("Juan Pérez", 1)
registro1 = RegistroTiempo("2023-10-01", 8)
empleado1.agregar_registro_tiempo(registro1)