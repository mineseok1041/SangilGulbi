document.addEventListener("DOMContentLoaded", function () {
    const table = document.querySelector(".pointLog_table");
    const allRows = Array.from(document.querySelectorAll(".pointLog_table tbody tr"));
    const tableBody = table.querySelector("tbody");
    const filterIcon = document.querySelector(".filterIcon");
    const filterPopup = document.querySelector(".filterPopup");
    const resetFiltersButton = filterPopup.querySelector(".resetFilters");
    const checkboxes = filterPopup.querySelectorAll("input[type='checkbox']");
    const pointCancelButton = document.querySelector(".pointCancel");

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

    pointCancelButton.addEventListener("click", () => {
        const selectedRow = document.querySelector(".pointLog_table .selected-row");
    
        if (!selectedRow) {
            alert("취소할 로그를 선택해주세요");
            return;
        }
        
        const logNo = selectedRow.dataset.no;
        
        if (confirm("해당 상벌점 부여를 취소하시겠습니까?")) {
            fetch("/teacher/pointCancel.do", {
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

    // ---------- 사이드바 토글 및 외부 클릭 닫기 ----------
    const navToggle = document.querySelector('.nav-toggle');
    const sidebar = document.querySelector('.sidebar');

    if (navToggle && sidebar) {
        // 햄버거 버튼 클릭
        navToggle.addEventListener('click', function(e) {
            e.stopPropagation(); // 이벤트 전파 방지
            sidebar.classList.toggle('active');
            document.body.classList.toggle('sidebar-open', sidebar.classList.contains('active'));
        });

        // 사이드바 내부 클릭 시 이벤트 전파 방지
        sidebar.addEventListener('click', function(e) {
            e.stopPropagation();
        });

        // 문서 전체 클릭 시 사이드바 닫기
        document.addEventListener('click', function() {
        if (sidebar.classList.contains('active')) {
            sidebar.classList.remove('active');
            document.body.classList.remove('sidebar-open');
    }
        });

    }
});
