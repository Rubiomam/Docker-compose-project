# Primera etapa: builder
# Utilizamos la imagen base oficial de Go para compilar nuestra aplicación
FROM golang:latest AS builder

# Establecemos el directorio de trabajo en el contenedor
WORKDIR /app

# Copiamos go.mod
COPY go.mod ./

# Copiamos los archivos de código fuente de la aplicación al contenedor
COPY . .

# Compilamos la aplicación.
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o client client.go

# Segunda etapa: Creamos una imagen ligera desde cero
FROM scratch

# Copiamos el ejecutable desde la primera etapa
COPY --from=builder /app/client .

# Comando para ejecutar la aplicación
CMD ["./client"]