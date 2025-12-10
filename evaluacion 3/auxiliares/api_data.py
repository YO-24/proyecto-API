# URL Base de la API
BASE_URL = "https://jsonplaceholder.typicode.com"

# Endpoints específicos para tu grupo de datos
URL_POSTS = f"{BASE_URL}/posts"
URL_COMMENTS = f"{BASE_URL}/comments"
URL_USERS_API = f"{BASE_URL}/users" # Útil si necesitas validar userIds

# Códigos de estado HTTP esperados
HTTP_OK = 200
HTTP_CREATED = 201