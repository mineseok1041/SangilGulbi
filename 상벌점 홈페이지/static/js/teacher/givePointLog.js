document.addEventListener("DOMContentLoaded", function () {
    const table = document.querySelector(".pointLog_table");
    // main-row 클래스가 붙은 행만 가져오기 (dropdown-row 등 제외)
    const tableRows = Array.from(document.querySelectorAll(".pointLog_table tbody tr.main-row"));
    const tableBody = table.querySelector("tbody");
    const headers = document.querySelectorAll(".pointLog_table thead th.sortable");
    const filterIcon = document.querySelector(".filterIcon");
    const filterPopup = document.querySelector(".filterPopup");
    const resetFiltersButton = filterPopup ? filterPopup.querySelector(".resetFilters") : null;
    const checkboxes = filterPopup.querySelectorAll("input[type='checkbox']");

    // 방어적으로 셀 텍스트 가져오기 함수
    function getCellText(row, index) {
        const cell = row.querySelector(`td:nth-child(${index})`);
        return cell ? cell.textContent.trim() : "";
    }

    // dropdown toggle 이벤트 (main-row만)
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

    // 행 클릭 이벤트 (main-row만)
    tableRows.forEach(row => {
        row.addEventListener("click", function (event) {
            event.stopPropagation();

            if (row.classList.contains("selected-row")) {
                row.classList.remove("selected-row");
            } else {
                tableRows.forEach(r => r.classList.remove("selected-row"));
                row.classList.add("selected-row");
            }
        });
    });

    // 기본 정렬 (최신순) - 4번째 셀 날짜 기준
    const sortedRows = tableRows.sort((a, b) => {
        const aDateText = getCellText(a, 4);
        const bDateText = getCellText(b, 4);
        const aDate = aDateText ? new Date(aDateText) : new Date(0);
        const bDate = bDateText ? new Date(bDateText) : new Date(0);
        return bDate - aDate;
    });

    tableBody.innerHTML = "";
    sortedRows.forEach(row => tableBody.appendChild(row));

    // 테이블 외부 클릭 시 선택 해제
    document.addEventListener("click", function (event) {
        if (!table.contains(event.target)) {
            tableRows.forEach(row => row.classList.remove("selected-row"));
            selectedStudent = null;
        }
    });

    // 필터 아이콘 클릭 토글
    if (filterIcon && filterPopup) {
        filterIcon.addEventListener("click", function () {
            filterPopup.classList.toggle("hidden");
        });
    }

    // 초기화 버튼 클릭 이벤트
    if (resetFiltersButton) {
        resetFiltersButton.addEventListener("click", function () {
            const checkboxes = filterPopup.querySelectorAll("input[type='checkbox']");
            checkboxes.forEach(checkbox => {
                checkbox.checked = false;
            });
            tableRows.forEach(row => {
                row.style.display = "";
            });
        });
    }

    // 팝업 외부 클릭 시 팝업 닫기
    document.addEventListener("click", function (event) {
        if (filterPopup && !filterPopup.contains(event.target) && !filterIcon.contains(event.target)) {
            filterPopup.classList.add("hidden");
        }
    });

    // 헤더 정렬 기능
    headers.forEach(header => {
        header.addEventListener("click", function (event) {
            const columnIndex = parseInt(header.getAttribute("data-column"), 10);
            if (isNaN(columnIndex)) return;

            const isAscending = header.classList.contains("asc");
            const direction = isAscending ? -1 : 1;

            headers.forEach(h => h.classList.remove("asc", "desc"));
            header.classList.add(isAscending ? "desc" : "asc");

            const sortedRows = tableRows.sort((a, b) => {
                const aText = getCellText(a, columnIndex);
                const bText = getCellText(b, columnIndex);

                switch (columnIndex) {
                    case 1: // 학번 - 숫자
                        return (parseInt(aText, 10) - parseInt(bText, 10)) * direction;
                    case 2: // 이름 - 텍스트
                    case 3: // 사유 - 텍스트
                    case 6: // 부여자 - 텍스트
                        return aText.localeCompare(bText) * direction;
                    case 4: // 부여시각 - 날짜
                        return (new Date(aText) - new Date(bText)) * direction;
                    case 5: // 부여점수 - 숫자
                        const aValue = parseFloat(aText.replace("+", "")) || 0;
                        const bValue = parseFloat(bText.replace("+", "")) || 0;
                        return (aValue - bValue) * direction;
                    default:
                        return aText.localeCompare(bText) * direction;
                }
            });

            tableBody.innerHTML = "";
            sortedRows.forEach(row => tableBody.appendChild(row));
        });
    });

    // 날짜 셀 포맷 변경 (.date-cell 클래스 대상)
    const dateCells = document.querySelectorAll('.date-cell');
    dateCells.forEach(cell => {
        const originalText = cell.textContent.trim();
        const datePart = originalText.split(' ')[0];
        if (datePart.length === 8) {
            const formattedDate = `${datePart.slice(0, 4)}/${datePart.slice(4, 6)}/${datePart.slice(6, 8)}`;
            cell.textContent = formattedDate;
        }
    });
});
