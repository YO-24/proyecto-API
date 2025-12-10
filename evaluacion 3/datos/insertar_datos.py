import sqlite3
from datos.conexion import crear_conexion

def insertar_usuario_db(usuario):
    """Recibe un objeto Usuario y lo guarda en la BD."""
    conn = crear_conexion()
    if conn:
        try:
            cursor = conn.cursor()
            sql = "INSERT INTO usuarios (username, password) VALUES (?, ?)"
            cursor.execute(sql, (usuario.username, usuario.password))
            conn.commit()
            print("Usuario registrado exitosamente en la BD.")
            return True
        except sqlite3.IntegrityError:
            print("Error: El nombre de usuario ya existe.")
            return False
        except Exception as e:
            print(f"Error al insertar usuario: {e}")
            return False
        finally:
            conn.close()
    return False