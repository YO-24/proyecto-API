import os
import sys

# Importamos nuestras funcionalidades
from negocio.negocio_usuarios import registrar_usuario, validar_login
from negocio.negocio_posts import sincronizar_posts, listar_posts_locales, guardar_post_nuevo_local, actualizar_post_local, eliminar_post_local
from negocio.negocio_comments import listar_comentarios_por_post
from servicios.api_service import crear_post_api, actualizar_post_api, eliminar_post_api

def limpiar_pantalla():
    "Limpia la consola según el sistema operativo."
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_inicio():
    "Menú inicial: Login o Registro [cite: 83-86]"
    while True:
        print("\n--- BIENVENIDO AL SISTEMA ---")
        print("1. Iniciar Sesión")
        print("2. Registrar Nuevo Usuario")
        print("3. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            user = input("Usuario: ")
            pwd = input("Contraseña: ")
            if validar_login(user, pwd):
                print(f"\n¡Bienvenido, {user}!")
                menu_principal(user) # Vamos al menú de la App
            else:
                print("\nError: Usuario o contraseña incorrectos.")
        
        elif opcion == '2':
            print("\n--- REGISTRO DE USUARIO ---")
            user = input("Nuevo nombre de usuario: ")
            pwd = input("Nueva contraseña: ")
            if registrar_usuario(user, pwd):
                print("¡Usuario creado! Ahora puede iniciar sesión.")
            else:
                print("No se pudo registrar el usuario.")
        
        elif opcion == '3':
            print("Saliendo del sistema...")
            sys.exit()
        else:
            print("Opción no válida.")

def menu_principal(usuario_actual):
    "Menú principal una vez logueado [cite: 87-95]"
    while True:
        print(f"\n--- MENÚ PRINCIPAL (Usuario: {usuario_actual}) ---")
        print("1.Sincronizar y Ver Posts")
        print("2.Crear un nuevo Post")
        print("3.Actualizar un Post")
        print("4.Eliminar un Post")
        print("5.Ver Comentarios")
        print("6.Cerrar Sesión")


        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            # PASO 1: Ver qué tenemos guardado en el PC
            posts = listar_posts_locales()
            
            # PASO 2: Solo vamos a internet si NO tenemos nada guardado
            if not posts: 
                print("\n[AVISO] Base de datos vacía. Descargando desde Internet...")
                sincronizar_posts()
                posts = listar_posts_locales() # Leemos de nuevo
            else:
                print(f"\n[AVISO] Cargando {len(posts)} posts desde tu BASE DE DATOS LOCAL (Sin internet)...")

            # PASO 3: Mostrar los datos
            print(f"--- Mostrando posts locales ---")
            
            if len(posts) > 5:
                print("... (posts antiguos ocultos) ...")
                # Mostramos los últimos 5 para que veas tus cambios
                for p in posts[-5:]: 
                    print(p)
            else:
                for p in posts:
                    print(p)
            

        elif opcion == '2':
            # POST: Enviar datos a la API
            print("\n--- CREAR POST ---")
            titulo = input("Ingrese Título: ")
            cuerpo = input("Ingrese Cuerpo: ")
            
            # Datos para enviar
            data = {"title": titulo, "body": cuerpo, "userId": 1}
            
            # Llamamos a la API y capturamos la respuesta
            nuevo_post = crear_post_api(data)
            
            # Si la API respondió bien (nos devolvió el objeto creado)
            if nuevo_post:
                # LO GUARDAMOS EN NUESTRA BD LOCAL
               guardar_post_nuevo_local(nuevo_post['id'], 1, titulo, cuerpo)
        
        elif opcion == '3':
            # PUT: Actualizar datos (Ahora pedimos cuerpo también)
            print("\n--- ACTUALIZAR POST ---")
            id_post = input("ID del Post a editar: ")
            nuevo_titulo = input("Nuevo Título: ")
            nuevo_cuerpo = input("Nuevo Cuerpo: ")
            
            data = {"title": nuevo_titulo, "body": nuevo_cuerpo, "userId": 1}
            
            # 1. Mandamos a la API (Simulacro)
            respuesta = actualizar_post_api(id_post, data)
            
            # 2. Si la API dice OK, actualizamos nuestra BD real
            if respuesta:
                actualizar_post_local(id_post, nuevo_titulo, nuevo_cuerpo)

        elif opcion == '4':
            # DELETE: Borrar datos
            print("\n--- ELIMINAR POST ---")
            id_post = input("ID del Post a eliminar: ")
            eliminar_post_api(id_post)
            eliminar_post_local(id_post)

        elif opcion == '5':
            # Lógica para mostrar comentarios
            print("\n--- VER COMENTARIOS ---")
            id_post = input("ID del Post: ")
            comentarios = listar_comentarios_por_post(id_post)
            print(f"--- Comentarios del Post {id_post} ---")
            if not comentarios:
                print("No se encontraron comentarios para este ID.")
            else:
                for c in comentarios:
                    print(f"- {c.email}: {c.body[:30]}...") # Muestra email y parte del texto

if __name__ == "__main__":
    # Aseguramos que la BD exista antes de arrancar
    from datos.conexion import inicializar_db
    inicializar_db()
    
    # Arrancar el programa
    limpiar_pantalla()
    menu_inicio()