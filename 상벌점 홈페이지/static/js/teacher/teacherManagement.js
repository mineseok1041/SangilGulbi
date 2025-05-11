document.addEventListener("DOMContentLoaded", function () {
    const searchInput = document.querySelector(".searchInput"); // 검색창
    const table = document.querySelector(".teacherInfo_table"); // 학생 정보 테이블
    const tableRows = Array.from(document.querySelectorAll(".teacherInfo_table tbody tr")); // 테이블의 모든 행 가져오기
    const tableBody = table.querySelector("tbody");
    const resetButton = document.querySelector(".resetPasswd"); // "비밀번호 재설정" 버튼
    const headers = document.querySelectorAll(".teacherInfo_table thead th.sortable");

    let selectedTeacher = null; // 선택된 학생 정보 초기화

    // 행 클릭 이벤트 추가
    tableRows.forEach(row => {
        row.addEventListener("click", function (event) {
            event.stopPropagation(); // 클릭 이벤트가 상위 요소로 전파되지 않도록 방지

            // 이미 선택된 행을 다시 클릭하면 선택 해제
            if (row.classList.contains("selected-row")) {
                row.classList.remove("selected-row");
                selectedTeacher = null; // 선택된 교사 정보 초기화
            } else {
                // 다른 행의 선택 해제
                tableRows.forEach(r => r.classList.remove("selected-row"));
                // 현재 행에 선택 클래스 추가
                row.classList.add("selected-row");

                // 선택된 교사 정보 저장
                const teacherName = row.cells[0].textContent.trim(); // 교사 이름
                const teacherId = row.cells[1].textContent.trim(); // 교사 아이디
                selectedTeacher = { teacherName, teacherId }; // 선택된 교사 정보 객체
            }
        });
    });

    // 테이블 외부 클릭 시 선택 해제
    document.addEventListener("click", function (event) {
        if (!table.contains(event.target)) {
            tableRows.forEach(row => row.classList.remove("selected-row"));
        }
    });

    // 검색창에 입력 이벤트 추가
    searchInput.addEventListener("input", function () {
        const filter = searchInput.value.toLowerCase(); // 입력값을 소문자로 변환

        tableRows.forEach(row => {
            const cells = row.querySelectorAll("td:nth-child(1), td:nth-child(2)"); // 각 행의 셀 가져오기
            const rowText = Array.from(cells)
                .map(cell => cell.textContent.toLowerCase()) // 셀의 텍스트를 소문자로 변환
                .join(" "); // 셀의 텍스트를 합침

            // 입력값이 행의 텍스트에 포함되면 표시, 아니면 숨김
            if (rowText.includes(filter)) {
                row.style.display = ""; // 행 표시
            } else {
                row.style.display = "none"; // 행 숨기기
            }
        });
    });

    resetButton.addEventListener("click", function () {
        let teacherName = ""; // 기본값
        let teacherId = ""; // 기본값

        // 교사가 선택된 경우 해당 정보를 사용
        if (selectedTeacher) {
            teacherName = selectedTeacher.teacherName;
            teacherId = selectedTeacher.teacherId;
        }

        const popupWidth = 600;
        const popupHeight = 800;
        const left = (window.innerWidth - popupWidth) / 2 + window.screenX;
        const top = (window.innerHeight - popupHeight) / 2 + window.screenY;

        // 팝업 열기
        window.open(
            `resetTeacherPasswdPopup.html?teacherName=${teacherName}&teacherId=${teacherId}`,
            "비밀번호 재설정",
            `width=${popupWidth},height=${popupHeight},left=${left},top=${top}`
        );
    });
    // 정렬 기능 추가
    headers.forEach(header => {
        header.addEventListener("click", function () {
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

                // 날짜 정렬 (부여 시각)
                if (columnIndex === 2) { // 부여 시각 열 (4번째 열)
                    return (new Date(aText) - new Date(bText)) * direction;
                }

                // 일반 텍스트 정렬
                return aText > bText ? direction : aText < bText ? -direction : 0;
            });

            // 정렬된 행을 테이블에 추가
            tableBody.innerHTML = "";
            sortedRows.forEach(row => tableBody.appendChild(row));
        });
    });
});