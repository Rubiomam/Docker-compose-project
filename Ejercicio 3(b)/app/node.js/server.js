const express = require('express');
const mysql = require('mysql2');
const bodyParser = require('body-parser');
const app = express();
const port = 5000;

app.set('view engine', 'ejs');

// Static files
app.use('/static', express.static('public'));

// Body parser middleware
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

// MySQL database connection
const db = mysql.createPool({
  host: 'mysql',
  user: 'root',
  password: 'ccDec2023',
  database: 'biblioteca'
});

// Routes
app.get('/', (req, res) => {
  res.render('index');
});

app.get('/formulario', (req, res) => {
  res.render('formulario');
});

app.post('/formulario', (req, res) => {
  const { nombre } = req.body;
  db.query("INSERT INTO usuarios (nombre) VALUES (?)", [nombre], (err, results) => {
    if (err) throw err;
    res.send(`Hola, ${nombre}. ¡Bienvenido a la Biblioteca de Alejandría!`);
  });
});

app.get('/libro', (req, res) => {
  res.render('libro');
});

app.post('/libro', (req, res) => {
  const { titulo, autor } = req.body;
  db.query("INSERT INTO libros (titulo, autor) VALUES (?, ?)", [titulo, autor], (err, results) => {
    if (err) throw err;
    res.send(`Libro ${titulo} registrado con éxito.`);
  });
});

app.get('/prestamo', (req, res) => {
  res.render('prestamo');
});

app.post('/prestamo', (req, res) => {
  const { usuario_id, libro_id, fecha_prestamo } = req.body;
  db.query("INSERT INTO prestamos (usuario_id, libro_id, fecha_prestamo) VALUES (?, ?, ?)", [usuario_id, libro_id, fecha_prestamo], (err, results) => {
    if (err) throw err;
    res.send("Préstamo registrado con éxito.");
  });
});

app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});