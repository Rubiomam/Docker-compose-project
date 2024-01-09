# Establecemos la imagen base con Python
FROM python:latest

# Establecemos el directorio de trabajo en el contenedor
WORKDIR /app

# Instalamos las dependencias de la aplicación
RUN pip install requests


# Copiamos el código fuente de la aplicación al contenedor
COPY client.py app/

# Declaramos el comando a ejecutar por defecto al lanzar el contenedor.
CMD ["python", "app/client.py"]