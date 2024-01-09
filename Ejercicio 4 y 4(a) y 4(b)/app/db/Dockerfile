FROM mysql:latest

# Establecemos variables de entorno para MySQL
ENV MYSQL_DATABASE=biblioteca
ENV MYSQL_ROOT_PASSWORD=ccDec2023
ENV MYSQL_USER=arubio
ENV MYSQL_PASSWORD=ccJan2024

# Copiamos el script de SQL a la imagen
COPY init.sql /docker-entrypoint-initdb.d/
COPY init2.sql /docker-entrypoint-initdb.d/