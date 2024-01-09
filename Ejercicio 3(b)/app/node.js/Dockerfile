# Establecemos la imagen base con Node.js
FROM node:latest

# Establecemos el directorio de trabajo en el contenedor
WORKDIR /node_app

# Copiamos el archivo package.json y package-lock.json
COPY package*.json ./

# Instalamos las dependencias de la aplicación
RUN npm install

# Copiamos el código fuente de la aplicación al contenedor
COPY . .

# Exponemos el puerto que usará la aplicación
EXPOSE 5000

# Finalmente, declaramos el comando a ejecutar por defecto al lanzar el contenedor
CMD ["node", "server.js"]