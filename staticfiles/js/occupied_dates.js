
// $(function() {
//     var occupiedDates = {{ occupied_dates | safe }};
    
//     $('#id_date_register').datepicker({
//         // Configura las opciones del datepicker según tu necesidad
//         minDate: '+1d',
//         dateFormat: 'yy-mm-dd',
//         // Bloquea las fechas ocupadas
//         beforeShowDay: function(date) {
//             var dateString = $.datepicker.formatDate('yy-mm-dd', date);
//             return [occupiedDates.indexOf(dateString) == -1];
//         }
//     });
// });


document.addEventListener('DOMContentLoaded', function () {
    // Obtiene el campo de fecha por su ID
    var dateRegisterField = document.getElementById('id_date_register');
    
    // Obtiene las fechas ocupadas del atributo data-occupied-dates y las convierte en un array de JavaScript
    var occupiedDates = JSON.parse(dateRegisterField.getAttribute('data-occupied-dates'));

    // Agrega un evento de cambio al campo de fecha para bloquear las fechas ocupadas
    dateRegisterField.addEventListener('input', function () {
      var selectedDate = dateRegisterField.value;
      if (occupiedDates.includes(selectedDate)) {
        alert('Esta fecha ya está ocupada. Por favor, elige otra fecha.');
        dateRegisterField.value = ''; // Limpia el campo de fecha
      }
    });
  });