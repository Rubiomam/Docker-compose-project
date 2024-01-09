document.addEventListener('DOMContentLoaded', function() {
    // Crear un nuevo párrafo
    var nuevoParrafo = document.createElement('p');
    nuevoParrafo.textContent = 'Este es un contenido dinámico generado por JavaScript.';

    // Crear un botón
    var nuevoBoton = document.createElement('button');
    nuevoBoton.textContent = 'Haz clic aquí';
    
    // Función para el botón
    nuevoBoton.addEventListener('click', function() {
        alert('¡Gracias por tu visita!');
    });

    // Añadir el párrafo y el botón al cuerpo de la página
    document.body.appendChild(nuevoParrafo);
    document.body.appendChild(nuevoBoton);
});
