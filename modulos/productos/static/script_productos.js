document.addEventListener('DOMContentLoaded', () => {
    const checkboxElements = document.querySelectorAll('input[name="selected_items"]');

    checkboxElements.forEach(checkbox => {
        checkbox.addEventListener('change', () => {
            const checkedCheckboxes = document.querySelectorAll('input[name="selected_items"]:checked');
            editarProductoButton.disabled = checkedCheckboxes.length !== 1;
            eliminarProductoButton.disabled = checkedCheckboxes.length === 0;
        });
    });

    const crearProductoButton = document.getElementById('crear-producto');
    crearProductoButton.addEventListener('click', () => {
        window.location.href = "crear/";
    });

    const editarProductoButton = document.getElementById('editar-producto');
    editarProductoButton.addEventListener('click', () => {
        const checkedCheckbox = document.querySelector('input[name="selected_items"]:checked');
        if (checkedCheckbox) {
            const productId = checkedCheckbox.value;
            window.location.href = `editar/${productId}/`;
        }
    });

    const eliminarProductoButton = document.getElementById('eliminar-producto');
    eliminarProductoButton.addEventListener('click', () => {
        const checkedCheckboxes = document.querySelectorAll('input[name="selected_items"]:checked');
        const productIds = Array.from(checkedCheckboxes).map(checkbox => checkbox.value);
        if (productIds.length > 0) {
            const confirmar = confirm("¿Estás seguro de que deseas eliminar los productos seleccionados?");
            if (confirmar) {
                productIds.forEach(productId => {
                    window.location.href = `eliminar/${productId}/`;
                });
            }
        }
    });
});
