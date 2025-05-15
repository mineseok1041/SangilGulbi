document.addEventListener("DOMContentLoaded", function () {
    const table = document.querySelector(".log_table");
    const tableRows = Array.from(document.querySelectorAll(".log_table tbody tr")); // 테이블의 모든 행 가져오기
    const tableBody = table.querySelector(".log_table tbody");
    const headers = document.querySelectorAll(".log_table thead th.sortable");
    const dateCells = document.querySelectorAll('.logDate');
    // const filterIcon = document.querySelector(".filterIcon"); // 필터 아이콘
    // const filterPopup = document.querySelector(".filterPopup"); // 필터 팝업
    // const resetFiltersButton = filterPopup.querySelector(".resetFilters");

    // 행 클릭 이벤트 추가
    tableRows.forEach(row => {
        row.addEventListener("click", function (event) {
            event.stopPropagation(); // 클릭 이벤트가 상위 요소로 전파되지 않도록 방지

            // 이미 선택된 행을 다시 클릭하면 선택 해제
            if (row.classList.contains("selected-row")) {
                row.classList.remove("selected-row");
            } else {
                // 다른 행의 선택 해제
                tableRows.forEach(r => r.classList.remove("selected-row"));
                // 현재 행에 선택 클래스 추가
                row.classList.add("selected-row");
            }
        });
    });

    // 페이지 로드 시 기본 정렬 (최신순)
    const sortedRows = tableRows.sort((a, b) => {
        const aDate = new Date(a.querySelector("td:nth-child(4)").textContent.trim()); // 날짜 열
        const bDate = new Date(b.querySelector("td:nth-child(4)").textContent.trim());
        return bDate - aDate; // 최신순 정렬
    });

    // 정렬된 행을 테이블에 추가
    tableBody.innerHTML = "";
    sortedRows.forEach(row => tableBody.appendChild(row));

    // 테이블 외부 클릭 시 선택 해제
    document.addEventListener("click", function (event) {
        if (!table.contains(event.target)) {
            tableRows.forEach(row => row.classList.remove("selected-row"));
        }
    });

    // // 필터 아이콘 클릭 이벤트
    // filterIcon.addEventListener("click", function () {
    //     filterPopup.classList.toggle("hidden"); // 팝업 메뉴 표시/숨김
    //     if (!filterPopup.contains(event.target) && !filterIcon.contains(event.target)) {
    //         filterPopup.classList.add("hidden"); // 필터 팝업 닫기
    //     }
    // });

    // // 팝업 외부 클릭 시 팝업 닫기
    // document.addEventListener("click", function (event) {
    //     if (!filterPopup.contains(event.target) && !filterIcon.contains(event.target)) {
    //         filterPopup.classList.add("hidden");
    //     }
    // });

    // // 초기화 버튼 클릭 이벤트
    // resetFiltersButton.addEventListener("click", function () {
    //     // 모든 체크박스 해제
    //     checkboxes.forEach(checkbox => {
    //         checkbox.checked = false;
    //     });

    //     // 테이블의 모든 행 표시
    //     tableRows.forEach(row => {
    //         row.style.display = ""; // 모든 행 표시
    //     });
    // });

    // 정렬 기능 추가
    headers.forEach(header => {
    header.addEventListener("click", function (event) {
        const columnIndex = header.getAttribute("data-column") - 1; // 열 인덱스 가져오기
        const isAscending = header.classList.contains("asc"); // 현재 정렬 상태 확인
        const direction = isAscending ? -1 : 1; // 정렬 방향 설정

        // 모든 헤더에서 정렬 클래스 제거
        headers.forEach(h => h.classList.remove("asc", "desc"));

        // 현재 헤더에 정렬 클래스 추가
        header.classList.add(isAscending ? "desc" : "asc");

        // 행 정렬
        const sortedRows = tableRows.sort((a, b) => {
            const aText = a.querySelectorAll("td")[columnIndex].textContent.trim();
            const bText = b.querySelectorAll("td")[columnIndex].textContent.trim();

            // 학번 정렬 (숫자)
            if (columnIndex === 0) { // 학번 열 (1번째 열)
                return (parseInt(aText, 10) - parseInt(bText, 10)) * direction;
            }

            // 이름 정렬 (텍스트)
            if (columnIndex === 1) { // 이름 열 (2번째 열)
                return aText.localeCompare(bText) * direction;
            }

            // 사유 정렬 (텍스트)
            if (columnIndex === 2) { // 사유 열 (3번째 열)
                return aText.localeCompare(bText) * direction;
            }

            // 부여시각 정렬 (날짜)
            if (columnIndex === 3) { // 부여시각 열 (4번째 열)
                return (new Date(aText) - new Date(bText)) * direction;
            }

            // 부여점수 정렬 (숫자)
            if (columnIndex === 4) { // 부여점수 열 (5번째 열)
                const aValue = parseFloat(aText.replace("+", "")); // "+" 제거 후 숫자로 변환
                const bValue = parseFloat(bText.replace("+", ""));
                return (aValue - bValue) * direction;
            }

            // 부여자 정렬 (텍스트)
            if (columnIndex === 5) { // 부여자 열 (6번째 열)
                return aText.localeCompare(bText) * direction;
            }

            // 기본적으로 텍스트 정렬
            return aText.localeCompare(bText) * direction;
        });

        // 정렬된 행을 테이블에 추가
        tableBody.innerHTML = "";
        sortedRows.forEach(row => tableBody.appendChild(row));
    });
});
  dateCells.forEach(cell => {
    const originalText = cell.textContent.trim(); // 예: "20250514 09:18:56"
    const datePart = originalText.split(' ')[0];  // "20250514"

    // 날짜 형식 변경
    const formattedDate = `${datePart.slice(0, 4)}/${datePart.slice(4, 6)}/${datePart.slice(6, 8)}`;

    cell.textContent = formattedDate; // "2025/05/14"
  });
});