document.getElementById("taskForm").addEventListener("submit", function (e) {
    e.preventDefault();

    const title = document.getElementById("title").value.trim();
    const priority = document.getElementById("priority").value;
    const errorMsg = document.getElementById("errorMsg");

    if (title === "") {
        errorMsg.textContent = "Task title is required.";
        return;
    }

    if (priority === "") {
        errorMsg.textContent = "Please select task priority.";
        return;
    }

    errorMsg.textContent = "";

    alert("Task created successfully ✅");

    // Reset form
    this.reset();
});
