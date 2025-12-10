from servicios.api_service import obtener_comments_api
from modelos.Modelos import Comment

def listar_comentarios_por_post(post_id):
    """
    Filtra los comentarios para mostrar solo los de un Post específico.
    Simula la relación 1 a N (Un Post tiene muchos Comentarios).
    """
    todos_los_comments = obtener_comments_api()
    comentarios_filtrados = []
    
    # Filtramos manualmente los que coincidan con el ID del Post
    for c in todos_los_comments:
        if c['postId'] == int(post_id):
            nuevo_comentario = Comment(c['id'], c['postId'], c['name'], c['email'], c['body'])
            comentarios_filtrados.append(nuevo_comentario)
            
    return comentarios_filtrados