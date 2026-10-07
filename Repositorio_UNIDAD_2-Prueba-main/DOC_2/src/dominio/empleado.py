from dominio.empleado import Empleado


class Proyecto:
    def __init__(self, nombre, id=None):
        self.id = id
        self.nombre = nombre
        self.empleados_list = []

    def agregar_empleado(self, empleado):
        if not isinstance(empleado, Empleado):
            raise TypeError("Solo se pueden asignar objetos Empleado.")

        if empleado in self.empleados_list:
            return False

        self.empleados_list.append(empleado)
        return True

    def quitar_empleado(self, empleado):
        if empleado not in self.empleados_list:
            return False

        self.empleados_list.remove(empleado)
        return True

    @property
    def empleados(self):
        return tuple(self.empleados_list)

    def cantidad_empleados(self):
        return len(self.empleados_list)

    def mostrar_datos(self):
        return f"{self.nombre} ({self.cantidad_empleados()} empleados)"

    def __str__(self):
        return self.mostrar_datos()
