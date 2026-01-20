document.querySelector("form").addEventListener("submit", function (e) {
    const inputs = this.querySelectorAll("input");
    let isValid = true;

    inputs.forEach(input => {
        if (input.value.trim() === "") {
            input.style.borderColor = "#DC2626";
            isValid = false;
        } else {
            input.style.borderColor = "#D1D5DB";
        }
    });

    if (!isValid) {
        e.preventDefault();
        alert("Please fill all required fields.");
    }
});
