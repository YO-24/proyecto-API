import requests
from auxiliares.api_data import URL_POSTS, URL_COMMENTS

# --- 1. SOLICITUD GET (Obtener datos) ---
def obtener_posts_api():
    """Descarga la lista de posts desde la API."""
    try:
        response = requests.get(URL_POSTS)
        response.raise_for_status() # Lanza error si el código no es 200
        return response.json() # Retorna la lista de diccionarios
    except requests.exceptions.RequestException as e:
        print(f"Error al conectar con la API de Posts: {e}")
        return []

def obtener_comments_api():
    """Descarga la lista de comentarios desde la API."""
    try:
        response = requests.get(URL_COMMENTS)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error al conectar con la API de Comments: {e}")
        return []

# --- 2. SOLICITUD POST (Enviar datos) ---
def crear_post_api(data_post):
    """
    Simula el envío de un nuevo post.
    data_post: Diccionario con {title, body, userId}
    """
    try:
        response = requests.post(URL_POSTS, json=data_post)
        # La API debería responder 201 (Created)
        if response.status_code == 201:
            print(f"¡Éxito! API respondió: {response.status_code}")
            return response.json() # Retorna el objeto creado con su nuevo ID
        else:
            print(f"La API respondió con código inesperado: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error en solicitud POST: {e}")
        return None

# --- 3. SOLICITUD PUT (Actualizar datos) ---
def actualizar_post_api(id_post, data_actualizada):
    """
    Simula la actualización de un post existente.
    """
    url_con_id = f"{URL_POSTS}/{id_post}"
    try:
        response = requests.put(url_con_id, json=data_actualizada)
        if response.status_code == 200:
            print(f"¡Éxito! Post {id_post} actualizado. API respondió: 200")
            return response.json()
        else:
            print(f"Error al actualizar. Código: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error en solicitud PUT: {e}")
        return None

# --- 4. SOLICITUD DELETE (Eliminar datos) ---
def eliminar_post_api(id_post):
    """
    Simula la eliminación de un post.
    """
    url_con_id = f"{URL_POSTS}/{id_post}"
    try:
        response = requests.delete(url_con_id)
        if response.status_code == 200:
            print(f"¡Éxito! Post {id_post} eliminado. API respondió: 200")
            return True
        else:
            print(f"Error al eliminar. Código: {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"Error en solicitud DELETE: {e}")
        return False