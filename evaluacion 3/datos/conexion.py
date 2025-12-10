import sqlite3
import os

# Definimos la ruta donde se guardará la base de datos
DB_NAME = 'sistema_gestion.db'

def crear_conexion():
    """Crea y retorna una conexión a la base de datos SQLite."""
    try:
        # Esto crea el archivo si no existe
        conn = sqlite3.connect(DB_NAME)
        return conn
    except sqlite3.Error as e:
        print(f"Error al conectar con la BD: {e}")
        return None

def inicializar_db():
    """Lee el script SQL y crea las tablas si no existen."""
    conn = crear_conexion()
    if conn:
        try:
            cursor = conn.cursor()
            
            # Buscamos la ruta del archivo SQL
            # Asumimos que el script está en Datos/sql/script_db.sql
            ruta_actual = os.path.dirname(os.path.abspath(__file__))
            ruta_script = os.path.join(ruta_actual, 'sql', 'script_db.sql')
            
            with open(ruta_script, 'r') as archivo_sql:
                script = archivo_sql.read()
                cursor.executescript(script)
                
            print("Base de datos y tablas inicializadas correctamente.")
        except Exception as e:
            print(f"Error al inicializar la BD: {e}")
        finally:
            conn.close()

# Esto permite probar este archivo directamente ejecutándolo
if __name__ == "__main__":
    inicializar_db()