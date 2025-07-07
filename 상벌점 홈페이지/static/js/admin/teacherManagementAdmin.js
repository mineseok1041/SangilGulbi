document.addEventListener("DOMContentLoaded", function () {
    const table = document.querySelector(".teacherInfo_table"); // 학생 정보 테이블
    const tableRows = Array.from(document.querySelectorAll(".teacherInfo_table tbody tr")); // 테이블의 모든 행 가져오기
    const tableBody = table.querySelector(".teacherInfo_table tbody");
    const resetButton = document.querySelector(".resetPasswd"); // "비밀번호 재설정" 버튼
    const headers = document.querySelectorAll(".teacherInfo_table thead th.sortable");
    const bellButton = document.querySelector(".bell"); // 알림 버튼
    const deleteButton = document.querySelector(".deleteAccount");
    const addButton = document.querySelector(".addTeacher"); // 추가 버튼
    const searchInput = document.querySelector(".searchBar .searchInput");
    const searchButton = document.querySelector(".searchButton");

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
            const currentRows = tableBody.querySelectorAll("tr");
            currentRows.forEach(row => row.classList.remove("selected-row"));
            selectedStudent = null;
        }
    });

    addButton.addEventListener("click", function () {
        const popupWidth = 600;
        const popupHeight = 800;
        const left = (window.innerWidth - popupWidth) / 2 + window.screenX;
        const top = (window.innerHeight - popupHeight) / 2 + window.screenY;

        // 팝업 열기
        window.open(
            `/admin/addTeacherPopup`,
            "선생님 계정 추가",
            `width=600,height=800,left=${left},top=${top}`
        );
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
            `/admin/resetTeacherPasswdPopup?teacherName=${teacherName}&teacherId=${teacherId}`,
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

            fetch("/admin/deleteTeacherAccount", {
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
            "/admin/teacherSignupApprovalPopup", // 팝업으로 열릴 페이지
            "선생님 계정 승인",
            `width=${popupWidth},height=${popupHeight},left=${left},top=${top}`
        );
    });

    searchButton.addEventListener("click", function () {
        const keyword = searchInput.value.trim();
        fetch(`/admin/searchTeachers?keyword=${encodeURIComponent(keyword)}`)
            .then(res => res.json())
            .then(data => {
                tableBody.innerHTML = "";
                data.forEach(teacher => {
                    const tr = document.createElement("tr");
                    tr.innerHTML = `
                        <td>${teacher.name ?? ""}</td>
                        <td>${teacher.id ?? ""}</td>
                        <td>${teacher.lastlogindate ?? "로그인 기록 없음"}</td>
                    `;

                    // 선택 이벤트 바인딩
                    tr.addEventListener("click", function (event) {
                        event.stopPropagation();

                        // 이미 선택된 경우 해제
                        if (tr.classList.contains("selected-row")) {
                            tr.classList.remove("selected-row");
                            selectedStudent = null;
                            return;
                        }
                    
                        // 기존 선택 해제
                        tableBody.querySelectorAll("tr").forEach(r => r.classList.remove("selected-row"));
                    
                        // 새 선택 적용
                        tr.classList.add("selected-row");
                    
                        const studentNum = tr.cells[0].textContent.trim();
                        const studentName = tr.cells[1].textContent.trim();
                        const studentId = tr.cells[2].textContent.trim();
                    
                        selectedStudent = { studentNum, studentName, studentId };
                    });
                    tableBody.appendChild(tr);
                });
            });
    });
    
    // 엔터키로도 검색 가능하게
    searchInput.addEventListener("keydown", function (event) {
        if (event.key === "Enter") {
            event.preventDefault();
            searchButton.click();
        }
    });
});