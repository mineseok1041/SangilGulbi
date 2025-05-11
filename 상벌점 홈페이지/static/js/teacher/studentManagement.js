document.addEventListener("DOMContentLoaded", function () {
    const table = document.querySelector(".studentInfo_table");
    const tableRows = Array.from(document.querySelectorAll(".studentInfo_table tbody tr")); // 테이블의 모든 행 가져오기
    const tableBody = table.querySelector("tbody");
    const headers = document.querySelectorAll(".studentInfo_table thead th.sortable");
    const resetButton = document.querySelector(".resetPasswd"); // "비밀번호 재설정" 버튼
    const bonusButton = document.querySelector(".giveBonus"); // "상점 부여" 버튼
    const penaltyButton = document.querySelector(".givePenalty"); // "벌점 부여" 버튼
    const filterIcon = document.querySelector(".filterIcon"); // 필터 아이콘
    const filterPopup = document.querySelector(".filterPopup"); // 필터 팝업
    const resetFiltersButton = filterPopup.querySelector(".resetFilters");

    let selectedStudent = null; // 선택된 학생 정보 초기화

    // 행 클릭 이벤트 추가
    tableRows.forEach(row => {
        row.addEventListener("click", function (event) {
            event.stopPropagation(); // 클릭 이벤트가 상위 요소로 전파되지 않도록 방지

            // 이미 선택된 행을 다시 클릭하면 선택 해제
            if (row.classList.contains("selected-row")) {
                row.classList.remove("selected-row");
                selectedStudent = null; // 선택된 학생 정보 초기화
            } else {
                // 다른 행의 선택 해제
                tableRows.forEach(r => r.classList.remove("selected-row"));
                // 현재 행에 선택 클래스 추가
                row.classList.add("selected-row");

                // 선택된 학생 정보 저장
                const studentNum = row.cells[0].textContent.trim(); // 학번
                const studentName = row.cells[1].textContent.trim(); // 이름
                const studentId = row.cells[2].textContent.trim(); // 아이디
                selectedStudent = { studentNum, studentName, studentId }; // 선택된 학생 정보 객체
            }
        });
    });

    // 테이블 외부 클릭 시 선택 해제
    document.addEventListener("click", function (event) {
        if (!table.contains(event.target)) {
            tableRows.forEach(row => row.classList.remove("selected-row"));
            selectedStudent = null; // 선택된 학생 정보 초기화
        }
    });

    // 필터 아이콘 클릭 이벤트
    filterIcon.addEventListener("click", function () {
        filterPopup.classList.toggle("hidden"); // 팝업 메뉴 표시/숨김
    });

    // 초기화 버튼 클릭 이벤트
    resetFiltersButton.addEventListener("click", function () {
        // 모든 체크박스 해제
        const checkboxes = filterPopup.querySelectorAll("input[type='checkbox']");
        checkboxes.forEach(checkbox => {
            checkbox.checked = false;
        });

        // 테이블의 모든 행 표시
        tableRows.forEach(row => {
            row.style.display = ""; // 모든 행 표시
        });
    });

    // 팝업 외부 클릭 시 팝업 닫기
    document.addEventListener("click", function (event) {
        if (!filterPopup.contains(event.target) && !filterIcon.contains(event.target)) {
            filterPopup.classList.add("hidden");
        }
    });

    resetButton.addEventListener("click", function () {
        let studentNum = ""; // 기본값
        let studentName = ""; // 기본값
        let studentId = ""; // 기본값

        // 학생이 선택된 경우 해당 정보를 사용
        if (selectedStudent) {
            studentNum = selectedStudent.studentNum;
            studentName = selectedStudent.studentName;
            studentId = selectedStudent.studentId;
        }
            const popupWidth = 600;
            const popupHeight = 800;
            const left = (window.innerWidth - popupWidth) / 2 + window.screenX;
            const top = (window.innerHeight - popupHeight) / 2 + window.screenY;

            // 팝업 열기
            window.open(
                `resetStudentPasswdPopup.html?studentNum=${studentNum}&studentName=${encodeURIComponent(studentName)}&studentId=${encodeURIComponent(studentId)}`,
                "비밀번호 재설정",
                `width=${popupWidth},height=${popupHeight},left=${left},top=${top}`
            );
    });

    penaltyButton.addEventListener("click", function () {
        let studentNum = ""; // 기본값
        let studentName = ""; // 기본값

        // 학생이 선택된 경우 해당 정보를 사용
        if (selectedStudent) {
            studentNum = selectedStudent.studentNum;
            studentName = selectedStudent.studentName;
        }
            const popupWidth = 1280;
            const popupHeight = 720;
            const left = (window.innerWidth - popupWidth) / 2 + window.screenX;
            const top = (window.innerHeight - popupHeight) / 2 + window.screenY;

            // 팝업 열기
            window.open(
                `/teacher/givePenaltyPoint?studentNum=${studentNum}&studentName=${encodeURIComponent(studentName)}`,
                "벌점 부여",
                `width=${popupWidth},height=${popupHeight},left=${left},top=${top}`
            );
    });

    bonusButton.addEventListener("click", function () {
        let studentNum = ""; // 기본값
        let studentName = ""; // 기본값
        let studentId = "";

        // 학생이 선택된 경우 해당 정보를 사용
        if (selectedStudent) {
            studentNum = selectedStudent.studentNum;
            studentName = selectedStudent.studentName;
            studentId = selectedStudent.studentId;
        }
            const popupWidth = 1280;
            const popupHeight = 720;
            const left = (window.innerWidth - popupWidth) / 2 + window.screenX;
            const top = (window.innerHeight - popupHeight) / 2 + window.screenY;

            // 팝업 열기
            window.open(
                `/teacher/giveBonusPoint?studentNum=${studentNum}&studentName=${encodeURIComponent(studentName)}&studentId=${studentId}`,
                "상점 부여",
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

                // 숫자 정렬 (총 상벌점)
                if (columnIndex === 4) { // 총 상벌점 열 (5번째 열, 0부터 시작하므로 4)
                    const aValue = parseFloat(aText.replace("+", "")); // "+" 제거 후 숫자로 변환
                    const bValue = parseFloat(bText.replace("+", ""));
                    return (aValue - bValue) * direction;
                }

                // 날짜 정렬 (마지막 활동)
                if (columnIndex === 3) { // 마지막 활동 열 (4번째 열)
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