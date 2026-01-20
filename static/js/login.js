document.addEventListener("DOMContentLoaded", function () {

    const form = document.querySelector("form");

    form.addEventListener("submit", function (e) {

        const inputs = form.querySelectorAll("input");
        let isValid = true;

        inputs.forEach(input => {
            if (input.value.trim() === "") {
                isValid = false;
                input.style.border = "1px solid red";
            } else {
                input.style.border = "1px solid #ccc";
            }
        });

        if (!isValid) {
            e.preventDefault();
            alert("Please fill all required fields");
        }
    });
});
