document.addEventListener("DOMContentLoaded", function () {
    const table = document.querySelector(".pointLog_table");
    const allRows = Array.from(document.querySelectorAll(".pointLog_table tbody tr"));
    const tableBody = table.querySelector("tbody");
    const filterIcon = document.querySelector(".filterIcon");
    const filterPopup = document.querySelector(".filterPopup");
    const resetFiltersButton = filterPopup.querySelector(".resetFilters");
    const checkboxes = filterPopup.querySelectorAll("input[type='checkbox']");

    // 날짜 형식 변경 (YYYY/MM/DD)
    allRows.forEach(row => {
        const cells = row.querySelectorAll("td");
        const dateCell = cells[3];
        if (dateCell) {
            const originalText = dateCell.textContent.trim();
            const match = originalText.match(/^(\d{4})(\d{2})(\d{2})/);
            if (match) {
                const [_, year, month, day] = match;
                dateCell.textContent = `${year}/${month}/${day}`;
            }
        }
    });

    // 드롭다운 토글
    document.querySelectorAll('.main-row').forEach(row => {
        row.addEventListener('click', () => {
            const dropdown = row.nextElementSibling;
            if (!dropdown || !dropdown.classList.contains('dropdown-row')) return;

            const isOpen = dropdown.style.display === 'table-row';

            document.querySelectorAll('.dropdown-row').forEach(r => r.style.display = 'none');
            if (!isOpen) {
                dropdown.style.display = 'table-row';
            }
        });
    });

    // 선택 강조
    allRows.forEach(row => {
        row.addEventListener("click", function (event) {
            event.stopPropagation();
            if (row.classList.contains("selected-row")) {
                row.classList.remove("selected-row");
            } else {
                allRows.forEach(r => r.classList.remove("selected-row"));
                row.classList.add("selected-row");
            }
        });
    });

    // 외부 클릭 시 선택 해제
    document.addEventListener("click", function (event) {
        if (!table.contains(event.target)) {
            allRows.forEach(row => row.classList.remove("selected-row"));
        }
    });

    // 필터 팝업 토글
    filterIcon.addEventListener("click", function (event) {
        event.stopPropagation();
        filterPopup.classList.toggle("hidden");
    });

    document.addEventListener("click", function (event) {
        if (!filterPopup.contains(event.target) && !filterIcon.contains(event.target)) {
            filterPopup.classList.add("hidden");
        }
    });

    // 필터 초기화
    resetFiltersButton.addEventListener("click", function () {
        checkboxes.forEach(checkbox => {
            checkbox.checked = false;
        });
        allRows.forEach(row => {
            row.style.display = "";
        });
    });
});
