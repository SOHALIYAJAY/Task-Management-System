let total = 5;
let pending = 3;
let completed = 2;

function addTask() {
    const taskName = prompt("Enter task name:");
    if (!taskName) return;

    const table = document.getElementById("taskTable");

    const row = document.createElement("tr");
    row.innerHTML = `
        <td>${taskName}</td>
        <td>Low</td>
        <td class="pending">Pending</td>
    `;

    table.appendChild(row);

    total++;
    pending++;

    updateStats();
}

function updateStats() {
    document.getElementById("total").innerText = total;
    document.getElementById("pending").innerText = pending;
    document.getElementById("completed").innerText = completed;
}
