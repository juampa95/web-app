document.addEventListener('DOMContentLoaded', () => {
    const checkboxElements = document.querySelectorAll('input[name="selected_ventas"]');
    const crearVentaButton = document.getElementById('crear-venta');
    const editarVentaButton = document.getElementById('editar-venta');
    const eliminarVentaButton = document.getElementById('eliminar-venta');

    checkboxElements.forEach(checkbox => {
        checkbox.addEventListener('change', () => {
            const checkedCheckboxes = document.querySelectorAll('input[name="selected_ventas"]:checked');
            editarVentaButton.disabled = checkedCheckboxes.length !== 1;
            eliminarVentaButton.disabled = checkedCheckboxes.length === 0;
        });
    });

    crearVentaButton.addEventListener('click', () => {
        window.location.href = "crear/";
    });

    editarVentaButton.addEventListener('click', () => {
        const checkedCheckbox = document.querySelector('input[name="selected_ventas"]:checked');
        if (checkedCheckbox) {
            const ventaId = checkedCheckbox.value;
            window.location.href = "editar/" + ventaId + "/";
        }
    });

    eliminarVentaButton.addEventListener('click', () => {
        const checkedCheckboxes = document.querySelectorAll('input[name="selected_ventas"]:checked');
        const ventaIds = Array.from(checkedCheckboxes).map(checkbox => checkbox.value);
        if (ventaIds.length > 0) {
            const confirmar = confirm("¿Estás seguro de que deseas eliminar las ventas seleccionadas?");
            if (confirmar) {
                ventaIds.forEach(ventaId => {
                    window.location.href = "eliminar/" + ventaId + "/";
                });
            }
        }
    });
});
