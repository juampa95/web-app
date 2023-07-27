document.addEventListener('DOMContentLoaded', () => {
  const agregarProductoBtn = document.getElementById('agregar-producto-btn');
  const guardarCompraBtn = document.getElementById('guardar-compra-btn');
  const productosSelect = document.getElementById('productos-select');
  const cantidadInput = document.getElementById('cantidad-input');
  const precioInput = document.getElementById('precio-input');
  const productosAgregados = document.getElementById('productos-agregados');
  const numeroFacturaInput = document.getElementById('numero_factura');
  const proveedorSelect = document.getElementById('proveedor_id');
  const fechaInput = document.getElementById('fecha');


  // Array para almacenar los detalles de compra
  let detallesCompra = [];

  agregarProductoBtn.addEventListener('click', () => {
    console.log('Botón "Agregar Item" clickeado');

    // Obtener los valores de los inputs
    const productoId = productosSelect.value;
    const cantidad = cantidadInput.value;
    const precio = precioInput.value;

    // Validar que los campos no estén vacíos
    if (productoId && cantidad && precio) {
      // Agregar el detalle de compra al array
      detallesCompra.push({ item_id: productoId, cantidad: cantidad, precio: precio });

      // Limpiar los inputs para el siguiente producto
      productosSelect.value = '';
      cantidadInput.value = '1';
      precioInput.value = '';

      // Mostrar los detalles de compra en la tabla
      mostrarDetallesCompra();
    }
  });

  // Función para enviar los detalles de compra al servidor
  function guardarCompra() {
    // Obtener el token CSRF
    const csrfToken = getCookie('csrftoken');

    // Obtener los detalles de compra almacenados en el array
    const detalles = detallesCompra;

    // Crear un objeto que contiene los datos a enviar al servidor
    const data = {
      numero_factura: numeroFacturaInput.value,
      proveedor_id: proveedorSelect.value,
      fecha: fechaInput.value,
      detalles: detalles,
    };

    // Realizar una solicitud POST al servidor para guardar la compra
    fetch('/compras/guardar/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrfToken,
      },
      body: JSON.stringify(data), // Convertir el objeto 'data' a una cadena JSON
    })
      .then(response => response.json())
      .then(data => {
        // Aquí puedes manejar la respuesta del servidor si es necesario
        console.log(data);
      })
      .catch(error => {
        // En caso de error, muestra el mensaje de error en la consola
        console.error('Error al guardar la compra:', error);
      });
  }
  guardarCompraBtn.addEventListener('click', guardarCompra);


  // Función para mostrar los detalles de compra en la tabla
  function mostrarDetallesCompra() {
    productosAgregados.innerHTML = '';

    detallesCompra.forEach(detalle => {
      const tr = document.createElement('tr');
      tr.innerHTML = `
        <td>${detalle.item_id}</td>
        <td>${detalle.cantidad}</td>
        <td>${detalle.precio}</td>
      `;
      productosAgregados.appendChild(tr);
    });
  }
});
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Buscar el nombre de la cookie y obtener su valor
      if (cookie.substring(0, name.length + 1) === `${name}=`) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}