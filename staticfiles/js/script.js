// LINK CON CLASE ACTIVE PARA MARCAR POSICION

// Obtenemos la URL actual
// let currentURL = window.location.href;

// // Obtenemos todos los enlaces de navegación
// let navLinks = document.querySelectorAll(".nav-link");

// // Iteramos sobre los enlaces
// for (var i = 0; i < navLinks.length; i++) {
//     let link = navLinks[i];

//     // Verificamos si el href del enlace coincide con la URL actual
//     if (link.href === currentURL) {
//         // Agregamos la clase "active" al enlace
//         link.classList.add("active");
//     };
// };

// document.addEventListener('DOMContentLoaded', function () {
//     const navLinks = document.querySelectorAll('.nav-link');
//     console.log(navLinks);

//     navLinks.forEach(function (link) {
//         link.addEventListener('click', function () {
//             navLinks.forEach(function (navLink) {
//                 navLink.classList.remove('active'); // Elimina la clase 'active' de todos los enlaces
//             });
//             this.classList.add('active'); // Agrega la clase 'active' al enlace clicado
//         });
//     });
// });

// document.addEventListener('DOMContentLoaded', function () {
//     const navLinks = document.querySelectorAll('.nav-link');
//     const currentUrl = "{{ current_url }}"; // Obtén la URL actual de Django

//     navLinks.forEach(function (link) {
//         const linkUrl = link.getAttribute('href'); // Obtiene la URL del enlace

//         if (currentUrl.startsWith(linkUrl)) {
//             link.classList.add('active');
//         }
//     });
// });

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



// document.addEventListener('DOMContentLoaded', function() {
//     var selectAllCheckbox = document.querySelector('.select-all');
//     var checkboxes = document.querySelectorAll('input[type="checkbox"]:not(.select-all)');

//     selectAllCheckbox.addEventListener('change', function() {
//         checkboxes.forEach(function(checkbox) {
//             checkbox.checked = selectAllCheckbox.checked;
//         });
//     });
// });



 // Espera a que se cargue completamente la página
//  document.addEventListener('DOMContentLoaded', function() {
//     // Encuentra el formulario por su ID
//     const updateJobForm = document.getElementById('updateJobForm');

//     // Agrega un manejador de eventos para el evento 'submit' del formulario
//     updateJobForm.addEventListener('submit', function(event) {
//         // Encuentra el campo de selección de servicios por su nombre
//         const serviceField = document.getElementsByName('service');

//         // Restablece el campo de selección de servicios deseleccionando todos los elementos
//         serviceField.forEach(function(checkbox) {
//             checkbox.checked = false;
//         });
//     });
// });


// document.addEventListener("DOMContentLoaded", function() {
//     function generate_discount(total_price){
//         console.log("ingresando descuento")
//         console.log("Valor total_price:", total_price);
//         const element = document.getElementById('descuento');
//         const discount = 0.90;
//         const discounted_price = total_price*discount
//         const formatted_price = discounted_price.toLocaleString('es-CL', {
//             style: 'currency',
//             currency: 'CLP'
//         });
//         console.log("Valor total_price:", formatted_price);
        
//         element.innerHTML = `Precio con descuento: ${formatted_price} pesos.`;
//         // return total_price*discount
//     };
// });

// document.addEventListener("DOMContentLoaded", function() {
//     const discountButton = document.getElementById('btnDiscount'); 


//     // Obtener el precio total desde el atributo data
//     const total_price = parseFloat(discountButton.getAttribute('data-total-price'));

//     // Agregar un event listener al botón
//     discountButton.addEventListener('click', function() {
//         const element = document.getElementById('discount');
//         const discount = 0.90;

//         if (!isNaN(total_price)) {
//             const discounted_price = total_price * discount;
//             const formatted_price = discounted_price.toLocaleString('es-CL', {
//                 style: 'currency',
//                 currency: 'CLP'
//             });

//             element.innerHTML = `Precio con descuento: ${formatted_price} pesos.`;
//         } else {
//             alert('El precio total no es válido.');
//         }
//     });
// });