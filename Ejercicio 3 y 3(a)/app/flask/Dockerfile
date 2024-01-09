# Establecemos la imagen base con Python
FROM python:latest

# Establecemos el directorio de trabajo en el contenedor
WORKDIR /flask

# Instalamos las dependencias de la aplicación
RUN pip install Flask mysql-connector-python

# Copiamos el código fuente de la aplicación al contenedor
COPY server.py flask/

# Exponemos el puerto 5000 para Flask
# Esto no abre el puerto, simplemente es una forma de documentación,
# Explica que el puerto está abierto.
EXPOSE 5000

# Declaramos el comando a ejecutar por defecto al lanzar el contenedor
CMD ["python", "server.py"]