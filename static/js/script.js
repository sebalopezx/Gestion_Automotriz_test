// var toastElList = [].slice.call(document.querySelectorAll('.toast'))
// var toastList = toastElList.map(function (toastEl) {
//   return new bootstrap.Toast(toastEl, option)
// })

// tu_script_personalizado.js

// document.addEventListener("DOMContentLoaded", function () {
//     // Escucha cambios en el contenido del elemento con ID "messages"
//     const messagesElement = document.getElementById("messages");
//     if (messagesElement) {
//         console.log(messagesElement);
//       messagesElement.addEventListener("DOMSubtreeModified", function () {
//         const messages = document.querySelectorAll(".messages .alert");
//         messages.forEach(function (message) {
//           // Comprueba si el mensaje tiene la clase "alert-success" o "alert-danger"
//           if (message.classList.contains("alert-success")) {
//             // Si es un mensaje de éxito, muestra el toast de éxito
//             mostrarToast("success", message.innerText);
//           } else if (message.classList.contains("alert-danger")) {
//             // Si es un mensaje de error, muestra el toast de error
//             mostrarToast("danger", message.innerText);
//           }
//         });
//       });
//     }
//   });
  
//   function mostrarToast(variant, message) {
//     // Crea un elemento de toast de Bootstrap
//     const toast = document.createElement("div");
//     toast.classList.add("toast", `bg-${variant}`, "text-white");
//     toast.setAttribute("role", "alert");
//     toast.setAttribute("aria-live", "assertive");
//     toast.setAttribute("aria-atomic", "true");
  
//     // Contenido del toast
//     toast.innerHTML = `
//       <div class="toast-body">${message}</div>
//       <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast" aria-label="Close"></button>
//     `;
  
//     // Agrega el toast al cuerpo del documento
//     document.body.appendChild(toast);
  
//     // Muestra el toast
//     const bootstrapToast = new bootstrap.Toast(toast);
//     bootstrapToast.show();
  
//     // Elimina el toast después de que se cierre
//     toast.addEventListener("hidden.bs.toast", function () {
//       document.body.removeChild(toast);
//     });
//   }
  

// tu_script_personalizado.js
// document.addEventListener("DOMContentLoaded", function () {
//   const toast_message = document.getElementById("toast-message");

//   // Función para crear y mostrar un toast
//   function showToast(message, variant) {
//     // const toast = document.createElement("div");
//     // toast.classList.add("toast", `bg-${variant}`, "text-white");
//     // toast.setAttribute("role", "alert");
//     // toast.setAttribute("aria-live", "assertive");
//     // toast.setAttribute("aria-atomic", "true");

//     toast_message.innerHTML = `
//       <div class="toast-body sticky-bottom">
//           <button type="button" class="btn-close btn-close-white me-auto pb-2" data-bs-dismiss="toast" aria-label="Close"></button>
//           ${message}
//       </div>
//     `;

//     // toastContainer.appendChild(toast);

//     // Mostrar el toast
//     const bootstrapToast = new bootstrap.Toast(toast_message);
//     bootstrapToast.show();

//     // Eliminar el toast después de ocultarlo
//     // toast_message.addEventListener("hidden.bs.toast", function () {
//     //   toast_message.removeChild(toast_message);
//     // });
//   }

//   // Ejemplo: Mostrar un toast de éxito
//   const successMessage = "{{ success_message }}"//"Acción realizada con éxito.";
//   const errorMessage = "{{ error_message }}"//"Error no se ha realizado la acción.";
//   // const successMessage = "{{ success_message|default:'' }}";
//   // const errorMessage = "{{ error_message|default:'' }}";
//   if (successMessage !== "") {
//     console.log("Success Message:", successMessage);
//     console.log("Error Message:", errorMessage);

//     showToast(successMessage, "success");
//   } 
//   // else{
//   //     showToast(errorMessage, "danger");
//   // }

//   // Ejemplo: Mostrar un toast de error
//   // const errorMessage = "{{ error_message }}"; // Reemplaza con tu mensaje de error
//   else if (errorMessage) {
//     console.log("Success Message:", successMessage);
//     console.log("Error Message:", errorMessage);

//     showToast(errorMessage, "danger");
//   }
// });


document.addEventListener("DOMContentLoaded", function () {
    const toastContainer = document.getElementById("toast-container");

    // Función para crear y mostrar un toast
    function showToast(message, variant) {
      const toast = document.createElement("div");
      toast.classList.add("toast", `bg-${variant}`, "text-white");
      toast.setAttribute("role", "alert");
      toast.setAttribute("aria-live", "assertive");
      toast.setAttribute("aria-atomic", "true");

      toast.innerHTML = `
        <div class="toast-body sticky-bottom">
            <button type="button" class="btn-close btn-close-white me-auto pb-2" data-bs-dismiss="toast" aria-label="Close"></button>
            ${message}
        </div>
      `;

      toastContainer.appendChild(toast);

      // Mostrar el toast
      const bootstrapToast = new bootstrap.Toast(toast);
      bootstrapToast.show();

      // Eliminar el toast después de ocultarlo
      toast.addEventListener("hidden.bs.toast", function () {
        toastContainer.removeChild(toast);
      });
    }

    const messages = document.querySelectorAll(".message");
    messages.forEach(function (messageElement) {
      const messageText = messageElement.textContent.trim();
      const messageClass = messageElement.getAttribute("data-message-class");
      showToast(messageText, messageClass);
    });
});
  //   // Ejemplo: Mostrar un toast de éxito
  //   const successMessage = "{{ success_message }}"//"Acción realizada con éxito.";
  //   const errorMessage = "{{ error_message }}"//"Error no se ha realizado la acción.";
  //   // const successMessage = "{{ success_message|default:'' }}";
  //   // const errorMessage = "{{ error_message|default:'' }}";
  //   if (successMessage !== "") {
  //     console.log("Success Message:", successMessage);
  //     console.log("Error Message:", errorMessage);

  //     showToast(successMessage, "success");
  //   } 
  //   // else{
  //   //     showToast(errorMessage, "danger");
  //   // }

  //   // Ejemplo: Mostrar un toast de error
  //   // const errorMessage = "{{ error_message }}"; // Reemplaza con tu mensaje de error
  //   else if (errorMessage) {
  //     console.log("Success Message:", successMessage);
  //     console.log("Error Message:", errorMessage);

  //     showToast(errorMessage, "danger");
  //   }
  // });
  
// MOTOR DE BUSQUEDA

// const searchForm = document.querySelector('.search-patent');
// const searchInput = document.querySelector('#search-input');

// searchForm.addEventListener('submit', function(e){
//     e.preventDefault();

//     const search = searchInput.value;
//     console.log(search);
// })

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