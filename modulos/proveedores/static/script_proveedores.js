document.addEventListener('DOMContentLoaded', () => {
    const checkboxElements = document.querySelectorAll('input[name="selected_proveedores"]');

    checkboxElements.forEach(checkbox => {
        checkbox.addEventListener('change', () => {
            const checkedCheckboxes = document.querySelectorAll('input[name="selected_proveedores"]:checked');
            editarProveedorButton.disabled = checkedCheckboxes.length !== 1;
            eliminarProveedorButton.disabled = checkedCheckboxes.length === 0;
        });
    });

    const crearProveedorButton = document.getElementById('crear-proveedor');
    crearProveedorButton.addEventListener('click', () => {
        window.location.href = "crear/";
    });

    const editarProveedorButton = document.getElementById('editar-proveedor');
    editarProveedorButton.addEventListener('click', () => {
        const checkedCheckbox = document.querySelector('input[name="selected_proveedores"]:checked');
        if (checkedCheckbox) {
            const proveedorId = checkedCheckbox.value;
            window.location.href = `editar/${proveedorId}/`;
        }
    });

    const eliminarProveedorButton = document.getElementById('eliminar-proveedor');
    eliminarProveedorButton.addEventListener('click', () => {
        const checkedCheckboxes = document.querySelectorAll('input[name="selected_proveedores"]:checked');
        const proveedorIds = Array.from(checkedCheckboxes).map(checkbox => checkbox.value);
        if (proveedorIds.length > 0) {
            const confirmar = confirm("¿Estás seguro de que deseas eliminar los proveedores seleccionados?");
            if (confirmar) {
                proveedorIds.forEach(proveedorId => {
                    window.location.href = `eliminar/${proveedorId}/`;
                });
            }
        }
    });
});
