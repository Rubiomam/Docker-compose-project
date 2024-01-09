import requests
import logging as log

log.basicConfig(level=log.INFO)

# URL del servidor Node.js
server_url = 'http://servidor:5000'

def send_request():
    # Enviamos una solicitud de prueba al servidor Node.js
    log.info("Enviando una solicitud de prueba al servidor")
    response = requests.get(f'{server_url}/')
    log.info("Respuesta del servidor: %s", response.text)

if __name__ == '__main__':
    # Enviamos una solicitud de prueba
    send_request()