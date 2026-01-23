function completeTask() {
    const status = document.getElementById("taskStatus");
    status.innerText = "Completed";
    status.classList.remove("pending");
    status.classList.add("completed");

    alert("Task marked as completed!");
}

function goBack() {
    window.history.back();
}
