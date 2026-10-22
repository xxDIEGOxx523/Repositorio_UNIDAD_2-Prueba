from persistencia.conexion import abrir_conexion
from persistencia.interfaces_dao import IUsuarioDAO  # Asumiendo que existe o puedes implementarla


class UsuarioDAO(IUsuarioDAO):

    def insertar(self, usuario):
        conexion = abrir_conexion()
        cursor = None

        try:
            cursor = conexion.cursor()
            cursor.execute("""
                INSERT INTO usuario
                (username, password_hash, rol, activo, id_empleado)
                VALUES (%s, %s, %s, %s, %s)
            """, (
                usuario.username,
                usuario.password_hash,
                usuario.rol,
                usuario.activo,
                usuario.id_empleado,
            ))

            conexion.commit()
            usuario.id_usuario = cursor.lastrowid
            return usuario

        except Exception:
            conexion.rollback()
            raise

        finally:
            if cursor is not None:
                cursor.close()
            conexion.close()

    def buscar_por_nombre(self, username):
        conexion = abrir_conexion()
        cursor = None

        try:
            cursor = conexion.cursor()
            cursor.execute(
                "SELECT * FROM usuario WHERE username = %s",
                (username,),
            )
            fila = cursor.fetchone()

            return self._fila_a_dict(fila) if fila else None

        finally:
            if cursor is not None:
                cursor.close()
            conexion.close()

    def buscar_por_empleado(self, id_empleado):
        conexion = abrir_conexion()
        cursor = None

        try:
            cursor = conexion.cursor()
            cursor.execute(
                "SELECT * FROM usuario WHERE id_empleado = %s",
                (id_empleado,),
            )
            fila = cursor.fetchone()

            return self._fila_a_dict(fila) if fila else None

        finally:
            if cursor is not None:
                cursor.close()
            conexion.close()

    @staticmethod
    def _fila_a_dict(fila):
        return {
            "id_usuario": fila[0],
            "username": fila[1],
            "password_hash": fila[2],
            "rol": fila[3],
            "activo": fila[4],
            "fecha_creacion": fila[5],
            "id_empleado": fila[6],
        }