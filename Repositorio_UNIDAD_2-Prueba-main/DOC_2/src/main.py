import sys
from dominio.empleado import Empleado
from persistencia.empleado_dao import EmpleadoDAO

def mostrar_menu():
    print("\n" + "="*30)
    print("      SISTEMA ECOTECH - CRUD")
    print("="*30)
    print("1. Añadir Empleado")
    print("2. Listar Empleados")
    print("3. Actualizar Empleado")
    print("4. Eliminar Empleado")
    print("5. Salir")
    print("="*30)

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-5): ").strip()

        if opcion == "1":
            print("\n--- AÑADIR NUEVO EMPLEADO ---")
            nombre = input("Nombre: ")
            correo = input("Correo electrónico: ")
            
            nuevo = Empleado(nombre=nombre, correo=correo)
            EmpleadoDAO.insertar(nuevo)
            print(f"¡Éxito! Empleado añadido con el ID: {nuevo.id}")

        elif opcion == "2":
            print("\n--- LISTA DE EMPLEADOS ---")
            empleados = EmpleadoDAO.listar()
            if not empleados:
                print("No hay empleados registrados en la base de datos.")
            for emp in empleados:
                print(f"ID: {emp.id} | Nombre: {emp.nombre} | Correo: {emp.correo}")

        elif opcion == "3":
            print("\n--- ACTUALIZAR EMPLEADO EXISTENTE ---")
            try:
                id_modificar = int(input("Ingresa el ID del empleado a modificar: "))
                emp = EmpleadoDAO.buscar_por_id(id_modificar)
                
                if emp:
                    print(f"Empleado encontrado: {emp.nombre} ({emp.correo})")
                    emp.nombre = input("Nuevo Nombre (deja vacío para no cambiar): ") or emp.nombre
                    emp.correo = input("Nuevo Correo (deja vacío para no cambiar): ") or emp.correo
                    
                    EmpleadoDAO.actualizar(emp)
                    print("¡Empleado actualizado correctamente en MySQL Workbench!")
                else:
                    print(f"No se encontró ningún empleado con el ID {id_modificar}")
            except ValueError:
                print("Por favor, ingresa un número de ID válido.")

        elif opcion == "4":
            print("\n--- ELIMINAR EMPLEADO ---")
            try:
                id_eliminar = int(input("Ingresa el ID del empleado a eliminar: "))
                emp = EmpleadoDAO.buscar_por_id(id_eliminar)
                
                if emp:
                    confirmar = input(f"¿Seguro que deseas eliminar a {emp.nombre}? (s/n): ").lower()
                    if confirmar == 's':
                        EmpleadoDAO.eliminar(id_eliminar)
                        print("Empleado eliminado de la base de datos.")
                    else:
                        print("Operación cancelada.")
                else:
                    print(f"No se encontró ningún empleado con el ID {id_eliminar}")
            except ValueError:
                print("Por favor, ingresa un número de ID válido.")

        elif opcion == "5":
            print("\n¡Gracias por usar el sistema EcoTech! Saliendo...")
            sys.exit()
            
        else:
            print("Opción inválida. Por favor, selecciona un número del 1 al 5.")

if __name__ == "__main__":
    main()




