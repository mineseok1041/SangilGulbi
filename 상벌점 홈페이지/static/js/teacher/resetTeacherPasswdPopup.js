document.addEventListener("DOMContentLoaded", function () {
    const tableRows = Array.from(document.querySelectorAll(".bonusPointReasonTable tbody tr")); // 테이블의 모든 행 가져오기
    const urlParams = new URLSearchParams(window.location.search);
    const teacherName = urlParams.get("teacherName") || ""; // 기본값 설정
    const teacherId = urlParams.get("teacherId") || ""; // 기본값 설정
    const teacherSearchModal = document.querySelector(".teacherSearchModal"); // 모달
    const modalContent = document.querySelector(".modalContent"); // 모달 내부 컨텐츠
    const teacherRows = document.querySelectorAll(".teacherTable tbody tr"); // 학생 목록 행
    const teacherNameElement = document.querySelector(".teacherName"); // 이름 표시 영역
    const teacherIdElement = document.querySelector(".teacherId"); // 선생님 ID 표시 영역
    const searchTeacherIcon = document.querySelector(".searchTeacherIcon"); // 돋보기 아이콘

    let selectedTeacher = null; // 선택된 교사 정보 초기화

    
    tableRows.forEach(row => {
        row.addEventListener("click", function () {
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
            const teacherName = row.querySelector("td:nth-child(1)").textContent.trim(); // 이름
            const teacherId = row.querySelector("td:nth-child(2)").textContent.trim(); // 아이디
            selectedTeacher = { teacherName, teacherId }; // 선택된 교사 정보 객체

            // 부여 정보 섹션에 데이터 업데이트
            teacherNameElement.textContent = teacherName;
            teacherIdElement.textContent = teacherId;
            }
        });
    });

    // 테이블 외부 클릭 시 선택 해제
    document.addEventListener("click", function (event) {
        const table = document.querySelector(".bonusPointReasonTable"); // 테이블 요소 가져오기
        if (!table.contains(event.target)) {
            tableRows.forEach(row => row.classList.remove("selected-row"));
        }
    });

    // 비밀번호 토글 기능
    const togglePasswordIcons = document.querySelectorAll(".togglePassword"); // 모든 토글 아이콘 가져오기

    togglePasswordIcons.forEach(icon => {
        icon.addEventListener("click", function () {
            const passwordInput = icon.previousElementSibling; // 아이콘 앞의 입력 필드 가져오기

            if (passwordInput.type === "password") {
                // 비밀번호가 숨겨진 상태 -> 보이도록 변경
                passwordInput.type = "text";
                icon.src = "../static/img/eyeOnIcon.png"; // 눈을 뜨고 있는 아이콘으로 변경
                icon.alt = "Hide Password"; // 접근성 텍스트 변경
            } else {
                // 비밀번호가 보이는 상태 -> 숨기도록 변경
                passwordInput.type = "password";
                icon.src = "../static/img/eyeOffIcon.png"; // 눈을 감고 있는 아이콘으로 변경
                icon.alt = "Show Password"; // 접근성 텍스트 변경
            }
        });
    });

    // 돋보기 아이콘 클릭 이벤트
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

    // 선생님 목록 행 클릭 이벤트
    teacherRows.forEach(row => {
        row.addEventListener("click", function () {
            const teacherName = row.querySelector("td:nth-child(1)").textContent; // 이름
            const teacherId = row.querySelector("td:nth-child(2)").textContent; // 학생 ID

            // 부여 정보 섹션에 데이터 업데이트
            teacherNameElement.textContent = teacherName;
            teacherIdElement.textContent = teacherId;

            // 모달 닫기
            teacherSearchModal.classList.remove("visible");
            teacherSearchModal.classList.add("hidden");
        });
    });


    // 이름과 아이디를 화면에 표시
    if (teacherName && teacherId) {
        document.querySelector(".teacherName").textContent = teacherName;
        document.querySelector(".teacherId").textContent = teacherId;
    };

    window.addEventListener("beforeunload", function () {
    teacherNameElement.textContent = ""; // 이름 초기화
    teacherIdElement.textContent = ""; // 아이디 초기화
    teacherRows.forEach(row => row.classList.remove("selected-row")); // 선택된 행 초기화
    selectedTeacher = null; // 선택된 데이터 초기화
});
    
});