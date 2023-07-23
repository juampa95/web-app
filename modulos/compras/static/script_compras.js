document.addEventListener('DOMContentLoaded', () => {
  const formularioCompra = document.getElementById('formulario-compra');
  const productosContainer = document.getElementById('productos-container');
  const agregarProductoBtn = document.getElementById('agregar-producto-btn');

  agregarProductoBtn.addEventListener('click', () => {
    const productoRow = document.createElement('div');
    productoRow.classList.add('producto-row');

    const productoInput = document.createElement('input');
    productoInput.classList.add('producto-autocomplete');
    productoInput.name = 'producto';
    productoInput.required = true;

    const cantidadInput = document.createElement('input');
    cantidadInput.classList.add('cantidad');
    cantidadInput.type = 'number';
    cantidadInput.name = 'cantidad';
    cantidadInput.value = '1';
    cantidadInput.required = true;

    const precioInput = document.createElement('input');
    precioInput.classList.add('precio');
    precioInput.type = 'number';
    precioInput.step = '0.01';
    precioInput.name = 'precio';
    precioInput.required = true;

    productoRow.appendChild(document.createTextNode('Producto: '));
    productoRow.appendChild(productoInput);
    productoRow.appendChild(document.createTextNode(' Cantidad: '));
    productoRow.appendChild(cantidadInput);
    productoRow.appendChild(document.createTextNode(' Precio: '));
    productoRow.appendChild(precioInput);

    productosContainer.appendChild(productoRow);
  });

  formularioCompra.addEventListener('submit', (event) => {
    event.preventDefault();

    const numeroFactura = document.getElementById('numero_factura').value;
    const proveedorId = document.getElementById('proveedor_id').value;
    const fecha = document.getElementById('fecha').value;
    const productos = document.querySelectorAll('.producto-autocomplete');
    const cantidades = document.querySelectorAll('.cantidad');
    const precios = document.querySelectorAll('.precio');

    const productosData = [];
    for (let i = 0; i < productos.length; i++) {
      const producto = productos[i].value;
      const cantidad = cantidades[i].value;
      const precio = precios[i].value;
      productosData.push({ producto, cantidad, precio });
    }

    const data = {
      numero_factura: numeroFactura,
      proveedor_id: proveedorId,
      fecha: fecha,
      productos: productosData,
      csrfmiddlewaretoken: getCookie('csrftoken')
    };

    fetch('/compras/ingresar/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    })
      .then(response => response.json())
      .then(data => {
        window.location.href = `/compras/detalle/${data.compra_id}/`;
      })
      .catch(error => {
        console.error('Error al guardar la compra:', error);
      });
  });

  function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        // Does this cookie string begin with the name we want?
        if (cookie.substring(0, name.length + 1) === (name + '=')) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }
});
