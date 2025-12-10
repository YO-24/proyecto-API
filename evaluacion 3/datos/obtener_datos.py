import sqlite3
from datos.conexion import crear_conexion
from modelos.Modelos import Usuario

def obtener_usuario_por_username(username):
    """Busca un usuario por su nombre y retorna un objeto Usuario."""
    conn = crear_conexion()
    usuario_encontrado = None
    if conn:
        try:
            cursor = conn.cursor()
            sql = "SELECT id, username, password FROM usuarios WHERE username = ?"
            cursor.execute(sql, (username,))
            fila = cursor.fetchone()
            
            if fila:
                # Creamos el objeto Usuario con los datos de la BD
                # fila[0]=id, fila[1]=username, fila[2]=password (encriptada)
                usuario_encontrado = Usuario(fila[1], fila[2], fila[0])
                
        except Exception as e:
            print(f"Error al obtener usuario: {e}")
        finally:
            conn.close()
            
    return usuario_encontrado