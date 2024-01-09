# Establecemos la imagen base con PostgreSQL
FROM postgres:latest

# Establecemos variables de entorno para PostgreSQL
ENV POSTGRES_DB=biblioteca
ENV POSTGRES_USER=arubio
ENV POSTGRES_PASSWORD=ccJan2024

# Copiamos el script de SQL a la imagen
COPY data1.sql /docker-entrypoint-initdb.d/
COPY data2.sql /docker-entrypoint-initdb.d/