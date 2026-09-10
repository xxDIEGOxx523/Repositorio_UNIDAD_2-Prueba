from dominio.empleado import Empleado
from dominio.desarrollo import Desarrollo  # type: ignore # Assuming Desarrollo is the correct class to import

empleado = Empleado(
    nombre="Ana Torres",
    correo="ana.torres@ecotech.cl"
)

desarrollo = Desarrollo()  # Create an instance of Desarrollo
desarrollo.agregar_empleado(empleado)  # Use empleado instead of ana
print(desarrollo.cantidad_empleados())
for empleado in desarrollo.empleados:
    print(empleado.mostrar_datos())
