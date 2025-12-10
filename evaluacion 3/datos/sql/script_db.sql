-- TABLA 1: USUARIOS (Para el Login de tu sistema)
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL -- Aquí guardaremos la contraseña encriptada
);

-- TABLA 2: POSTS (Refleja los datos de JSONPlaceholder)
CREATE TABLE IF NOT EXISTS posts (
    id INTEGER PRIMARY KEY,         -- ID original que viene de la API
    userId INTEGER,                 -- ID del usuario de la API (no confundir con tu tabla local)
    title TEXT,
    body TEXT
);

-- TABLA 3: COMENTARIOS (Refleja los datos de JSONPlaceholder)
CREATE TABLE IF NOT EXISTS comments (
    id INTEGER PRIMARY KEY,         -- ID original que viene de la API
    postId INTEGER,                 -- Clave foránea que conecta con el Post
    name VARCHAR(100),
    email VARCHAR(100),
    body TEXT,
    FOREIGN KEY(postId) REFERENCES posts(id)
);