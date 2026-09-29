from dominio.empleado import Empleado
from dominio.departamento import Departamento
from persistencia.empleado_dao import EmpleadoDAO

"""empleado = Empleado(
    nombre="Ana Torres",
    correo="ana.torres@ecotech.cl"
)

departamento = Departamento("Desarrollo")

departamento.agregar_empleado(empleado)

print(departamento.cantidad_empleados())

for empleado in departamento.empleados:
    print(empleado.mostrar_datos())

# main.py
from persistencia.crear_db import crear_tablas
from dominio.empleado import Empleado
from persistencia.empleado_dao import EmpleadoDAO
crear_tablas()
empleado = Empleado(nombre="Ana Pérez", correo="ana@ecotech.cl")
print("Antes:", empleado.id)
# None
EmpleadoDAO.insertar(empleado)
print("Después:", empleado.id)
# id generado por la BD"""


empleado = Empleado(
nombre="Sergio Torres",
correo="sergio.torres@ecotech.cl"
)
EmpleadoDAO.insertar(empleado)

encontrado = EmpleadoDAO.buscar_por_id(empleado.id)
print("Encontrado:", encontrado)
print("Listado:")
for item in EmpleadoDAO.listar():
    print(item)



