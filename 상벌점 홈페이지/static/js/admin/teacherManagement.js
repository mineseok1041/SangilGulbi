document.addEventListener("DOMContentLoaded", function () {
    const table = document.querySelector(".teacherInfo_table"); // 학생 정보 테이블
    const tableRows = Array.from(document.querySelectorAll(".teacherInfo_table tbody tr")); // 테이블의 모든 행 가져오기
    const tableBody = table.querySelector(".teacherInfo_table tbody");
    const resetButton = document.querySelector(".resetPasswd"); // "비밀번호 재설정" 버튼
    const headers = document.querySelectorAll(".teacherInfo_table thead th.sortable");
    const bellButton = document.querySelector(".bell"); // 알림 버튼
    const deleteButton = document.querySelector(".deleteAccount");

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

    // 페이지 로드 시 기본 정렬 (이름순)
    const sortedRows = tableRows.sort((a, b) => {
        const aName = a.querySelector("td:nth-child(1)").textContent.trim(); // 이름 열
        const bName = b.querySelector("td:nth-child(1)").textContent.trim();
        return aName.localeCompare(bName); // 이름순 정렬
    });

    // 정렬된 행을 테이블에 추가
    tableBody.innerHTML = "";
    sortedRows.forEach(row => tableBody.appendChild(row));

    // 테이블 외부 클릭 시 선택 해제
    document.addEventListener("click", function (event) {
        if (!table.contains(event.target)) {
            tableRows.forEach(row => row.classList.remove("selected-row"));
            selectedTeacher = null; // 선택된 교사 정보 초기화
        }
    });

    resetButton.addEventListener("click", function () {
        const teacherName = selectedTeacher ? selectedTeacher.teacherName : ""; 
        const teacherId = selectedTeacher ? selectedTeacher.teacherId : "";

        const popupWidth = 600;
        const popupHeight = 800;
        const left = (window.innerWidth - popupWidth) / 2 + window.screenX;
        const top = (window.innerHeight - popupHeight) / 2 + window.screenY;

        // 팝업 열기
        window.open(
            `/teacher/resetTeacherPasswdPopup?teacherName=${teacherName}&teacherId=${teacherId}`,
            "비밀번호 재설정",
            `width=600,height=800,left=${left},top=${top}`
        );
    });

    if (deleteButton) {
        deleteButton.addEventListener("click", function () {
            if (!selectedTeacher) {
                alert("삭제할 선생님을 선택하세요.");
                return;
            }
            const confirmDelete = confirm(`정말로 ${selectedTeacher.teacherName}(${selectedTeacher.teacherId}) 선생님 계정을 삭제하시겠습니까?`);
            if (!confirmDelete) return;

            fetch("/teacher/deleteTeacherAccount", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ teacherId: selectedTeacher.teacherId })
            })
            .then(res => res.json())
            .then(data => {
                if (data.success) {
                    alert("계정이 삭제되었습니다.");
                    location.reload();
                } else {
                    alert(data.error || "삭제 중 오류가 발생했습니다.");
                }
            })
            .catch(() => alert("삭제 요청 중 오류가 발생했습니다."));
        });
    }

    // 알림 버튼 클릭 시 팝업 열기
    bellButton.addEventListener("click", function () {
        const popupWidth = 600;
        const popupHeight = 800;
        const left = (window.innerWidth - popupWidth) / 2 + window.screenX;
        const top = (window.innerHeight - popupHeight) / 2 + window.screenY;

        // 팝업 열기
        window.open(
            "/teacher/teacherSignupApprovalPopup", // 팝업으로 열릴 페이지
            "선생님 계정 승인",
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
    const dateCell = document.querySelectorAll('.date-cell');

    dateCell.forEach(cell => {
        const originalText = cell.textContent.trim(); // 예: "20250514 09:18:56"
        const datePart = originalText.split(' ')[0];  // "20250514"

        // 날짜 형식 변경
        const formattedDate = `${datePart.slice(0, 4)}/${datePart.slice(4, 6)}/${datePart.slice(6, 8)}`;

        cell.textContent = formattedDate; // "2025/05/14"
    });
});