from servicios.api_service import obtener_posts_api
from modelos.Modelos import Post
from datos.conexion import crear_conexion
import sqlite3

def sincronizar_posts():
    """
    1. Trae los posts desde la API.
    2. Los guarda en la base de datos local.
    """
    print("Descargando posts desde la API...")
    datos_api = obtener_posts_api() # Esto llama a tu servicio
    
    if not datos_api:
        print("No se encontraron datos o hubo un error en la API.")
        return

    conn = crear_conexion()
    if conn:
        try:
            cursor = conn.cursor()
            contador = 0
            
            for item in datos_api:
                # La API devuelve diccionarios, los convertimos a objetos u guardamos
                # item es un diccionario: {'userId': 1, 'id': 1, 'title': '...', 'body': '...'}
                
                # Usamos INSERT OR IGNORE para no duplicar si ya existen
                sql = """
                INSERT OR IGNORE INTO posts (id, userId, title, body) 
                VALUES (?, ?, ?, ?)
                """
                cursor.execute(sql, (item['id'], item['userId'], item['title'], item['body']))
                contador += 1
            
            conn.commit()
            print(f"Sincronización completada. {contador} posts procesados/guardados.")
            
        except sqlite3.Error as e:
            print(f"Error guardando en BD: {e}")
        finally:
            conn.close()

def listar_posts_locales():
    """Lee los posts desde tu Base de Datos local para mostrarlos."""
    posts = []
    conn = crear_conexion()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id, userId, title, body FROM posts")
            filas = cursor.fetchall()
            
            for f in filas:
                # f[0]=id, f[1]=userId, f[2]=title, f[3]=body
                p = Post(f[0], f[1], f[2], f[3])
                posts.append(p)
        except Exception as e:
            print(f"Error leyendo BD: {e}")
        finally:
            conn.close()
    return posts

def guardar_post_nuevo_local(id_post, user_id, title, body):
    """Guarda manualmente un post nuevo en la BD local."""
    conn = crear_conexion()
    if conn:
        try:
            cursor = conn.cursor()
            sql = "INSERT INTO posts (id, userId, title, body) VALUES (?, ?, ?, ?)"
            cursor.execute(sql, (id_post, user_id, title, body))
            conn.commit()
            print(" -> Post guardado exitosamente en tu Base de Datos local.")
        except sqlite3.Error as e:
            print(f"Error al guardar localmente: {e}")
        finally:
            conn.close()

def actualizar_post_local(id_post, nuevo_titulo, nuevo_cuerpo):
    """Actualiza un post en la base de datos local."""
    conn = crear_conexion()
    if conn:
        try:
            cursor = conn.cursor()
            # Actualizamos Título y Cuerpo donde coincida el ID
            sql = "UPDATE posts SET title = ?, body = ? WHERE id = ?"
            cursor.execute(sql, (nuevo_titulo, nuevo_cuerpo, id_post))
            conn.commit()
            print(" -> [BD LOCAL] Post actualizado correctamente.")
        except sqlite3.Error as e:
            print(f"Error al actualizar local: {e}")
        finally:
            conn.close()

def eliminar_post_local(id_post):
    """Elimina el post y cualquier rastro de él (comentarios asociados)."""
    conn = crear_conexion()
    if conn:
        try:
            cursor = conn.cursor()
            
            # 1. Primero borramos los comentarios asociados a este post (Limpieza)
            sql_comments = "DELETE FROM comments WHERE postId = ?"
            cursor.execute(sql_comments, (id_post,))
            
            # 2. Ahora sí borramos el post
            sql_post = "DELETE FROM posts WHERE id = ?"
            cursor.execute(sql_post, (id_post,))
            
            if cursor.rowcount > 0:
                conn.commit()
                print(f" -> [BD LOCAL] Post {id_post} y sus datos eliminados correctamente.")
                return True
            else:
                print(" -> No se encontró el post para eliminar.")
                return False
                
        except sqlite3.Error as e:
            print(f"Error al eliminar local: {e}")
            return False
        finally:
            conn.close()