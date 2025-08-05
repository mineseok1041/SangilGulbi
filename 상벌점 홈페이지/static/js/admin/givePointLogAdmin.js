document.addEventListener("DOMContentLoaded", function () {
    const table = document.querySelector(".pointLog_table");
    const allRows = Array.from(document.querySelectorAll(".pointLog_table tbody tr"));
    const filterIcon = document.querySelector(".filterIcon");
    const filterPopup = document.querySelector(".filterPopup");
    const headers = document.querySelectorAll(".pointLog_table thead th.sortable");
    const resetFiltersButton = filterPopup.querySelector(".resetFilters");
    const checkboxes = filterPopup.querySelectorAll("input[type='checkbox']");
    const pointCancelButton = document.querySelector(".pointCancel");

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

    pointCancelButton.addEventListener("click", () => {
        const selectedRow = document.querySelector(".pointLog_table .selected-row");
    
        if (!selectedRow) {
            alert("취소할 로그를 선택해주세요");
            return;
        }
        
        const logNo = selectedRow.dataset.no;
        
        if (confirm("상벌점 부여 취소? : " + logNo)) {
            fetch("/admin/pointCancel.do", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ no: logNo })
            })
            .then(res => res.json())
            .then(data => {
                if (data.success) {
                    alert("점수 부여가 취소되었습니다.");
                    location.reload();
                } else {
                    alert(data.error || "취소 중 오류가 발생했습니다.");
                }
            })
            .catch(() => alert("취소 요청 중 오류가 발생했습니다."));
        }
    });
    document.querySelector('.nav-toggle').addEventListener('click', function() {
    document.querySelector('.sidebar').classList.toggle('active');
});
});
