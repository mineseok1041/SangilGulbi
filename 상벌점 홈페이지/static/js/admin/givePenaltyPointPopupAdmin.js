document.addEventListener("DOMContentLoaded", function () {
    const tableRows = Array.from(document.querySelectorAll(".penaltyPointReasonTable tbody tr")); // 테이블의 모든 행 가져오기
    const searchStudentIcon = document.querySelector(".searchStudentIcon"); // 돋보기 아이콘
    const studentSearchModal = document.querySelector(".studentSearchModal"); // 모달
    const modalContent = document.querySelector(".modalContent"); // 모달 내부 컨텐츠
    const studentRows = document.querySelectorAll(".studentTable tbody tr"); // 테이블 행
    const studentNumElement = document.querySelector(".studentNum"); // 학번 표시 영역
    const studentNameElement = document.querySelector(".studentName"); // 이름 표시 영역
    const studentIdElement = document.querySelector(".studentId"); // 학생 ID 영역
    const writeTeacherIdElement = document.querySelector(".writeTeacherId");
    const searchTeacherIcon = document.querySelector(".searchTeacherIcon"); // 부여자 검색 돋보기 아이콘
    const teacherSearchModal = document.querySelector(".teacherSearchModal"); // 부여자 검색 모달
    const teacherRows = document.querySelectorAll(".teacherTable tbody tr"); // 부여자 목록 행
    const giveTeacherNameElement = document.querySelector(".giveTeacherName"); // 부여자 표시
    const reasonRows = document.querySelectorAll(".penaltyPointReasonTable tbody tr"); // 벌점 항목 행
    const reasonElement = document.querySelector(".reason"); // 사유 표시 영역
    const penaltyPointElement = document.querySelector(".studentPenaltyPoint"); // 점수 표시 영역
    const urlParams = new URLSearchParams(window.location.search);
    const studentNum = urlParams.get("studentNum") || ""; // 기본값 설정
    const studentName = urlParams.get("studentName") || ""; // 기본값 설정
    const studentId = urlParams.get("studentId") || "";

    // 행 클릭 이벤트 추가
    tableRows.forEach(row => {
        row.addEventListener("click", function () {
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

    // 테이블 외부 클릭 시 선택 해제
    document.addEventListener("click", function (event) {
        const table = document.querySelector(".penaltyPointReasonTable"); // 테이블 요소 가져오기
        if (!table.contains(event.target)) {
            tableRows.forEach(row => row.classList.remove("selected-row"));
        }
    });

    // 돋보기 아이콘 클릭 이벤트
    searchStudentIcon.addEventListener("click", function () {
        studentSearchModal.classList.remove("hidden");
        studentSearchModal.classList.add("visible"); // 모달 표시
    });

    // 모달 외부 클릭 시 닫기
    studentSearchModal.addEventListener("click", function (event) {
        // 모달 내부를 클릭한 경우 닫히지 않도록 처리
        if (!modalContent.contains(event.target)) {
            studentSearchModal.classList.remove("visible");
            studentSearchModal.classList.add("hidden"); // 모달 숨김
        }
    });

    // 테이블 행 클릭 이벤트
    studentRows.forEach(row => {
        row.addEventListener("click", function () {
            const studentNumber = row.querySelector("td:nth-child(1)").textContent; // 학번
            const studentName = row.querySelector("td:nth-child(2)").textContent; // 이름
            const studentId = row.querySelector("td:nth-child(3)").textContent; // ID (숨겨진 셀)

            // 부여 정보 섹션에 데이터 업데이트
            studentNumElement.textContent = studentNumber;
            studentNameElement.textContent = studentName;
            studentIdElement.textContent = studentId; // <- 여기에 ID도 반영

            // 모달 닫기
            studentSearchModal.classList.remove("visible");
            studentSearchModal.classList.add("hidden");
        });
    });

    // 부여자 검색 돋보기 아이콘 클릭 이벤트
    searchTeacherIcon.addEventListener("click", function () {
        teacherSearchModal.classList.remove("hidden");
        teacherSearchModal.classList.add("visible"); // 모달 표시
    });

    // 모달 외부 클릭 시 닫기
    teacherSearchModal.addEventListener("click", function (event) {
        // 모달 내부를 클릭한 경우 닫히지 않도록 처리
        if (!modalContent.contains(event.target)) {
            teacherSearchModal.classList.remove("visible");
            teacherSearchModal.classList.add("hidden"); // 모달 숨김
        }
    });

    // 부여자 목록 행 클릭 이벤트
    teacherRows.forEach(row => {
        row.addEventListener("click", function () {
            const teacherId = row.querySelector("td:nth-child(1)").textContent; // ID
            const teacherName = row.querySelector("td:nth-child(2)").textContent; // 부여자 이름

            // 부여 정보 섹션에 부여자 이름 업데이트
            giveTeacherNameElement.textContent = teacherName;

            // 숨겨진 span에 ID 저장
            document.querySelector(".giveTeacherId").textContent = teacherId;

            // 모달 닫기
            teacherSearchModal.classList.remove("visible");
            teacherSearchModal.classList.add("hidden");
        });
    });

    // 벌점 항목 클릭 이벤트
    reasonRows.forEach(row => {
        row.addEventListener("click", function () {
            const reason = row.querySelector("td:nth-child(2)").textContent; // 사유
            const penaltyPoint = row.querySelector("td:nth-child(3)").textContent; // 점수

            // 부여 정보 섹션에 데이터 업데이트
            reasonElement.textContent = reason;
            penaltyPointElement.textContent = penaltyPoint;

            // 선택된 행 강조 표시
            reasonRows.forEach(r => r.classList.remove("selected-row")); // 기존 선택 해제
            row.classList.add("selected-row"); // 현재 행 선택
        });
    });

    // 학생 목록 행 클릭 이벤트
    studentRows.forEach(row => {
        row.addEventListener("click", function () {
            const studentNumber = row.querySelector("td:nth-child(1)").textContent; // 학번
            const studentName = row.querySelector("td:nth-child(2)").textContent; // 이름

            // 부여 정보 섹션에 데이터 업데이트
            studentNumElement.textContent = studentNumber;
            studentNameElement.textContent = studentName;

            // 모달 닫기
            studentSearchModal.classList.remove("visible");
            studentSearchModal.classList.add("hidden");
        });
    });

    // 부여자 목록 행 클릭 이벤트
    teacherRows.forEach(row => {
        row.addEventListener("click", function () {
            const teacherName = row.querySelector("td:nth-child(2)").textContent; // 부여자 이름

            // 부여 정보 섹션에 부여자 이름 업데이트
            giveTeacherNameElement.textContent = teacherName;

            // 모달 닫기
            teacherSearchModal.classList.remove("visible");
            teacherSearchModal.classList.add("hidden");
        });
    });

    // 학번과 이름을 화면에 표시
    if (studentNum && studentName && studentId) {
        document.querySelector(".studentNum").textContent = studentNum;
        document.querySelector(".studentName").textContent = studentName;
        document.querySelector(".studentId").textContent = studentId;
    }
});

function submitPenalty() {
    document.getElementById("formStudentId").value = document.querySelector(".studentId").textContent;
    document.getElementById("formReason").value = document.querySelector(".reason").textContent;
    document.getElementById("formPoint").value = document.querySelector(".studentPenaltyPoint").textContent.replace("-", "");
    document.getElementById("formWriteTeacherId").value = document.querySelector(".writeTeacherId").textContent;
    document.getElementById("formGiveTeacherId").value = document.querySelector(".giveTeacherId").textContent;
    document.getElementById("formOpinion").value = document.querySelector(".opinion").value;

    document.getElementById("penaltyForm").submit();
}

    document.querySelector('.cancelButton').addEventListener('click', function() {
    window.close();
});