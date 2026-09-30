from persistencia.conexion import abrir_conexion, obtener_motor, marcador_sql
from dominio.empleado import Empleado


class EmpleadoDAO:

    @staticmethod
    def insertar(empleado):
        conexion = abrir_conexion()
        cursor = conexion.cursor()
        marcador = "?" if obtener_motor() == "sqlite" else "%s"
        sql = f"""
            INSERT INTO empleado (nombre, correo)
            VALUES ({marcador}, {marcador})
        """
        cursor.execute(sql, (empleado.nombre, empleado.correo))
        empleado.id = cursor.lastrowid
        conexion.commit()
        conexion.close()
        return empleado
    
    @staticmethod
    def buscar_por_id(id_empleado):
        conexion = abrir_conexion()
        cursor = conexion.cursor()
        marca = marcador_sql()
        sql = f"""
            SELECT id, nombre, correo
            FROM empleado WHERE id = {marca}
        """
        cursor.execute(sql, (id_empleado,))
        fila = cursor.fetchone()
        conexion.close()
        if fila is None:
            return None
        return EmpleadoDAO._fila_a_empleado(fila)

    @staticmethod
    def listar():
        conexion = abrir_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT id, nombre, correo FROM empleado")
        filas = cursor.fetchall()
        conexion.close()
        empleados = []
        for fila in filas:
            empleados.append(Empleado(id=fila[0], nombre=fila[1], correo=fila[2]))
        return empleados

    @staticmethod
    def actualizar(empleado):
        """Actualiza el nombre y correo de un empleado existente por su ID"""
        conexion = abrir_conexion()
        cursor = conexion.cursor()
        marca = marcador_sql()
        sql = f"""
            UPDATE empleado 
            SET nombre = {marca}, correo = {marca} 
            WHERE id = {marca}
        """
        # Pasamos los nuevos datos y el ID al final para la condición WHERE
        cursor.execute(sql, (empleado.nombre, empleado.correo, empleado.id))
        conexion.commit()
        conexion.close()
        return empleado

    @staticmethod
    def eliminar(id_empleado):
        """Elimina un empleado de la base de datos usando su ID"""
        conexion = abrir_conexion()
        cursor = conexion.cursor()
        marca = marcador_sql()
        sql = f"DELETE FROM empleado WHERE id = {marca}"
        cursor.execute(sql, (id_empleado,))
        conexion.commit()
        conexion.close()
        return True

    @staticmethod
    def _fila_a_empleado(fila):
        return Empleado(id=fila[0], nombre=fila[1], correo=fila[2])




