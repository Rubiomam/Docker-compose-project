from flask import Flask, request
import logging as log
import mysql.connector

log.basicConfig(level=log.INFO)

app = Flask(__name__)

# Configura la conexión a la base de datos MySQL
db_config = {
    'host': 'mysql',
    'user': 'root',
    'password': 'ccDec2023',
    'database': 'biblioteca'
}

@app.route('/')
def index():
    # Esta función se asocia a la ruta raíz "/"
    return "¡Bienvenido a la Biblioteca de Alejandría!"

@app.route('/formulario', methods=['GET', 'POST'])
def formulario():
    # Esta función se asocia a la ruta "/formulario"
    if request.method == 'GET':
        return '''
        <h1>Registro de Usuario</h1>
        <form action="/formulario" method="post">
            <label for="nombre">Nombre:</label>
            <input type="text" id="nombre" name="nombre"><br>
            <input type="submit" value="Enviar">
        </form>
        '''
    
    nombre = request.form['nombre']
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuarios (nombre) VALUES (%s);", (nombre,))
    conn.commit()
    conn.close()
    return f"Hola, {nombre}. ¡Bienvenido a la Biblioteca de Alejandría!"

@app.route('/libro', methods=['GET', 'POST'])
def libro():
    # Esta función se asocia a la ruta "/libro"
    if request.method == 'GET':
        return '''
        <h1>Registro de Libro</h1>
        <form action="/libro" method="post">
            <label for="titulo">Título:</label>
            <input type="text" id="titulo" name="titulo"><br>
            <label for="autor">Autor:</label>
            <input type="text" id="autor" name="autor"><br>
            <input type="submit" value="Enviar">
        </form>
        '''
    
    titulo = request.form['titulo']
    autor = request.form['autor']
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO libros (titulo, autor) VALUES (%s, %s);", (titulo, autor))
    conn.commit()
    conn.close()
    return f"Libro {titulo} registrado con éxito."

@app.route('/prestamo', methods=['GET', 'POST'])
def prestamo():
    # Esta función se asocia a la ruta "/prestamo"
    if request.method == 'GET':
        return '''
        <h1>Registro de Préstamo</h1>
        <form action="/prestamo" method="post">
            <label for="usuario_id">ID Usuario:</label>
            <input type="number" id="usuario_id" name="usuario_id"><br>
            <label for="libro_id">ID Libro:</label>
            <input type="number" id="libro_id" name="libro_id"><br>
            <label for="fecha_prestamo">Fecha Préstamo:</label>
            <input type="date" id="fecha_prestamo" name="fecha_prestamo"><br>
            <input type="submit" value="Enviar">
        </form>
        '''
    
    usuario_id = request.form['usuario_id']
    libro_id = request.form['libro_id']
    fecha_prestamo = request.form['fecha_prestamo']
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO prestamos (usuario_id, libro_id, fecha_prestamo) VALUES (%s, %s, %s);", 
                   (usuario_id, libro_id, fecha_prestamo))
    conn.commit()
    conn.close()
    return f"Préstamo registrado con éxito."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)