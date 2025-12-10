import hashlib
from modelos.Modelos import Usuario
from datos.insertar_datos import insertar_usuario_db
from datos.obtener_datos import obtener_usuario_por_username

def encriptar_contrasena(password):
    "Convierte la contraseña en un hash SHA-256."
    hash_obj = hashlib.sha256(password.encode())
    return hash_obj.hexdigest()

def registrar_usuario(username, password):
    """
    Lógica de negocio para registrar:
    1. Verifica si ya existe.
    2. Encripta la contraseña.
    3. Manda a guardar a la capa de datos.
    """
    if obtener_usuario_por_username(username):
        print("El usuario ya existe. Intente con otro nombre.")
        return False
    
    # Encriptamos antes de crear el objeto
    pass_encriptada = encriptar_contrasena(password)
    nuevo_usuario = Usuario(username, pass_encriptada)
    
    return insertar_usuario_db(nuevo_usuario)

def validar_login(username, password):
    """
    Lógica de negocio para login:
    1. Busca al usuario en la BD.
    2. Encripta la contraseña ingresada.
    3. Compara los hashes.
    """
    usuario_db = obtener_usuario_por_username(username)
    
    if usuario_db:
        pass_input_hash = encriptar_contrasena(password)
        if pass_input_hash == usuario_db.password:
            return True # Login correcto
    
    return False # Usuario no existe o contraseña incorrecta