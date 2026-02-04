function toggleEdit() {
    const inputs = document.querySelectorAll(
        '#profileForm input, #profileForm textarea'
    );

    inputs.forEach(input => {
        input.readOnly = false;
        input.disabled = false;
        input.classList.add('editable');
    });
}