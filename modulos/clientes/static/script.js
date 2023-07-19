document.addEventListener('DOMContentLoaded', () => {
    const checkboxElements = document.querySelectorAll('input[name="selected_clientes"]');

    checkboxElements.forEach(checkbox => {
        checkbox.addEventListener('change', () => {
            const checkedCheckboxes = document.querySelectorAll('input[name="selected_clientes"]:checked');
            editarClienteButton.disabled = checkedCheckboxes.length !== 1;
            eliminarClienteButton.disabled = checkedCheckboxes.length === 0;
        });
    });

    const crearClienteButton = document.getElementById('crear-cliente');
    crearClienteButton.addEventListener('click', () => {
        window.location.href = "crear/";
    });

    const editarClienteButton = document.getElementById('editar-cliente');
    editarClienteButton.addEventListener('click', () => {
        const checkedCheckbox = document.querySelector('input[name="selected_clientes"]:checked');
        if (checkedCheckbox) {
            const clienteId = checkedCheckbox.value;
            window.location.href = `editar/${clienteId}/`;
        }
    });

    const eliminarClienteButton = document.getElementById('eliminar-cliente');
    eliminarClienteButton.addEventListener('click', () => {
        const checkedCheckboxes = document.querySelectorAll('input[name="selected_clientes"]:checked');
        const clienteIds = Array.from(checkedCheckboxes).map(checkbox => checkbox.value);
        if (clienteIds.length > 0) {
            const confirmar = confirm("¿Estás seguro de que deseas eliminar los clientes seleccionados?");
            if (confirmar) {
                clienteIds.forEach(clienteId => {
                    window.location.href = `eliminar/${clienteId}/`;
                });
            }
        }
    });
});