import sys
from dominio.registrotiempo import RegistroTiempo

class TerminalInterface:
    def __init__(self, registro_dao, empleado_dao, proyecto_dao, departamento_dao):
        self.registro_dao = registro_dao
        self.empleado_dao = empleado_dao
        self.proyecto_dao = proyecto_dao
        self.departamento_dao = departamento_dao

    def mostrar_menu(self):
        print("\n" + "="*40)
        print("      SISTEMA DE GESTIÓN GUBERNENTAL / ECOTECH")
        print("="*40)
        print(" 1. Registrar tiempo de empleado")
        print(" 2. Mostrar todos los registros de tiempo")
        print(" 3. Ver lista de Empleados")
        print(" 4. Ver lista de Proyectos")
        print(" 5. Salir del programa")
        print("="*40)

    def iniciar(self):
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción (1-5): ").strip()
            if opcion == "1":
                self._solicitar_registro()
            elif opcion == "2":
                self._mostrar_listado_tiempos()
            elif opcion == "3":
                self._listar_entidad(self.empleado_dao, "EMPLEADOS")
            elif opcion == "4":
                self._listar_entidad(self.proyecto_dao, "PROYECTOS")
            elif opcion == "5":
                print("\nCerrando sistema de gestión. ¡Hasta luego!")
                sys.exit()
            else:
                print("\n❌ Opción no válida. Intente nuevamente.")

    def _listar_entidad(self, dao, nombre_entidad: str):
        print(f"\n--- LISTA DE {nombre_entidad} ---")
        items = dao.obtener_todos()
        if not items:
            print("No hay registros disponibles.")
            return
        for item in items:
            print(f"ID: {item['id']} | Nombre: {item['nombre']}")

    def _solicitar_registro(self):
        print("\n--- NUEVO REGISTRO DE TIEMPO ---")
        try:
            id_empleado = int(input("ID del Empleado: "))
            id_proyecto = int(input("ID del Proyecto: "))
            horas = float(input("Cantidad de horas trabajadas: "))
            
            if horas <= 0 or horas > 24:
                print("\n❌ Error: Las horas diarias deben estar entre 1 y 24.")
                return

            # Vinculación con tu clase de dominio existente
            nuevo_registro = RegistroTiempo(id_empleado=id_empleado, id_proyecto=id_proyecto, horas=horas)
            
            if self.registro_dao.insertar(nuevo_registro):
                print("\n✅ ¡Tiempo guardado exitosamente!")
            else:
                print("\n❌ No se pudo completar la persistencia.")
        except ValueError:
            print("\n❌ Error: Ingrese valores numéricos válidos.")

    def _mostrar_listado_tiempos(self):
        print("\n--- HISTORIAL DE REGISTROS DE TIEMPO ---")
        registros = self.registro_dao.obtener_todos_con_detalles()
        if not registros:
            print("No se encontraron registros de tiempo.")
            return
        for reg in registros:
            print(f"[{reg['fecha']}] Empleado: {reg['empleado']:15} | Proyecto: {reg['proyecto']:12} | Horas: {reg['horas']:.1f}")
