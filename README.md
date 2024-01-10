# Docker-compose-project
Definición

La containerización se define como una metodología de implementación de software que implica el empaquetado del código y sus dependencias en unidades estandarizadas conocidas como contenedores. Estos contenedores permiten que las aplicaciones se ejecuten de manera eficiente y coherente en diversos entornos informáticos. A diferencia de la virtualización tradicional, que requiere máquinas virtuales (VM) con sistemas operativos completos, la containerización opera a nivel del sistema operativo (SO), compartiendo recursos del SO anfitrión y evitando la sobrecarga de iniciar una VM completa para cada aplicación.

Ventajas y Aplicaciones

La containerización ofrece múltiples beneficios, entre los que destacan una implementación más rápida, reducción de gastos generales, y una migración simplificada. Esta metodología es fundamental para el desarrollo de aplicaciones nativas en la nube y para la arquitectura de microservicios, donde servicios pequeños y autónomos se conectan para formar aplicaciones más complejas. Los contenedores facilitan el desarrollo, la implementación y el ajuste independiente de estos microservicios, proporcionando un entorno óptimo para un desarrollo de software ágil y libre de errores. Además, la flexibilidad de los contenedores para moverse entre diferentes entornos en la nube y su capacidad para escalar sin necesidad de reescribir aplicaciones o realizar cambios significativos de configuración, los convierte en una herramienta indispensable en la actualidad.

Objetivo del proyecto

El objetivo de la práctica es la familiarización del estudiante con conceptos de containerización, y programación asociada a los contenedores. Para ello, el alumno podrá elegir entre varias tareas de las señaladas en el documento identificado como "Práctica Evaluada: Docker" que fue entregado en clase; y completar, de manera independiente, aquellas que sean de su interés. El alumno podrá partir de la infraestructura elaborada en clase, especificada en los documentos identificados como "Tutorial 3 - Dockerfile - Creación de imágenes de Docker" y "Práctica Docker Compose".

Para la elaboración del presente proyecto se eligieron las siguientes tareas:
1.- Utilización de Git y GitHub para el control de versiones. 
2.- Elaboración de un esquema de datos más complejo en MySQL que el revisado en el documento "Práctica Docker Compose", que incluya más tablas, más datos por tabla y relaciones entre ellas. También se añade la modificación de los scripts de inserción para que estos incluyan más datos en la base de datos. La inserción se podrá llevar a cabo desde la terminal o desde la aplicación web, con confirmación de culminación de la tarea respectiva en la misma aplicación.
3.- Modificación de la página web para que también incluya hojas de estilo CSS, código Javascript simple y algún contenido dinámico en Javascript. Además, se añade la modificación del servidor de Flask en Python para que pueda servir estas hojas de estilo CSS y Javascript. Esto cubriría las tareas planteadas en las secciones 3 y 3(a).
4.- A partir de la construcción anterior, utilización de un servidor Node.js con la imagen apropiada de Docker y modificación de todos los componentes necesarios, de manera que la base de datos siga funcionando de la misma manera. Esto cubriría las tareas planteadas en la sección 3(b).
5.- Modificación del lenguaje de programación del cliente para que el envío de las peticiones sea más eficiente. Utilización del lenguaje de programación compilado Golang. Elaboración de un sistema ‘multi-stage build’, de manera que la imagen de cliente sea mínima en su tamaño. Utilización de imágenes preexistentes como base. Esto cubriría las tareas planteadas en las secciones 4, 4(a) y 4(b).
6.- Modificación de la imagen de la base de datos y utilización de PostgreSQL. Modificación de todos los componentes necesarios, de manera que la base de datos siga funcionando de la misma manera.
7.- Elaboración de la memoria del proyecto, en la cual se detallará cada uno de las tareas elegidas, su realización, y los cambios requeridos, según las necesidades en la infraestructura de Docker, Docker Compose y Dockerfile.

Descripción del caso

En todos los ejercicios se creará una base de datos para una biblioteca ficticia a la cual hemos denominado ‘Alejandría’, con tablas para almacenar información sobre usuarios (nombre), libros (título y autor) y préstamos de libros (usuario id, libro id y fecha préstamo). La estructura de la base de datos facilita la gestión de estas entidades y sus relaciones. En todos los casos, las tablas se han inicializado con la carga automática de 10 registros por tipo de dato. Una vez se ejecute la instrucción ‘docker compose up’ en cada ejercicio, se podrá interactuar con la base de datos desde el terminal de comandos o desde la página web de la aplicación, En este último caso, solo se podrá efectuar el ingreso de nuevos registros a las tablas antes mencionadas, recibiendo confirmación de la transacción en la misma página web. Desde la terminal de comandos se podrán efectuar todas las transacciones posibles que permita la base de datos utilizada. En todos los casos se ha creado un volumen para persistir los datos de la base de datos fuera del ciclo de vida del contenedor.

Es importante resaltar que el alcance de este proyecto no abarca la optimización de código ni la consideración de todos los aspectos de seguridad que uno de mayor envergadura, en la vida real, demandaría. Solo se pretende poner en práctica los conceptos aprendidos en relación con los temas relacionados con Docker, Docker Compose y Dockerfile, a través de la ejecución de los ejercicios seleccionados.

Para poder completar esta actividad, además del material recibido en clase, utilizamos la información que libremente se encuentra disponible en las siguientes fuentes: github.com, hub.docker.com, docker.com, chat,openai,com (ChatGPT) y Google Chrome.


Documentación

Con la finalidad de evitar la redundancia y una extensión excesiva de la presente memoria, solo se brindará detalle del código utilizado la primera vez que este aparezca. Cuando no existan cambios de un archivo en particular entre los diferentes ejercicios, solo se hará mención a su existencia y se resaltará el hecho de que no haya variado.

1.- Utilización de Git y GitHub para el control de versiones. El código correspondiente al proyecto podrá encontrarse en GitHub en el siguiente enlace: GitHub - Rubiomam/Docker-compose-project: Docker compose project. De igual manera, se ha generado un archivo ‘zip’ que también forma parte del paquete de entrega.

2. Ejercicio 2

Estructura de directorios

 

Código asociado a esa estructura

docker-compose.yml

El archivo `docker-compose.yml` configura un entorno de aplicación con tres contenedores interconectados (base de datos, servidor y cliente), cada uno con su propia imagen Docker y configuraciones específicas de red. También define redes para la comunicación entre contenedores y un volumen para la persistencia de datos. 

1. Versión:
`version: '3'`: Define la versión del archivo Docker Compose.

2. Servicios:
	`db`: Configura el contenedor para la base de datos MySQL
•	‘container_name: mysql`: El nombre del contenedor será `mysql
•	`build`: Instrucciones para construir la imagen del contenedor a partir de un `Dockerfile` ubicado en el directorio `./db/`
•	`volumes`: Monta un volumen llamado `mysql-data` en `/var/lib/mysql` dentro del contenedor para persistir los datos de la base de datos
•	 `networks`: Asigna el contenedor a la red `myapp-network` con una dirección IP estática

	`server`: Configura el servidor de aplicaciones, en este caso es un servidor Flask
•	`container_name: servidor`: El nombre del contenedor será `servidor`
•	`build`: Construye la imagen del contenedor desde el directorio `./server/`
•	`ports`: Mapea el puerto 8000 del host al puerto 5000 del contenedor
•	`depends_on`: Indica que este servicio depende del servicio `db`
•	`restart`: Política de reinicio del contenedor
•	`networks`: Conecta el contenedor a dos redes, con direcciones IP específicas

	`client`: Configura el cliente
•	`build`: Construye la imagen del contenedor a partir de un `Dockerfile` ubicado en el directorio `./client/`
•	`deploy`: Especifica la configuración de despliegue, con 6 réplicas del contenedor
•	`networks`: Conecta el contenedor a la red `myapp-external`
•	`depends_on`: Indica que este servicio depende del servicio `server`

3. Redes:
Define dos redes (`myapp-external` y `myapp-network`) con controladores de puente y configuraciones IPAM para manejar las direcciones IP y subredes

4. Volúmenes:
`mysql-data: {}`: Crea un volumen llamado `mysql-data`. Esto se usa para persistir los datos de la base de datos fuera del ciclo de vida del contenedor

client.py

Este script en Python está diseñado para actuar como un cliente que se comunica con un servidor, identificado como `servidor` en el puerto `5000`. Utiliza la librería `requests` para enviar solicitudes HTTP y `logging` para el registro de eventos. Esto sirve para probar la conectividad y la respuesta de un servidor web.

1. Importaciones:
•	`requests`: Una biblioteca en Python utilizada para hacer solicitudes HTTP
•	`logging`: Módulo estándar de Python para registrar eventos, errores y otros mensajes informativos

2. Configuración de Logging:
`log.basicConfig(level=log.INFO)`: Esta línea configura el nivel de registro en `INFO`, lo que significa que solo los mensajes con nivel `INFO` o superior (como `WARNING`, `ERROR`, `CRITICAL`) se mostrarán

3. `server_url = 'http://servidor:5000'`: Aquí se define la URL del servidor al que se enviarán las solicitudes

4. Función `send_request`: Esta función es el núcleo del script. Cuando se llama, envía una solicitud GET al servidor.
•	`log.info("Enviando solicitud de prueba al servidor")`: Registra un mensaje informativo antes de enviar la solicitud
•	`response = requests.get(f'{server_url}/')`: Realiza una solicitud GET al servidor
•	`log.info("Respuesta del servidor: %s", response.text)`: Registra la respuesta recibida del servidor

5. Punto de entrada del script:
•	`if __name__ == '__main__':`: Si el script se ejecuta como programa principal (y no se importa como módulo), se ejecutará el código dentro de este bloque
•	`send_request()`: Si el script es el programa principal, llama a la función `send_request()` para enviar una solicitud de prueba al servidor

Dockerfile (client)

Este `Dockerfile` crea una imagen de Docker para una aplicación en Python que ejecuta el script `client.py`. La imagen incluye todo lo necesario para el script, y el propio script `client.py`. Cuando se inicia un contenedor basado en esta imagen, automáticamente ejecutará el script `client.py.

1.	Imagen Base:
`FROM python:latest`: Esta línea especifica la imagen base para el contenedor. Aquí, se está usando la última versión oficial de Python disponible en Docker Hub. Esto significa que el contenedor tendrá Python ya instalado, listo para ejecutar cualquier código Python

2.	Directorio de Trabajo:
`WORKDIR /app`: Establece el directorio de trabajo dentro del contenedor a `/app`. Esto significa que todos los comandos que se ejecuten posteriormente en el `Dockerfile` se realizarán en este directorio

3. Instalación de Dependencias:
`RUN pip install requests`: Ejecuta el comando `pip install requests` para instalar la biblioteca `requests` en el contenedor. `requests` es una biblioteca de Python utilizada para realizar solicitudes HTTP, lo cual es necesario para el script `client.py` que se mencionó anteriormente

4. Copia del Código Fuente:
 `COPY client.py app/`: Esta línea copia el archivo `client.py` desde el contexto de construcción de Docker al directorio `/app` en el contenedor. Esto pone el script `client.py` en el contenedor para que pueda ser ejecutado

5. Comando por Defecto:
`CMD ["python", "app/client.py"]`: Define el comando por defecto que se ejecutará cuando se inicie el contenedor. En este caso, ejecuta `python app/client.py`, lo que iniciará el script `client.py` en Python

Dockerfile (db)

Este `Dockerfile` crea una imagen de Docker para un servidor MySQL con una configuración específica. Cuando se inicia un contenedor a partir de esta imagen, se configura con las variables de entorno especificadas (incluyendo la base de datos, usuarios y contraseñas) y ejecuta cualquier script de inicialización proporcionado (en este caso, `init.sql` e `init2.sql`).

1. Imagen Base:
FROM mysql:latest`: Esta línea especifica la imagen base del contenedor. Se utiliza la última versión de la imagen oficial de MySQL disponible en Docker Hub. Esto significa que el contenedor tendrá una instalación de MySQL lista para ser utilizada.

2. Establecimiento de Variables de Entorno:
•	`ENV MYSQL_DATABASE=biblioteca`: Esta instrucción establece una variable de entorno `MYSQL_DATABASE` con el valor `biblioteca`. Esto indica que, al iniciar el contenedor, MySQL creará automáticamente una base de datos llamada `biblioteca`
•	`ENV MYSQL_ROOT_PASSWORD=ccDec2023`: Establece la contraseña del usuario `root` de MySQL a `ccDec2023
•	`ENV MYSQL_USER=arubio`: Crea un usuario adicional llamado `arubio` en el servidor MySQL
•	`ENV MYSQL_PASSWORD=ccJan2024`: Establece la contraseña para el usuario `arubio` a `ccJan2024`

3. Copia de Scripts SQL:
`COPY init.sql /docker-entrypoint-initdb.d/` y `COPY init2.sql /docker-entrypoint-initdb.d/`: Estas líneas copian los archivos `init.sql` e `init2.sql` desde el contexto de construcción de Docker al directorio `/docker-entrypoint-initdb.d/` en el contenedor. MySQL ejecutará automáticamente cualquier script SQL o script de shell en este directorio la primera vez que se inicie el contenedor y se inicialice el directorio de datos de MySQL


init.sql

Este script SQL está diseñado para crear una base de datos para una biblioteca, con tablas para almacenar información sobre usuarios, libros y préstamos de libros.

1. Creación de la Base de Datos `biblioteca`:
•	`CREATE DATABASE IF NOT EXISTS biblioteca;`: Esta instrucción crea una base de datos llamada `biblioteca` si aún no existe. El uso de `IF NOT EXISTS` previene errores si la base de datos ya existe
•	`USE biblioteca;`: Esta línea indica que las operaciones siguientes se deben realizar en la base de datos `biblioteca`

2. Creación de la Tabla `usuarios`:
•	`CREATE TABLE usuarios (...)`: Define la estructura de una tabla llamada `usuarios`. Esta tabla contiene dos campos:
•	`id`: Un campo de tipo entero (`INT`) que se autoincrementa. Se usa como clave primaria (`PRIMARY KEY`), lo que significa que cada valor en esta columna debe ser único y no puede ser `NULL`
•	`nombre`: Un campo de tipo cadena de caracteres `VARCHAR(50)`, que puede almacenar nombres con una longitud máxima de 50 caracteres

3. Creación de la Tabla `libros`:
•	`CREATE TABLE libros (...)`: Establece la estructura para una tabla llamada `libros`, que también incluye dos campos:
•	`id`: Al igual que en la tabla `usuarios`, es un entero autoincrementado que actúa como clave primaria
•	`titulo`: Un campo de tipo `VARCHAR(100)` para almacenar el título del libro.
•	`autor`: Un campo de tipo `VARCHAR(50)` para almacenar el nombre del autor del libro

4. Creación de la Tabla `prestamos`:
•	`CREATE TABLE prestamos (...)`: Esta tabla está diseñada para registrar los préstamos de libros a usuarios. Incluye los siguientes campos:
•	`id_prestamo`: Clave primaria, entero autoincrementado
•	`usuario_id`: Un campo entero que referencia el `id` de un usuario en la tabla `usuarios`
•	`libro_id`: Un campo entero que referencia el `id` de un libro en la tabla `libros`
•	`fecha_prestamo`: Un campo de tipo `DATE`, que registra la fecha en que se realizó el préstamo
•	Las líneas `FOREIGN KEY (usuario_id) REFERENCES usuarios(id)` y `FOREIGN KEY (libro_id) REFERENCES libros(id)` establecen restricciones de clave foránea. Esto significa que cada `usuario_id` en `prestamos` debe existir en la tabla `usuarios`, y cada `libro_id` en `prestamos` debe existir en la tabla `libros`



Init2.sql

Este script SQL se utiliza para poblar las tablas `usuarios`, `libros`, y `prestamos` con datos de ejemplo. Estos datos representan usuarios de una biblioteca, libros disponibles en la biblioteca y registros de cuándo los usuarios han tomado prestados estos libros.

1. Inserción de Datos en la Tabla `usuarios`:
`INSERT INTO usuarios (nombre) VALUES ...`: Esta instrucción inserta registros en la tabla `usuarios`. En total, se insertan diez usuarios

2. Inserción de Datos en la Tabla `libros`:
`INSERT INTO libros (titulo, autor) VALUES ...`: Similar a la inserción en la tabla `usuarios`, esta línea inserta registros en la tabla `libros`. Cada registro consta de un `titulo` y un `autor`. Se añaden diez libros en total con sus respectivos títulos y autores

3. Inserción de Datos en la Tabla `prestamos`:
`INSERT INTO prestamos (usuario_id, libro_id, fecha_prestamo) VALUES ...`: Esta instrucción inserta registros en la tabla `prestamos`. Cada registro enlaza un `usuario_id` y un `libro_id` con una `fecha_prestamo`. En total, se insertan diez préstamos

Dockerfile (server)

Este `Dockerfile` crea una imagen de Docker para una aplicación Flask que interactúa con una base de datos MySQL. La imagen incluye un entorno Python, las dependencias necesarias para Flask y MySQL, y el código fuente de la aplicación. Al iniciar un contenedor basado en esta imagen, la aplicación Flask se iniciará automáticamente y escuchará en el puerto 5000.

1. Imagen Base:
 `FROM python:latest`: Esta línea establece la imagen base del contenedor como la última versión de Python disponible en Docker Hub. Esto proporciona un entorno Python listo para usar

2. Directorio de Trabajo:
 `WORKDIR /app`: Establece `/app` como el directorio de trabajo dentro del contenedor. Todos los comandos que se ejecuten posteriormente en el `Dockerfile` se realizarán en este directorio

3. Instalación de Dependencias:
 `RUN pip install Flask mysql-connector-python`: Instala las dependencias necesarias para la aplicación utilizando `pip`, el gestor de paquetes de Python. En este caso, se instalan Flask (un microframework web para Python) y `mysql-connector-python` (un controlador para conectar con bases de datos MySQL desde Python)

4. Copia del Código Fuente:
`COPY server.py app/`: Copia el archivo `server.py` desde el contexto de construcción de Docker al directorio `/app` en el contenedor. Esto sitúa el script del servidor en el contenedor para su ejecución

5. Exposición del Puerto:
`EXPOSE 5000`: Indica que el contenedor escuchará en el puerto 5000. Esto es estándar para aplicaciones Flask. La instrucción `EXPOSE` es más una documentación para los desarrolladores, ya que no abre activamente el puerto; es necesario mapear los puertos al ejecutar el contenedor

6. Comando por Defecto:
 `CMD ["python", "app/server.py"]`: Define el comando que se ejecutará por defecto cuando se inicie el contenedor. En este caso, arranca la aplicación Flask ejecutando `server.py` con Python




server.py

Este script Python es una aplicación web utilizando el microframework Flask, que interactúa con una base de datos MySQL. Esta aplicación permite registrar usuarios, libros y préstamos de libros en la base de datos a través de una interfaz web.

1. Importaciones y Configuración de Logging:
•	Se importan los módulos necesarios: Flask para la aplicación web, request para manejar solicitudes HTTP, logging para registrar eventos y mysql.connector para interactuar con la base de datos MySQL
•	Se configura el nivel de registro en `INFO`

2. Creación de la Aplicación Flask:
   `app = Flask(__name__)`: Crea una instancia de una aplicación Flask

3. Configuración de la Conexión a la Base de Datos:
 `db_config`: Un diccionario con la configuración necesaria para conectar con la base de datos MySQL, incluyendo el host, usuario, contraseña y nombre de la base de datos

4. Rutas y Funciones de la Aplicación:
•	`@app.route('/')`: Define la ruta raíz (`/`). La función asociada devuelve un mensaje de bienvenida.
•	`@app.route('/formulario', methods=['GET', 'POST'])`: Define la ruta `/formulario` para el registro de usuarios. Si el método es `GET`, muestra un formulario HTML para ingresar el nombre del usuario. Si es `POST`, procesa los datos del formulario, inserta un nuevo usuario en la base de datos y muestra un mensaje de bienvenida.
•	`@app.route('/libro', methods=['GET', 'POST'])`: Similar a `/formulario`, pero para el registro de libros. El formulario permite ingresar el título y autor del libro.
•	`@app.route('/prestamo', methods=['GET', 'POST'])`: Ruta para registrar préstamos de libros. El formulario solicita el ID del usuario, el ID del libro y la fecha de préstamo. Si es `POST`, inserta el préstamo en la base de datos.

5. Conexión y Manipulación de la Base de Datos:
En cada función de ruta que procesa un formulario `POST`, se establece una conexión con la base de datos (`mysql.connector.connect(**db_config)`), se crea un cursor, se ejecuta una sentencia SQL para insertar los datos y se cierra la conexión

6. Ejecución de la Aplicación:
•	El bloque `if __name__ == '__main__':` asegura que el servidor Flask solo se ejecute si el script es el programa principal
•	`app.run(host='0.0.0.0', port=5000)`: Inicia el servidor Flask, escuchando en todas las interfaces de red (`0.0.0.0`) en el puerto 5000



Pantallas resultantes al interactuar con la aplicación web

1.- localhost:8000: Pantalla de bienvenida

 

2.- localhost:8000/formulario

 

3.- localhost:8000/formulario – Respuesta del servidor

 

4.- localhost:8000/libro

 

5.- localhost:8000/libro – Respuesta del servidor

 










6.- localhost:8000/prestamo

 

7.- localhost:8000/prestamo – Respuesta del servidor

 




	

 
3. Ejercicio 3 y 3(a)

Estructura de directorios

 

Código asociado a esa estructura

docker-compose.yml

Los únicos cambios que tuvieron que efectuarse en este script, con respecto al Ejercicio 2, son los siguientes:

	`server`: Configura el servidor de aplicaciones, en este caso es un servidor Flask
•	`build`: Construye la imagen del contenedor desde el directorio `./flask/`
•	`volumes`: ‘./flask:/flask’; Monta un volumen local para persistir o compartir datos


client.py

No presenta cambios con respecto al Ejercicio 2.

Dockerfile (client)

No presenta cambios con respecto al Ejercicio 2.


Dockerfile (db)

No presenta cambios con respecto al Ejercicio 2.

init.sql

No presenta cambios con respecto al Ejercicio 2.

Init2.sql

No presenta cambios con respecto al Ejercicio 2.

Dockerfile (flask)

Los únicos cambios que tuvieron que efectuarse en este script, con respecto al Ejercicio 2, son los siguientes:

2. Directorio de Trabajo:
 `WORKDIR /flask`: Establece `/flask` como el directorio de trabajo dentro del contenedor

4. Copia del Código Fuente:
`COPY server.py flask/`: Copia el archivo `server.py` desde el contexto de construcción de Docker al directorio `/flask` en el contenedor

server.py

Al igual que en el Ejercicio 2, a través de este script se sirve una aplicación Flask que proporciona una interfaz web para añadir usuarios, libros y préstamos de libros a una base de datos denominada `biblioteca`. Utiliza plantillas HTML para la presentación de formularios (ubicados en un directorio independiente denominado ‘templates’) y se comunica con una base de datos MySQL para almacenar esta información. Sin embargo, tal como lo indica el enunciado de la tarea asociada al presente Ejercicio, en este caso se modifica la página web para que también incluya hojas de estilo CSS y contenido dinámico en Javascript; realizando las modificaciones correspondientes del servidor de Flask en Python para que pueda servir estas hojas.

A continuación se incluyen las secciones donde se efectuaron cambios con respecto al Ejercicio 2:

4. Rutas y Funciones de la Aplicación:
•	`@app.route('/')`: Define la ruta raíz (`/`). La función asociada renderiza y devuelve el template `index.html`
•	`@app.route('/formulario', methods=['GET', 'POST'])`: Define la ruta `/formulario`. Si el método es `GET`, muestra un formulario HTML para ingresar el nombre del usuario (usando `render_template`). Si es `POST`, procesa los datos del formulario, inserta un nuevo usuario en la base de datos y muestra un mensaje de bienvenida
•	`@app.route('/libro', methods=['GET', 'POST'])`: Similar a `/formulario`, pero para el registro de libros. Utiliza el template `libro.html` para el formulario.
•	`@app.route('/prestamo', methods=['GET', 'POST'])`: Ruta para registrar préstamos de libros. Usa el template `prestamo.html` para el formulario y procesa los datos de préstamo si el método es `POST`

style.css

Este fragmento de código es un conjunto de reglas CSS destinadas a estilizar la página web. Establece tipografías, colores, estilos de botones y formularios para crear una experiencia de usuario agradable y fácil de navegar.

1. Estilo General del Cuerpo:
•	`body`: Aplica estilos al cuerpo de la página web
•	`font-family: Arial, sans-serif;`: Establece la fuente del texto como Arial o, si no está disponible, cualquier fuente sans-serif
•	`background-color: #f0f0f0;`: Establece un color de fondo claro (#f0f0f0) para la página
•	`color: #333;`: Define el color predeterminado del texto como un gris oscuro (#333)

2. Imágenes de Ancho Completo: Utilizaremos una imagen en la página de bienvenida.
•	`.full-width-image`: Aplica estilos a las imágenes con la clase `full-width-image` 
•	`width: 100%;`: Hace que la imagen ocupe el 100% del ancho de su contenedor
•	`height: 400px;`: Fija la altura de la imagen a 400 píxeles
•	`object-fit: cover;`: Hace que la imagen cubra completamente el área asignada sin deformarse

3. Texto Centrado:
•	`.centered-text`: Aplica estilos a los elementos con la clase `centered-text`
•	`text-align: center;`: Centra el texto dentro de estos elementos

4. Contenedor del Formulario:
•	`.form-container`: Diseña los contenedores de formularios con la clase `form-container`
•	`max-width: 500px;`: Limita el ancho máximo del contenedor a 500 píxeles
•	`margin: 20px auto;`: Centra el contenedor en la página y añade un margen de 20 píxeles
•	`padding: 20px;`: Añade un relleno de 20 píxeles dentro del contenedor
•	`border: 1px solid #ddd;`: Crea un borde sólido de 1 píxel con un color gris claro
•	`border-radius: 10px;`: Redondea las esquinas del contenedor
•	`box-shadow: 0 0 10px rgba(0,0,0,0.1);`: Añade una sombra ligera alrededor del contenedor
•	`background-color: #fff;`: Establece un fondo blanco para el contenedor

5. Estilos de Entrada:
•	`input[type="text"], input[type="number"], input[type="date"], input[type="submit"]`: Aplica estilos a diferentes tipos de campos de entrada (`text`, `number`, `date`, `submit`)
•	`width: calc(100% - 40px);`: Establece el ancho del campo, restando 40 píxeles al 100% del ancho disponible (para tener en cuenta el margen y el relleno)
•	`padding: 10px;`: Añade un relleno de 10 píxeles dentro de cada campo
•	`margin: 10px 20px;`: Establece los márgenes alrededor de cada campo
•	`border: 1px solid #ddd;`: Define un borde sólido de 1 píxel en color gris claro
•	`border-radius: 5px;`: Redondea las esquinas de los campos de entrada

6. Estilo del Botón de Enviar:
•	`input[type="submit"]`: Aplica estilos adicionales específicamente a los botones de enviar
•	`background-color: #007bff;`: Asigna un color de fondo azul
•	`color: white;`: Establece el texto del botón en blanco
•	`cursor: pointer;`: Cambia el cursor a un puntero cuando se pasa sobre el botón
•	`input[type="submit"]:hover`: Estilos para cuando el cursor pasa sobre el botón
•	`background-color: #0056b3;`: Cambia el color de fondo a un azul más oscuro al pasar el cursor sobre el botón

Imagen ‘Biblioteca’

Utilizada en la plantilla index.html para mejorar la apariencia de la página web de inicio de la aplicación.

Script.js

Este script JavaScript agrega dinámicamente un párrafo y un botón al cuerpo de la página web cuando se carga por completo. Además, el botón tiene una funcionalidad interactiva que muestra un mensaje de agradecimiento al usuario cuando se hace clic en él.

1. Evento DOMContentLoaded:
`document.addEventListener('DOMContentLoaded', function() {...});`: Este código registra un evento que se dispara cuando todo el contenido del DOM ha sido completamente cargado y analizado, sin esperar hojas de estilo, imágenes y subframes para terminar de cargar. El código dentro de esta función se ejecutará una vez que la página esté completamente cargada.

2. Creación de un Nuevo Párrafo:
•	`var nuevoParrafo = document.createElement('p');`: Crea un nuevo elemento párrafo (`<p>`) y lo almacena en la variable `nuevoParrafo`
•	`nuevoParrafo.textContent = 'Este es un contenido dinámico generado por JavaScript.';`: Establece el texto del párrafo a "Este es un contenido dinámico generado por JavaScript."

3. Creación de un Botón:
•	`var nuevoBoton = document.createElement('button');`: Crea un nuevo elemento botón (`<button>`) y lo almacena en la variable `nuevoBoton`
•	`nuevoBoton.textContent = 'Haz clic aquí';`: Establece el texto del botón a "Haz clic aquí"

4. Funcionalidad del Botón:
•	`nuevoBoton.addEventListener('click', function() {...});`: Añade un evento de tipo `click` al botón. Cuando el botón se presiona, se ejecuta la función anónima asociada
•	`alert('¡Gracias por tu visita!');`: La función anónima muestra un cuadro de alerta con el mensaje "¡Gracias por tu visita!" cuando se hace clic en el botón

5. Añadiendo Elementos al Cuerpo de la Página:
•	`document.body.appendChild(nuevoParrafo);`: Añade el párrafo creado (`nuevoParrafo`) al final del cuerpo de la página
•	`document.body.appendChild(nuevoBoton);`: Añade el botón creado (`nuevoBoton`) justo después del párrafo en el cuerpo de la página

index.html

Esta plantilla HTML sirve como estructura básica para la página web de la biblioteca, con un diseño y funcionalidad enriquecidos por CSS y JavaScript externos. Utiliza la sintaxis de Flask para referenciar recursos estáticos, lo que permite una gestión eficiente de archivos como hojas de estilo y scripts en aplicaciones Flask.

1. Doctype y Estructura HTML:
•	`<!DOCTYPE html>`: Especifica que este documento es HTML5
•	Las etiquetas `<html>`, `<head>`, y `<body>` estructuran el documento en secciones lógicas

2. Cabeza del Documento:
•	`<head>`: Contiene metadatos y enlaces a recursos externos
•	`<title>Biblioteca</title>`: Define el título de la página, que aparece en la pestaña del navegador
•	`<link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='css/style.css') }}">`: Enlaza una hoja de estilo CSS. La función `url_for('static', filename='css/style.css')` es específica de Flask y se utiliza para generar una URL al archivo de hoja de estilo `style.css` dentro de la carpeta `static`

3. Cuerpo del Documento:
•	`<h1 class="centered-text">Bienvenido a la Biblioteca de Alejandría</h1>`: Muestra el encabezado principal centrado con un mensaje de bienvenida
•	`<img src="{{ url_for('static', filename='images/biblioteca.jpg') }}" alt="Imagen de una biblioteca" class="full-width-image">`: Inserta una imagen, utilizando la función `url_for` para obtener la URL de la imagen `biblioteca.jpg` en la carpeta `static`. La clase `full-width-image` define estilos para que la imagen se extienda a lo ancho de la página
•	Los párrafos `<p>` proporcionan información adicional sobre la biblioteca

4. Inclusión de un Script JavaScript:
 `<script src="{{ url_for('static', filename='js/script.js') }}"></script>`: Incluye un archivo JavaScript (`script.js`) utilizando la función `url_for` para generar su URL. Este script añade funcionalidad interactiva a la página

formulario.html

Esta plantilla HTML proporciona una interfaz para que los usuarios se registren en la aplicación web. Utiliza CSS para el estilo y tiene un formulario HTML simple que permite a los usuarios introducir su nombre y enviarlo al servidor para su procesamiento. La integración con Flask se indica mediante el uso de la función `url_for` para referenciar recursos estáticos.

1. Doctype y Estructura HTML:
•	`<!DOCTYPE html>`: Declara el tipo de documento como HTML5
•	Las etiquetas `<html>`, `<head>`, y `<body>` estructuran el documento en secciones lógicas

2. Cabeza del Documento:
•	`<head>`: Contiene metadatos y enlaces a recursos externos
•	`<title>Formulario de Bienvenida</title>`: Establece el título de la página, que se muestra en la pestaña del navegador
•	`<link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='css/style.css') }}">`: Enlaza una hoja de estilo CSS. La función `url_for('static', filename='css/style.css')` es específica de Flask y genera una URL al archivo CSS en la carpeta `static`

3. Cuerpo del Documento (Body):
•	`<div class="form-container">`: Contenedor `div` con la clase `form-container`, que se refiere a estilos definidos en la hoja de estilo CSS vinculada.
•	Dentro del `div`, hay una estructura de formulario HTML:
•	`<h1>Registro de Usuario</h1>`: Encabezado que indica el propósito del formulario.
•	`<form method="POST" action="/formulario">`: Define el formulario con el método `POST`, que enviará los datos del formulario al servidor. El atributo `action` indica que los datos del formulario se enviarán a la ruta `/formulario`
•	`<label for="nombre">Nombre:</label>`: Etiqueta para el campo de entrada del nombre
•	`<input type="text" id="nombre" name="nombre" required>`: Campo de entrada para que el usuario introduzca su nombre. El atributo `required` indica que este campo es obligatorio
•	`<input type="submit" value="Enviar">`: Botón de enviar que enviará los datos del formulario

libro.html

Esta plantilla HTML proporciona una interfaz de usuario para el registro de libros en la aplicación web. Utiliza estilos CSS para la presentación y tiene un formulario HTML para la entrada de datos del libro (título y autor) que se enviarán al servidor para su procesamiento. La integración con Flask se indica a través del uso de la función `url_for` para referenciar recursos estáticos.

1. Doctype y Estructura HTML:
•	`<!DOCTYPE html>`: Declara el documento como HTML5
•	Las etiquetas `<html>`, `<head>`, y `<body>` son las estructuras básicas del documento HTML

2. Cabeza del Documento:
•	`<head>`: Contiene información de metadatos y enlaces a recursos externos
•	`<title>Registro de Libro</title>`: Define el título de la página, que aparecerá en la pestaña del navegador
•	`<link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='css/style.css') }}">`: Enlaza una hoja de estilo CSS externa. La función `url_for('static', filename='css/style.css')` es específica de Flask y genera una URL al archivo CSS en la carpeta `static`

3. Cuerpo del Documento (Body):
•	`<div class="form-container">`: Contenedor `div` con la clase `form-container`. Esta clase aplica estilos definidos en la hoja de estilo CSS vinculada para formatear y presentar el formulario de manera atractiva
•	Dentro del `div`, se define un formulario HTML para el registro de libros:
•	`<h1>Registro de Libro</h1>`: Encabezado para el formulario
•	`<form method="POST" action="/libro">`: El formulario utiliza el método `POST` para enviar los datos del formulario al servidor. El atributo `action` especifica que los datos se enviarán a la ruta `/libro`
•	`<label for="titulo">Título:</label>` seguido de `<input type="text" id="titulo" name="titulo" required>`: Campo de entrada para que el usuario introduzca el título del libro. El atributo `required` asegura que este campo debe ser completado antes de enviar el formulario
•	`<label for="autor">Autor:</label>` seguido de `<input type="text" id="autor" name="autor" required>`: Campo de entrada para el nombre del autor del libro, también marcado como obligatorio
•	`<input type="submit" value="Registrar Libro">`: Botón para enviar el formulario

prestamo.html

Esta plantilla HTML proporciona una interfaz de usuario para el registro de préstamos en la biblioteca. Utiliza CSS para el diseño y presenta un formulario HTML para la entrada de datos del préstamo, que incluye el ID del usuario, el ID del libro y la fecha del préstamo, que luego se enviarán al servidor para su procesamiento. La integración con Flask se indica a través del uso de la función `url_for` para referenciar recursos estáticos.

1. Doctype y Estructura HTML:
•	`<!DOCTYPE html>`: Indica que el documento es HTML5
•	Las etiquetas `<html>`, `<head>` y `<body>` estructuran el documento en secciones lógicas

2. Cabeza del Documento:
•	`<head>`: Contiene metadatos y enlaces a recursos externos
•	`<title>Registro de Préstamo</title>`: Establece el título de la página, que aparecerá en la pestaña del navegador
•	`<link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='css/style.css') }}">`: Enlaza una hoja de estilo CSS. La función `url_for('static', filename='css/style.css')` es específica de Flask y genera una URL al archivo CSS en la carpeta `static`

3. Cuerpo del Documento (Body):
•	`<div class="form-container">`: Contenedor `div` con la clase `form-container`, que aplica estilos definidos en la hoja de estilo CSS vinculada para mejorar la presentación del formulario
•	Dentro del `div`, se define un formulario HTML para el registro de préstamos:
•	`<h1>Registro de Préstamo</h1>`: Encabezado para el formulario
•	`<form method="POST" action="/prestamo">`: El formulario usa el método `POST` para enviar datos al servidor. El atributo `action` especifica que los datos se enviarán a la ruta `/prestamo`
•	`<label for="usuario_id">ID Usuario:</label>` seguido de `<input type="number" id="usuario_id" name="usuario_id" required>`: Campo de entrada para el ID del usuario que realiza el préstamo, marcado como obligatorio
•	`<label for="libro_id">ID Libro:</label>` seguido de `<input type="number" id="libro_id" name="libro_id" required>`: Campo de entrada para el ID del libro que se está prestando, también obligatorio
•	`<label for="fecha_prestamo">Fecha de Préstamo:</label>` seguido de `<input type="date" id="fecha_prestamo" name="fecha_prestamo" required>`: Campo para seleccionar la fecha del préstamo, igualmente marcado como obligatorio
•	`<input type="submit" value="Registrar Préstamo">`: Botón para enviar el formulario

Pantallas resultantes al interactuar con la aplicación web

Nota:
Es importante mencionar que las pantallas resultantes de este Ejercicio, así como la de los demás a partir de él, tendrán la misma apariencia. En consecuencia, solo se mostrarán en esta sección.

Por otro lado, también debe tenerse en cuenta que, en todos los Ejercicios, la dirección web local para interactuar con la aplicación web será: localhost:8000.

1.- localhost:8000: Pantalla de bienvenida

 




2.- localhost:8000 – Respuesta del servidor después de haber hecho clic en el botón ‘Haz clic aquí’

 

3.- localhost:8000/formulario

 

4.- localhost:8000/formulario – Respuesta del servidor

 










5.- localhost:8000/libro

 

6.- localhost:8000/libro – Respuesta del servidor

 

7.- localhost:8000/prestamo

 

8.- localhost:8000/prestamo – Respuesta del servidor

 




 
4. Ejercicio 3(b)

Estructura de directorios

 

 
Código asociado a esa estructura

docker-compose.yml

Los únicos cambios que tuvieron que efectuarse en este script, con respecto al Ejercicio 2, son los siguientes:

2. Servicios:
	`server`: Configura el servidor de aplicaciones, en este caso es un servidor Node,js
•	`build`: Construye la imagen del contenedor desde el directorio `./node.js/`
•	volumes: ./node.js:/node.js’: Monta un volumen local para el código fuente del servidor Node.js.

client.py

No presenta cambios con respecto al Ejercicio 2.

Dockerfile (client)

No presenta cambios con respecto al Ejercicio 2.


Dockerfile (db)

No presenta cambios con respecto al Ejercicio 2.

init.sql

No presenta cambios con respecto al Ejercicio 2.

init2.sql

No presenta cambios con respecto al Ejercicio 2.

Dockerfile (node.js)

Este `Dockerfile` crea una imagen de Docker para una aplicación Node.js. Configura el entorno, instala las dependencias necesarias y prepara la aplicación para ser ejecutada. Cuando se inicia un contenedor basado en esta imagen, se ejecuta automáticamente la aplicación Node.js definida en `server.js`.

1. Imagen Base:
`FROM node:latest`: Esta línea especifica la imagen base del contenedor. Se usa la última versión de Node.js disponible en Docker Hub. Esta imagen incluirá un entorno Node.js completo y listo para usar

2. Directorio de Trabajo:
`WORKDIR /node_app`: Define `/node_app` como el directorio de trabajo dentro del contenedor. Todos los comandos que se ejecuten después de esta instrucción se llevarán a cabo en este directorio

3. Copia de Archivos `package.json` y `package-lock.json’:
`COPY package*.json ./`: Copia ambos archivos `package.json` y `package-lock.json` desde el directorio actual en el host al directorio de trabajo actual (`/node_app`) en el contenedor. Estos archivos definen las dependencias del proyecto

4. Instalación de Dependencias:
`RUN npm install`: Ejecuta `npm install` para instalar las dependencias del proyecto especificadas en `package.json` y `package-lock.json`. Esto se hace antes de copiar todo el código fuente para aprovechar la caché de capas de Docker si solo cambian los archivos de código fuente y no las dependencias

5. Copia del Código Fuente:
`COPY . .`: Copia todos los archivos y directorios restantes desde el directorio actual en el host al directorio de trabajo en el contenedor (`/node_app`). Esto incluye el código fuente de la aplicación Node.js y cualquier otro archivo necesario para la aplicación

6. Exposición del Puerto:
 `EXPOSE 5000`: Indica que el contenedor estará escuchando en el puerto 5000

7. Comando por Defecto:
`CMD ["node", "server.js"]`: Define el comando que se ejecutará por defecto cuando se inicie el contenedor. En este caso, inicia la aplicación Node.js ejecutando `server.js` con Node.js.

package-lock.json

Este archivo asegura que se instalen exactamente las mismas versiones de todas las dependencias (y subdependencias) en todas las instalaciones. Se genera automáticamente cuando se ejecutan operaciones npm (Node Package Manager)  que modifican el árbol de nodos, como npm install (sin parámetros), npm install <nombre_del_paquete>, o npm update.

Propósito: El package-lock.json contiene información detallada sobre el árbol de dependencias, incluyendo la versión exacta de cada paquete instalado, su ubicación dentro del árbol de nodos y sus dependencias adicionales. Esto ayuda a evitar discrepancias en las versiones de los paquetes entre diferentes entornos de desarrollo y producción.

No se Modifica Manualmente: Es importante no modificar este archivo manualmente, ya que está diseñado para ser actualizado automáticamente por npm.



package.json

Este archivo es esencial para cualquier proyecto Node.js, ya que especifica las dependencias necesarias, los metadatos del proyecto, y los scripts para la ejecución del mismo. Facilita la gestión de dependencias y la configuración del entorno de desarrollo, lo que es crucial para el desarrollo y despliegue eficientes de aplicaciones Node.js. Se genera de la siguiente manera:

Creación Inicial: Al iniciar un nuevo proyecto Node.js, se crea un package.json ejecutando el comando npm init en la terminal. Esto inicia un proceso interactivo que permite configurar las propiedades básicas del proyecto, como el nombre, la versión, la descripción, punto de entrada, scripts, autor, licencia, etc.

Adición de Dependencias: Cuando se instalan paquetes utilizando npm con comandos como npm install <nombre_del_paquete>, npm añade automáticamente estas dependencias al archivo package.json en la sección ‘dependencies’.

La configuración resultante en nuestro caso es la siguiente:

1. Metadatos Básicos:
•	`"name": "biblioteca-app"`: El nombre del proyecto. En este caso, se llama "biblioteca-app"
•	`"version": "1.0.0"`: La versión actual del proyecto. Aquí se sigue el esquema de versionado semántico (major.minor.patch)
•	`"description": "Biblioteca web application"`: Una breve descripción del proyecto
•	`"main": "server.js"`: El punto de entrada principal del proyecto. Aquí, es `server.js`, lo que significa que este es el archivo que se ejecutará cuando se inicie la aplicación
•	`"author": "Antonio Rubio"`: El nombre del autor del proyecto
•	`"license": "ISC"`: El tipo de licencia bajo la cual se distribuye el proyecto. ISC es una licencia de software libre

2. Scripts:
`"scripts": {"start": "node server.js"}`: Define los scripts que se pueden ejecutar desde la línea de comandos. En este caso, el script `start` inicia la aplicación ejecutando `node server.js`

3. Dependencias:
•	‘”dependencies": { ... }`: Enumera las bibliotecas de las que depende el proyecto. Estas bibliotecas se instalarán automáticamente al ejecutar `npm install`. Las dependencias incluidas son:
•	`body-parser`: Middleware para analizar cuerpos de solicitudes entrantes en Express
•	`express`: El framework web para Node.js
•	`mysql2`: Un módulo cliente para interactuar con bases de datos MySQL
•	`ejs`: Un motor de plantillas para generar HTML

server,js

Este script de Node.js configura un servidor web para la biblioteca, maneja rutas para diferentes funcionalidades (registro de usuarios, libros, préstamos), interactúa con una base de datos MySQL y utiliza plantillas EJS para renderizar vistas (el equivalente a los ‘templates’ que venían utilizándose).

1. Importaciones y Configuraciones Iniciales:
•	`express`, `mysql2`, y `body-parser` son importados. Estos módulos son usados para crear el servidor, interactuar con la base de datos MySQL, y analizar cuerpos de solicitudes HTTP, respectivamente
•	Se crea una instancia de una aplicación Express y se configura para usar el puerto `5000`

2. Configuración del Motor de Vistas y Archivos Estáticos:
•	`app.set('view engine', 'ejs')`: Establece EJS como el motor de renderizado de vistas. EJS es un sistema de plantillas que permite generar HTML con JavaScript
•	`app.use('/static', express.static('public'))`: Sirve archivos estáticos (como CSS, JavaScript, imágenes) desde el directorio `public`, accesibles en la ruta `/static`

3. Middleware de Análisis de Cuerpos de Solicitudes:
`bodyParser.urlencoded({ extended: false })` y `bodyParser.json()`: Configura el middleware para analizar cuerpos de solicitudes codificados en URL y JSON

4. Conexión a la Base de Datos MySQL:
`mysql.createPool(...)`: Crea un "pool" de conexiones a la base de datos MySQL con las credenciales y detalles de la base de datos proporcionados

5. Definición de Rutas:
•	Rutas HTTP GET y POST para diferentes endpoints (`/`, `/formulario`, `/libro`, `/prestamo`):
•	Cada ruta `GET` sirve una página web renderizada con EJS. Por ejemplo, `res.render('index')` renderiza y envía la página `index.ejs`
•	Las rutas `POST` manejan la recepción de datos de formularios y ejecutan consultas SQL para insertar datos en la base de datos (usuarios, libros, préstamos)

6. Manejo de Errores en Consultas SQL:
En cada consulta SQL, se comprueba si hay errores (`if (err) throw err;`). Si hay un error, se lanza una excepción

7. Inicio del Servidor:
`app.listen(port, ...)`: Inicia el servidor para que escuche en el puerto especificado, mostrando un mensaje en la consola una vez que el servidor está en funcionamiento



Directorio node_modules

El directorio `node_modules` en un proyecto de servidor Node.js es donde se almacenan todas las dependencias (bibliotecas, frameworks, herramientas, etc.) necesarias para el proyecto. Estas dependencias son definidas en el archivo `package.json` del proyecto y se instalan localmente en este directorio.

El directorio node_modules en un proyecto Node.js se genera y se llena automáticamente a través del gestor de paquetes npm (Node Package Manager).


style,css

No presenta cambios con respecto al Ejercicio 3 y 3(a).

Imagen ‘Biblioteca’

No presenta cambios con respecto al Ejercicio 3 y 3(a).

script.js

No presenta cambios con respecto al Ejercicio 3 y 3(a).

index.ejs

La única diferencia con el código utilizado en el Ejercicio 3 y 3(a) radica en que Node.js no trabaja con la estructura ‘url_for’ en su lugar, en Node.js, la referencia a recursos estáticos se efectúa de la siguiente manera:

•	href="/static/css/style.css": El atributo href especifica la ubicación (URL) del recurso vinculado. En este caso, el valor /static/css/style.css es la ruta al archivo CSS. Esta ruta sugiere que el archivo style.css se encuentra dentro de un directorio css, el cual a su vez está dentro de un directorio static. La ruta comienza con una barra (/), lo que indica que es una ruta absoluta desde la raíz del servidor web.
•	`src="/static/js/script.js"`: El atributo `src` especifica la ubicación (URL) del archivo de script que se va a incluir. En este caso, `"/static/js/script.js"` indica que el archivo JavaScript se encuentra en un directorio llamado `js`, que a su vez está dentro de un directorio `static`. La ruta comienza con una barra (`/`), lo que sugiere que es una ruta absoluta desde la raíz del sitio web.

formulario.ejs

La única diferencia con el código utilizado en el Ejercicio 3 y 3(a) radica en que Node.js no trabaja con la estructura ‘url_for’ en su lugar, en Node.js, la referencia a recursos estáticos se efectúa de la siguiente manera: href="/static/css/style.css".




libro.ejs

Al igual que con la plantilla ‘formulario, la única diferencia con el código utilizado en el Ejercicio 3 y 3(a) radica en que Node.js no trabaja con la estructura ‘url_for’ en su lugar, en Node.js, la referencia a recursos estáticos se efectúa de la siguiente manera: href="/static/css/style.css".

prestamo.ejs

Al igual que con la plantilla ‘formulario, la única diferencia con el código utilizado en el Ejercicio 3 y 3(a) radica en que Node.js no trabaja con la estructura ‘url_for’ en su lugar, en Node.js, la referencia a recursos estáticos se efectúa de la siguiente manera: href="/static/css/style.css".
 
5. Ejercicio 4, 4(a) y 4(b)

Estructura de directorios

 


 
Código asociado a esa estructura

docker-compose.yml

Los únicos cambios que tuvieron que efectuarse en este script, con respecto al Ejercicio 2, son los siguientes:

	`server`: Configura el servidor de aplicaciones, en este caso es un servidor Go
•	`build`: Construye la imagen del contenedor desde un Dockerfile en el directorio `./go/`
•	`ports`: Mapea el puerto 8000 del host al puerto 8080 del contenedor

client,go

Este es un script escrito en Go (también conocido como Golang), un lenguaje de programación compilado y concurrente desarrollado por Google. Este programa está diseñado para realizar una solicitud HTTP a un servidor y mostrar la respuesta.

1. Paquete y Importaciones:
•	`package main`: Define el paquete principal. En Go, el paquete `main` es el punto de entrada de la ejecución del programa
•	`import`: Importa paquetes necesarios para el funcionamiento del programa:
•	`fmt`: Para operaciones de entrada/salida formateadas (por ejemplo, imprimir en la consola)
•	`io/ioutil`: Para leer la respuesta del cuerpo de la solicitud HTTP
•	`log`: Para registrar mensajes, en este caso, errores
•	`net/http`: Para realizar solicitudes HTTP

2. Función Principal `main`:
•	`func main() {...}`: Define la función principal que se ejecuta cuando se inicia el programa
•	`url := "http://servidor:8080/"`: Declara una variable `url` y le asigna la dirección del servidor al que se hará la solicitud

3. Realizando una Solicitud HTTP:
•	`resp, err := http.Get(url)`: Realiza una solicitud HTTP GET a la URL especificada. Retorna un objeto de respuesta (`resp`) y un error (`err`). Si hay un error (por ejemplo, si el servidor no está accesible), se registra el error y se termina el programa
•	`defer resp.Body.Close()`: Aplaza el cierre del cuerpo de la respuesta hasta que se complete la función `main`. Esto es importante para evitar fugas de recursos

4. Leyendo el Cuerpo de la Respuesta:
`body, err := ioutil.ReadAll(resp.Body)`: Lee todo el cuerpo de la respuesta. Si hay un error al leer, se registra y se termina el programa

5. Imprimiendo la Respuesta:
`fmt.Println("Respuesta del servidor: ", string(body))`: Imprime la respuesta del servidor. La respuesta (`body`) es un conjunto de bytes, por lo que se convierte a `string` para una presentación legible

Dockerfile

Este `Dockerfile` utiliza un proceso de construcción en dos etapas para crear una imagen Docker eficiente y optimizada para una aplicación Go. La primera etapa compila la aplicación en un entorno de Go, mientras que la segunda etapa crea una imagen final ligera que contiene solo el ejecutable necesario para ejecutar la aplicación. Este enfoque minimiza el tamaño de la imagen final.

1. Primera Etapa: Compilación (builder):
•	`FROM golang:latest AS builder`: Esta línea inicia la primera etapa de construcción usando la imagen oficial de Go como base. La etapa se denomina `builder`, lo que permite referenciarla más adelante
•	`WORKDIR /app`: Establece el directorio de trabajo en `/app` dentro del contenedor
•	`COPY go.mod ./`: Copia el archivo `go.mod` al directorio de trabajo en el contenedor. Este archivo define las dependencias del proyecto
•	`COPY . .`: Copia todos los archivos de código fuente (incluyendo el resto de archivos y directorios) del directorio actual en la máquina host al directorio de trabajo en el contenedor
•	`RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o client client.go`: Compila la aplicación Go. La variable de entorno `CGO_ENABLED=0` desactiva CGO para una compilación estática, y `GOOS=linux` asegura la compatibilidad con el entorno de ejecución de Linux. El resultado es un ejecutable llamado `client`

2. Segunda Etapa: Creación de la Imagen Ligera:
•	`FROM scratch`: Comienza la segunda etapa de construcción usando una imagen base "scratch", que es esencialmente una imagen vacía. Es útil para crear imágenes muy pequeñas que contienen solo lo estrictamente necesario
•	`COPY --from=builder /app/client .`: Copia el ejecutable `client` compilado en la primera etapa desde `/app/client` a la raíz del sistema de archivos de la nueva imagen
•	`CMD ["./client"]`: Define el comando que se ejecutará cuando se inicie un contenedor basado en esta imagen. En este caso, ejecuta el ejecutable `client`

go.mod (client)

El archivo `go.mod` es fundamental para los proyectos Go, ya que Go, desde la versión 1.11, utiliza un sistema de módulos para manejar dependencias Este archivo ayuda a manejar las versiones de las dependencias externas de manera eficiente y reproducible. Además, facilita la construcción y el mantenimiento del código en diferentes entornos y máquinas, ya que asegura que se usen las mismas versiones de las dependencias en todas partes.

Inicialización: Se crea un go.mod al inicializar un nuevo módulo con el comando go mod init [nombre_del_módulo].
Actualización Automática: Al agregar importaciones al proyecto Go y luego ejecutar comandos como go build, Go actualizará automáticamente go.mod para incluir las dependencias necesarias.

Para el archivo go.mod relacionado con client.go se tiene la siguiente configuración:

•	Nombre del Módulo: ‘module github.com/AntonioRubio/biblioteca`. Esta línea define el nombre del módulo
•	Versión de Go: `go 1.21.5’. Especifica la versión mínima de Go requerida para este módulo. Esto asegura que se utilicen las características y funcionalidades del lenguaje que son compatibles con esa versión específica de Go. Aquí, se indica que el módulo requiere la versión 1.21.5 de Go.

Dockerfile (db)

No presenta cambios con respecto al Ejercicio 2.

init.sql

No presenta cambios con respecto al Ejercicio 2.

init2.sql

No presenta cambios con respecto al Ejercicio 2.

Dockerfile (go)

Este `Dockerfile` utiliza un proceso de construcción en dos etapas para crear una imagen Docker eficiente y optimizada para una aplicación Go. La primera etapa compila la aplicación en un entorno de Go, mientras que la segunda etapa crea una imagen final ligera que contiene solo el ejecutable y los recursos necesarios (plantillas, archivos estáticos). Este enfoque es eficiente en términos de tamaño de la imagen final.

1. Primera Etapa: Compilación (builder):
•	`FROM golang:latest AS builder`: Inicia la primera etapa de construcción usando la imagen oficial de Go como base. La etapa se nombra `builder` para referencias posteriores.
•	`WORKDIR /app`: Establece `/app` como el directorio de trabajo en el contenedor.
•	`COPY go.mod go.sum ./`: Copia los archivos `go.mod` y `go.sum` al directorio de trabajo del contenedor. Estos archivos definen las dependencias del proyecto y sus versiones.
•	`RUN go mod download`: Descarga las dependencias del proyecto especificadas en `go.mod` y `go.sum`.
•	`COPY . .`: Copia todos los archivos de código fuente del directorio actual en la máquina host al directorio de trabajo en el contenedor.
•	`RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o app server.go`: Compila la aplicación. `CGO_ENABLED=0` y `GOOS=linux` aseguran una compilación estática y compatible con Linux. El ejecutable resultante se nombra `app`.

2. Segunda Etapa: Creación de la Imagen Ligera:
•	`FROM scratch`: Inicia la segunda etapa de construcción usando una imagen base "scratch", que es esencialmente una imagen vacía. Ideal para crear imágenes mínimas
•	`COPY --from=builder /app/app /app`: Copia el ejecutable `app` de la primera etapa al sistema de archivos de la imagen final
•	`COPY --from=builder /app/templates /templates`: Copia las plantillas desde la etapa de construcción al contenedor final
•	`COPY --from=builder /app/static /static`: Copia archivos estáticos como hojas de estilo CSS y scripts JavaScript desde la etapa de construcción al contenedor final
•	`EXPOSE 8080`: Indica que el contenedor estará escuchando en el puerto 8080
•	`CMD ["./app"]`: Define el comando para ejecutar la aplicación (`app`) en el contenedor

go.mod (go)

El archivo `go.mod` de este Ejercicio establece que la versión utilizada de Go es la 1.21.5 y que el proyecto depende de una versión específica del driver MySQL para Go.

•	Declaración del Módulo:`module github.com/AntonioRubio/biblioteca`: Esta línea declara el nombre del módulo
•	Versión de Go:`go 1.21.5`: Especifica que el módulo fue creado con la versión 1.21.5 de Go. Esto ayuda a garantizar la compatibilidad y el uso correcto de las características del lenguaje disponibles en esa versión específica
•	Dependencias del Módulo:
	`require github.com/go-sql-driver/mysql v1.7.1 // indirect`: Esta línea especifica una dependencia del proyecto. Indica que el módulo requiere la versión `v1.7.1` del paquete `github.com/go-sql-driver/mysql`, que es un driver para conectar Go con bases de datos MySQL 
	El comentario `// indirect` indica que esta dependencia no es usada directamente por este módulo en su código, sino que puede ser requerida por otras dependencias

go.sum (go)

El archivo `go.sum` proporciona un nivel adicional de seguridad y confiabilidad en la gestión de dependencias. Al verificar las sumas de comprobación, Go puede asegurarse de que las dependencias no han sido alteradas o comprometidas desde que se generaron estas sumas. Si un paquete ha sido modificado de alguna manera desde que se calculó su suma de comprobación, Go lo detectará y emitirá una advertencia o un error, evitando así el uso de dependencias inseguras o alteradas.

El archivo go.sum se genera automáticamente junto con el archivo go.mod y es una parte integral del sistema de gestión de módulos de Go. Cada vez que se ejecutan comandos como go mod tidy, go get, go build, go test, etc., y estos comandos modifican el archivo go.mod (añadiendo, actualizando o eliminando dependencias), Go también actualiza o genera el archivo go.sum.

La estructura del archivo go.sum correspondiente a este Ejercicio es la siguiente:

1. Registro de Dependencias: `github.com/go-sql-driver/mysql v1.7.1 h1:lUIinVbN1DY0xBg0eMOzmmtGoHwWBbvnWubQUrtU8EI=`

•	Esta línea registra la suma de comprobación para una versión específica (`v1.7.1`) del paquete `github.com/go-sql-driver/mysql`, que es un driver de MySQL para Go.
•	La cadena larga al final (`h1:...`) es la suma de comprobación en sí, que es un hash generado a partir del contenido específico de esa versión del paquete.

2. Registro para el Archivo go.mod del Paquete: `github.com/go-sql-driver/mysql v1.7.1/go.mod h1:OXbVy3sEdcQ2Doequ6Z5BW6fXNQTmx+9S1MCJN5yJMI=`
  
•	Similar a la primera línea, pero esta vez la suma de comprobación es para el archivo `go.mod` de la versión `v1.7.1` del paquete `github.com/go-sql-driver/mysql`.
•	Esta suma de comprobación adicional asegura la integridad no solo del código del paquete, sino también de su lista de dependencias y otras especificaciones definidas en su `go.mod`.

server.go

Este script es un programa de servidor web escrito en Go que utiliza el paquete `net/http` para manejar solicitudes HTTP, `database/sql` con un driver MySQL para la conexión con una base de datos, y `html/template` para el renderizado de plantillas HTML. El servidor maneja varias rutas y realiza operaciones básicas de base de datos.

1. Importaciones:
Se importan los paquetes necesarios para la funcionalidad del servidor, incluyendo el manejo de HTTP, plantillas, base de datos y registro de errores

2. Conexión a la Base de Datos:
 El servidor establece una conexión con una base de datos MySQL usando el paquete `database/sql` y el driver MySQL (`github.com/go-sql-driver/mysql`). La conexión se configura con las credenciales y detalles de la base de datos

3. Servicio de Archivos Estáticos:
Se configura un manejador para servir archivos estáticos (CSS, JavaScript, imágenes) desde el directorio `static`

4. Configuración de Plantillas:
Se prepara el sistema de plantillas para renderizar páginas HTML dinámicas. Las plantillas están almacenadas en el directorio `templates`.

5. Manejadores de Rutas: Se definen varios manejadores de ruta (`http.HandleFunc`) para diferentes endpoints:
•	La ruta raíz (`/`) sirve la página principal
•	`/formulario` maneja el formulario de registro de usuarios
•	`/libro` maneja el registro de libros
•	`/prestamo` maneja el registro de préstamos de libros
•	Cada ruta maneja solicitudes GET para mostrar formularios y solicitudes POST para procesar datos enviados

6. Operaciones de Base de Datos:
En las rutas POST, se recogen los datos del formulario y se ejecutan consultas SQL para insertarlos en la base de datos

7. Inicio del Servidor:
El servidor se inicia y escucha en el puerto 8080. Las solicitudes entrantes son manejadas por los manejadores de ruta definidos


style,css

No presenta cambios con respecto al Ejercicio 3 y 3(a).

Imagen ‘Biblioteca’

No presenta cambios con respecto al Ejercicio 3 y 3(a).

script.js

No presenta cambios con respecto al Ejercicio 3 y 3(a).

index.html

No presenta cambios con respecto al Ejercicio 3(b), solo cambia la extensión a ‘html’.

formulario.html

No presenta cambios con respecto al Ejercicio 3(b), solo cambia la extensión a ‘html’.




libro.html

No presenta cambios con respecto al Ejercicio 3(b), solo cambia la extensión a ‘html’.

prestamo.html

No presenta cambios con respecto al Ejercicio 3(b), solo cambia la extensión a ‘html’.

 
6. Ejercicio 5

Estructura de directorios

 
 
Código asociado a esa estructura

docker-compose.yml

Los únicos cambios que tuvieron que efectuarse en este script, con respecto al Ejercicio 4, 4(a) y 4(b), son los siguientes:

2.	Servicios:
	`db`: Configura un servicio de base de datos PostgreSQL.
•	`container_name: postgres`: Asigna el nombre `postgres` al contenedor de la base de datos
•	`ports`: Mapea el puerto 5432 del host al puerto 5432 del contenedor, que es el puerto por defecto de PostgreSQL
•	`volumes`: Monta un volumen llamado `postgres-data` para persistir los datos de la base de datos.

4. Volúmenes:
`volumes`: Define un volumen `postgres-data` para la persistencia de datos de la base de datos PostgreSQL.

client,go

No presenta cambios con respecto al Ejercicio 4, 4(a) y 4(b).

Dockerfile (client)

No presenta cambios con respecto al Ejercicio 4, 4(a) y 4(b).

go.mod

No presenta cambios con respecto al Ejercicio 4, 4(a) y 4(b).

Dockerfile (db)

Este `Dockerfile` crea una imagen Docker para un servidor PostgreSQL manteniendo el mismo funcionamiento de la base de datos ‘biblioteca’.

1. Imagen Base:
`FROM postgres:latest`: Esta línea indica que la imagen base para este contenedor es la última versión de la imagen oficial de PostgreSQL disponible en Docker Hub

2. Variables de Entorno:
•	`ENV POSTGRES_DB=biblioteca`: Establece la variable de entorno `POSTGRES_DB`. Cuando se inicia el contenedor, PostgreSQL creará automáticamente una base de datos con este nombre, en este caso, `biblioteca`
•	`ENV POSTGRES_USER=arubio`: Establece la variable de entorno `POSTGRES_USER`. Define el nombre del usuario administrador de la base de datos; aquí, el usuario es `arubio`
•	`ENV POSTGRES_PASSWORD=ccJan2024`: Establece la variable de entorno `POSTGRES_PASSWORD`. Define la contraseña para el usuario administrador de la base de datos

3. Copia de Scripts SQL:
 `COPY data1.sql /docker-entrypoint-initdb.d/` y `COPY data2.sql /docker-entrypoint-initdb.d/`: Estas líneas copian archivos de script SQL (`data1.sql` e `data2.sql`) desde el contexto de construcción de Docker al directorio `/docker-entrypoint-initdb.d/` en el contenedor. PostgreSQL ejecutará automáticamente todos los scripts SQL o scripts de shell en este directorio cuando el contenedor se inicie por primera vez y la base de datos se inicialice.

data1sql

Su estructura no presenta cambios con respecto al archivo init.sql del Ejercicio 2. Sin embargo, fue necesario cambiar su nombre a data1.sql para asegurar que durante el proceso de inicialización de la base de datos este archivo se cargara primero que data2.sql (antes init2.sql).

data2.sql

Su estructura no presenta cambios con respecto al archivo init2.sql del Ejercicio 2. Sin embargo, fue necesario cambiar su nombre a data2.sql para asegurar que durante el proceso de inicialización de la base de datos este archivo se cargara después que data1.sql (antes init.sql).


Dockerfile (go)

No presenta cambios con respecto al Ejercicio 4, 4(a) y 4(b).

go.mod

El archivo `go.mod` de este Ejercicio establece que la versión utilizada de Go es la 1.21.5 y que el proyecto depende de la versión `v1.10.9` del driver `github.com/lib/pq` para conectar Go con bases de datos PostgreSQL.

1. Nombre del Módulo:
`module github.com/AntonioRubio/biblioteca`: Esta línea declara el nombre del módulo

2. Versión de Go:
`go 1.21.5`: Especifica que el proyecto utiliza la versión 1.21.5 de Go

3. Dependencias:
`require github.com/lib/pq v1.10.9`: Enumera las dependencias del proyecto. Aquí, el proyecto depende de `github.com/lib/pq` en la versión `v1.10.9`. El paquete `github.com/lib/pq` es un driver para conectar Go con bases de datos PostgreSQL

go.sum

El archivo `go.sum` proporciona una capa adicional de seguridad y confiabilidad en la gestión de dependencias al almacenar las sumas de comprobación de cada dependencia y su archivo `go.mod`. Esto ayuda a proteger el proyecto contra modificaciones maliciosas o errores involuntarios en las dependencias y es una parte crucial del sistema de módulos y dependencias de Go.

1. Sumas de Comprobación de la Dependencia:
Cada línea en el archivo `go.sum` representa la suma de comprobación (checksum) de una dependencia específica o de su archivo `go.mod`. Estas sumas de comprobación son utilizadas por Go para verificar que las dependencias descargadas no han sido alteradas o comprometidas

2. Entradas del Archivo:
•	`github.com/lib/pq v1.10.9 h1:YXG7RB+JIjhP29X+OtkiDnYaXQwpS4JEWq7dtCCRUEw=`: Esta línea es la suma de comprobación del código fuente del paquete `github.com/lib/pq` en la versión `v1.10.9`
•	`github.com/lib/pq v1.10.9/go.mod h1:AlVN5x4E4T544tWzH6hKfbfQvm3HdbOxrmggDNAPY9o=`: Esta línea es la suma de comprobación del archivo `go.mod` del mismo paquete y versión


server.go

Este script crea un servidor web en Go que interactúa con una base de datos PostgreSQL para manejar datos de una biblioteca, incluyendo el registro de usuarios, libros y préstamos. Utiliza plantillas HTML para mostrar las páginas y formularios, y procesa las solicitudes de los usuarios para realizar operaciones en la base de datos.

1. Importaciones:
Se importan los paquetes necesarios para la funcionalidad del servidor, incluyendo el manejo de HTTP, plantillas, base de datos y registro de errores. El paquete `github.com/lib/pq` es el driver de PostgreSQL para Go.

2. Conexión a la Base de Datos PostgreSQL:
Se establece una conexión con la base de datos PostgreSQL usando el paquete `database/sql`. La cadena de conexión incluye el usuario, la contraseña, el nombre de la base de datos, el host (postgres) y el puerto.

3. Servicio de Archivos Estáticos:
Se configura un manejador para servir archivos estáticos (CSS, JavaScript, imágenes) desde un directorio `static`.

4. Configuración de Plantillas:
Se prepara el sistema de plantillas para renderizar páginas HTML dinámicas. Las plantillas están almacenadas en el directorio `templates`.

5. Manejadores de Rutas: Se definen varios manejadores de ruta (`http.HandleFunc`) para diferentes endpoints:
•	La ruta raíz (`/`) sirve la página principal
•	`/formulario` maneja el formulario de registro de usuarios
•	`/libro` maneja el registro de libros
•	`/prestamo` maneja el registro de préstamos de libros
•	Cada ruta maneja solicitudes GET para mostrar formularios y solicitudes POST para procesar datos enviados

6. Operaciones de Base de Datos:
En las rutas POST, se recogen los datos del formulario y se ejecutan consultas SQL para insertarlos en la base de datos. Se utilizan marcadores de posición `$1`, `$2`, etc., para los parámetros en las consultas SQL.

7. Inicio del Servidor:
El servidor se inicia y escucha en el puerto 8080. Las solicitudes entrantes son manejadas por los manejadores de ruta definidos.

style,css

No presenta cambios con respecto al Ejercicio 3 y 3(a).

Imagen ‘Biblioteca’

No presenta cambios con respecto al Ejercicio 3 y 3(a).

script.js

No presenta cambios con respecto al Ejercicio 3 y 3(a).

index.html

No presenta cambios con respecto al Ejercicio 4, 4(a) y 4(b).

formulario.html

No presenta cambios con respecto al Ejercicio 4, 4(a) y 4(b).

libro.html

No presenta cambios con respecto al Ejercicio 4, 4(a) y 4(b).

prestamo.html

No presenta cambios con respecto al Ejercicio 4, 4(a) y 4(b).

