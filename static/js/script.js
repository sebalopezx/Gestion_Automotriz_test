// Generar OT y Checklist 

// function generateOT(id){
//     fetch("{% url 'generate_ot' date.id %}", {
//         method: 'POST',
//         headers: {
//             'X-CSRFToken': getCookie('csrftoken')
//         }
//     })
//     .then(response => response.json())
//     .then(data => {
//         alert("Trabajo generado exitosamente.");
//         // Puedes realizar acciones adicionales aquí si lo deseas
//     })
//     .catch(error => {
//         console.error("Error al generar el trabajo:", error);
//     });
// }

// // Función para obtener el token CSRF de las cookies
// function getCookie(name) {
//     var value = "; " + document.cookie;
//     var parts = value.split("; " + name + "=");
//     if (parts.length === 2) return parts.pop().split(";").shift();
// }


// function generateOT(id) {
//     console.log("id "+id)
//     const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

//     fetch(`/list_jobs/${id}/ot/`, {
//         method: 'POST',
//         headers: {
//             'X-CSRFToken': csrfToken
//         }
//     })
//     .then(response => {
//         if (response.ok) {
//             return response.json();
//         } else {
//             throw new Error('Error al generar OT.');
//         }
//     })
//     .then(data => {
//         // Manejar la respuesta exitosa aquí
//         console.log('Trabajo creado:', data);
//     })
//     .catch(error => {
//         // Manejar errores aquí
//         console.error('Error:', error);
//     });
// }
