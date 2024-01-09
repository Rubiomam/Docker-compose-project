from flask import Flask, request, render_template
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
    return render_template('index.html')

@app.route('/formulario', methods=['GET', 'POST'])
def formulario():
    # Esta función se asocia a la ruta "/formulario"
    # Si el método es GET, muestra el formulario
    if request.method == 'GET':
        return render_template('formulario.html')
    
    # Si el método es POST, procesa los datos del template
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
        return render_template('libro.html')
    
    # Si el método es POST, procesa los datos del template
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
        return render_template('prestamo.html')
    
    # Si el método es POST, procesa los datos del template
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