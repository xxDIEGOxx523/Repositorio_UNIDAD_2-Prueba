from dominio.proyecto import Proyecto
from persistencia.conexion import abrir_conexion

class ProyectoDAO:

    def guardar(self, proyecto):
        con = abrir_conexion()
        cur = con.cursor()
        try:
            cur.execute("INSERT INTO proyecto (nombre) VALUES (?)", (proyecto.nombre,))
            con.commit()
            proyecto.id = cur.lastrowid
            return proyecto
        except:
            con.rollback()
            raise
        finally:
            con.close()

    def buscar(self, id_proyecto):
        con = abrir_conexion()
        try:
            cur = con.cursor()
            cur.execute("SELECT id, nombre FROM proyecto WHERE id = ?", (id_proyecto,))
            fila = cur.fetchone()
            if fila is None:
                return None
            return Proyecto(id=fila[0], nombre=fila[1])
        finally:
            con.close()

    def listar(self):
        con = abrir_conexion()
        try:
            cur = con.cursor()
            cur.execute("SELECT id, nombre FROM proyecto")
            filas = cur.fetchall()
            lista = []
            for fila in filas:
                lista.append(Proyecto(id=fila[0], nombre=fila[1]))
            return lista
        finally:
            con.close()

    def cambiar(self, proyecto):
        con = abrir_conexion()
        try:
            cur = con.cursor()
            cur.execute(
                "UPDATE proyecto SET nombre = ? WHERE id = ?",
                (proyecto.nombre, proyecto.id)
            )
            con.commit()
            return cur.rowcount > 0
        except:
            con.rollback()
            raise
        finally:
            con.close()

    def borrar(self, id_proyecto):
        con = abrir_conexion()
        try:
            cur = con.cursor()
            cur.execute("DELETE FROM proyecto WHERE id = ?", (id_proyecto,))
            con.commit()
            return cur.rowcount > 0
        except:
            con.rollback()
            raise
        finally:
            con.close()


