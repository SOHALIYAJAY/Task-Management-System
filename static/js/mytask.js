function filterTasks(status, btn) {
    const rows = document.querySelectorAll(".task-row");
    const buttons = document.querySelectorAll(".filters button");

    buttons.forEach(b => b.classList.remove("active"));
    btn.classList.add("active");

    rows.forEach(row => {
        if (status === "all" || row.dataset.status === status) {
            row.style.display = "flex";
        } else {
            row.style.display = "none";
        }
    });
}

/* SEARCH */
document.getElementById("searchInput").addEventListener("input", function () {
    const value = this.value.toLowerCase();
    document.querySelectorAll(".task-row").forEach(row => {
        row.style.display = row.dataset.title.includes(value)
            ? "flex"
            : "none";
    });
});
