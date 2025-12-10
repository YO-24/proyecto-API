class Usuario:
    def __init__(self, username, password, id=None):
        self.id = id
        self.username = username
        self.password = password

    def __str__(self):
        return f"Usuario: {self.username}"

class Post:
    def __init__(self, id, userId, title, body):
        self.id = id
        self.userId = userId # ID del usuario en la API externa
        self.title = title
        self.body = body

    def __str__(self):
        return f"POST [{self.id}]: {self.title}"

class Comment:
    def __init__(self, id, postId, name, email, body):
        self.id = id
        self.postId = postId
        self.name = name
        self.email = email
        self.body = body

    def __str__(self):
        return f"COMMENT [{self.id}] by {self.email}"