class Departamento:
    def __init__(self, nombre):
        self.nombre = nombre

class Empleado:
    def __init__(self, nombre, departamento):
        self.nombre = nombre
        self.departamento = departamento

class Proyecto:
    def __init__(self, nombre, empleado):
        self.nombre = nombre
        self.empleado = empleado

class RegistroTiempo:
    def __init__(self):
        self.registros = []

    def agregar_registro(self, empleado, proyecto, horas):
        self.registros.append({
            'empleado': empleado.nombre,
            'proyecto': proyecto.nombre,
            'horas': horas
        })

    def mostrar_registros(self):
        for registro in self.registros:
            print(f"Empleado: {registro['empleado']}, Proyecto: {registro['proyecto']}, Horas: {registro['horas']}")