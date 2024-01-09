-- Inserta usuarios
INSERT INTO usuarios (nombre) VALUES 
('Juan'), ('Marta'), ('Pedro'), ('Laura'),
('Ana'), ('Carlos'), ('Diana'), ('Roberto'),
('Elena'), ('Sergio');

-- Inserta libros
INSERT INTO libros (titulo, autor) VALUES 
('1984', 'George Orwell'), 
('A Breath of Snow and Ashes', 'Diana Gabaldon'),
('A orillas del río Piedra me senté y lloré', 'Paulo Coelho'),
('Adulterio', 'Paulo Coelho'),
('Al este del Edén', 'John Steinbeck'),
('Ángeles y demonios', 'Dan Brown'),
('Anna Karenina', 'Leo Tolstoy'),
('Brave New World', 'Aldous Huxley'),
('Brida', 'Paulo Coelho'),
('Catch-22', 'Joseph Heller');

-- Inserta préstamos
INSERT INTO prestamos (usuario_id, libro_id, fecha_prestamo) VALUES 
(1, 5, '2023-12-10'), 
(2, 3, '2023-12-12'),
(3, 2, '2023-12-15'),
(4, 1, '2023-12-15'),
(5, 4, '2023-12-22'),
(6, 6, '2024-01-03'),
(7, 7, '2024-01-04'),
(8, 8, '2024-01-04'),
(9, 9, '2024-01-04'),
(10, 10, '2024-01-05');