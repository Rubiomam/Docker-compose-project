-- Crea la tabla usuarios
CREATE TABLE IF NOT EXISTS usuarios (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50)
);

-- Crea la tabla libros
CREATE TABLE IF NOT EXISTS libros (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(100),
    autor VARCHAR(50)
);

-- Crea la tabla prestamos
CREATE TABLE IF NOT EXISTS prestamos (
    id_prestamo SERIAL PRIMARY KEY,
    usuario_id INT,
    libro_id INT,
    fecha_prestamo DATE,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
    FOREIGN KEY (libro_id) REFERENCES libros(id)
);