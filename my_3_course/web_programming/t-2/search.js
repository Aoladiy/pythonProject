function searchTable(inputId, tableId, columnIndex) {
    const input = document.getElementById(inputId);
    const filter = input.value.toUpperCase();
    const table = document.getElementById(tableId);
    const tbody = table.querySelector("tbody");
    const rows = tbody.getElementsByTagName("tr");

    for (let i = 0; i < rows.length; i++) {
        const cell = rows[i].getElementsByTagName("td")[columnIndex];
        if (cell) {
            const textValue = cell.textContent || cell.innerText;
            if (textValue.toUpperCase().indexOf(filter) > -1) {
                rows[i].style.display = "";
            } else {
                rows[i].style.display = "none";
            }
        }
    }
}

function searchTableGlobal(inputId, tableId) {
    const input = document.getElementById(inputId);
    const filter = input.value.toUpperCase();
    const table = document.getElementById(tableId);
    const rows = table.querySelectorAll("tbody tr");

    rows.forEach((row) => {
        const cells = row.querySelectorAll("td");
        let rowVisible = false;

        cells.forEach((cell) => {
            const textValue = cell.textContent || cell.innerText;
            if (textValue.toUpperCase().indexOf(filter) > -1) {
                rowVisible = true;
            }
        });

        if (rowVisible) {
            row.style.display = "";
        } else {
            row.style.display = "none";
        }
    });
}

document.getElementById("toggleName").addEventListener("change", function () {
    toggleColumn(0);
});

document.getElementById("toggleEmail").addEventListener("change", function () {
    toggleColumn(1);
});

document.getElementById("toggleGroup").addEventListener("change", function () {
    toggleColumn(2);
});

function toggleColumn(columnIndex) {
    const table = document.getElementById("dataTable");
    const headerRow = table.querySelector("thead tr");
    const rows = table.querySelectorAll("tbody tr");
    const isColumnVisible = !headerRow.querySelectorAll("th")[columnIndex].classList.contains("hidden");

    // Скрываем или отображаем заголовок колонки
    headerRow.querySelectorAll("th")[columnIndex].classList.toggle("hidden", isColumnVisible);

    // Скрываем или отображаем данные в колонке
    rows.forEach((row) => {
        const cells = row.querySelectorAll("td");
        cells[columnIndex].classList.toggle("hidden", isColumnVisible);
    });
}