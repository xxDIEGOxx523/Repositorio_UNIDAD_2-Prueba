from dominio.empleado import Empleado
from dominio.departamento import Departamento


empleado = Empleado(
    nombre="Ana Torres",
    correo="ana.torres@ecotech.cl"
)

departamento = Departamento("Desarrollo")

departamento.agregar_empleado(empleado)

print(departamento.cantidad_empleados())

for empleado in departamento.empleados:
    print(empleado.mostrar_datos())
