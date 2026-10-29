from persistencia.conexion import abrir_conexion
from dominio.usuario import Usuario


class UsuarioDAO:

    def insertar(self, usuario):
        conexion = abrir_conexion()
        cursor = None
        try:
            cursor = conexion.cursor()
            cursor.execute("""
                INSERT INTO usuario (username, password_hash, id_empleado)
                VALUES (%s, %s, %s)
            """, (usuario.nombre_usuario, usuario.password_hash,
                  usuario.empleado_id))
            conexion.commit()
            usuario.id = cursor.lastrowid
            return usuario.id
        except Exception:
            conexion.rollback()
            raise
        finally:
            if cursor is not None:
                cursor.close()
            conexion.close()

    def buscar_por_nombre(self, nombre_usuario):
        return self._buscar("username", nombre_usuario)

    def buscar_por_empleado(self, id_empleado):
        return self._buscar("id_empleado", id_empleado)

    def _buscar(self, columna, valor):
        conexion = abrir_conexion()
        cursor = None
        try:
            cursor = conexion.cursor()

            cursor.execute(
                f"SELECT id_usuario, username, password_hash, id_empleado "
                f"FROM usuario WHERE {columna} = %s",
                (valor,),
            )
            fila = cursor.fetchone()
            if fila is None or fila[3] is None:
                return None
            return Usuario(nombre_usuario=fila[1], password_hash=fila[2],
                           empleado_id=fila[3], id=fila[0])
        finally:
            if cursor is not None:
                cursor.close()
            conexion.close()