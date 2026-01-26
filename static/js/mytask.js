function filterTasks(status) {
    const rows = document.querySelectorAll(".task-row");
    const buttons = document.querySelectorAll(".filters button");

    buttons.forEach(btn => btn.classList.remove("active"));
    // event.target.classList.add("active");

    rows.forEach(row => {
        if (status === "all" || row.dataset.status === status) {
            row.style.display = "grid";
        } else {
            row.style.display = "none";
        }
    });
}


/* STATUS TOGGLE (UI ONLY) */
function toggleStatus(btn) {
    if (btn.innerText === "Pending") {
        btn.innerText = "Completed";
        btn.classList.remove("pending");
        btn.classList.add("completed");
        btn.closest(".task-row").dataset.status = "Completed";
    } else {
        btn.innerText = "Pending";
        btn.classList.remove("completed");
        btn.classList.add("pending");
        btn.closest(".task-row").dataset.status = "Pending";
    }
}

/* SEARCH */
document.getElementById("searchInput").addEventListener("input", function () {
    const value = this.value.toLowerCase();
    document.querySelectorAll(".task-row").forEach(row => {
        row.style.display = row.dataset.title.includes(value)
            ? "grid"
            : "none";
    });
});
