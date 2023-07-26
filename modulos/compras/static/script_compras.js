document.addEventListener('DOMContentLoaded', () => {
  const agregarProductoBtn = document.getElementById('agregar-producto-btn');
  const guardarCompraBtn = document.getElementById('guardar-compra-btn');
  const productosSelect = document.getElementById('productos-select');
  const cantidadInput = document.getElementById('cantidad-input');
  const precioInput = document.getElementById('precio-input');
  const productosAgregados = document.getElementById('productos-agregados');


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

  guardarCompraBtn.addEventListener('click', (e) => {
    e.preventDefault()
    // Validar que se haya agregado al menos un detalle de compra
    if (detallesCompra.length > 0) {
      // Crear un objeto con los datos de la compra y los detalles de compra
      const data = {
        numero_factura: document.getElementById('numero_factura').value,
        proveedor_id: document.getElementById('proveedor_id').value,
        fecha: document.getElementById('fecha').value,
        detalles: detallesCompra
      };

      const url = window.location.origin + '/compras/guardar/';
      const csrftoken = getCookie('csrftoken'); // Implementa la función getCookie para obtener el valor del token CSRF desde las cookies


      // Enviar la petición fetch al servidor
      fetch(url, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify(data)
      })
        .then(response => response.json())
        .then(data => {
          // Mostrar un mensaje de éxito
          alert('Compra guardada exitosamente');

          // Limpiar la lista de detalles de compra
          detallesCompra = [];
          mostrarDetallesCompra();

          // Limpiar los campos del formulario de compra
          document.getElementById('numero_factura').value = '';
          document.getElementById('proveedor_id').value = '';
          document.getElementById('fecha').value = '';

          // Redirigir a la página de detalle de la compra guardada
          window.location.href = `/compras/detalle_items_factura/${data.compra_id}`;

          console.log(data);
        })
        .catch(error => {
          console.error('Error al guardar la compra:', error);
        });
    } else {
      alert('Agrega al menos un producto antes de guardar la compra.');
    }
  });


  // Función para mostrar los detalles de compra en la tabla
  function mostrarDetallesCompra() {
    productosAgregados.innerHTML = '';

    detallesCompra.forEach(detalle => {
      const tr = document.createElement('tr');
      tr.innerHTML = `
        <td>${detalle.producto_id}</td>
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