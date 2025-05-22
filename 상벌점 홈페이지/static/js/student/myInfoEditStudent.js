document.addEventListener("DOMContentLoaded", function () {
    // 요소 캐싱
    const studentSearchModal = document.querySelector(".studentSearchModal");
    const modalContent = document.querySelector(".modalContent");
    const studentRows = document.querySelectorAll(".studentTable tbody tr");
    const studentNumElement = document.querySelector(".studentNum");
    const studentNameElement = document.querySelector(".studentName");
    const studentIdElement = document.querySelector(".studentId");
    const studentIdInput = document.querySelector(".studentIdInput");
    const searchStudentIcon = document.querySelector(".searchStudentIcon");
    const togglePasswordIcons = document.querySelectorAll(".togglePassword");

    // URL 파라미터로 값이 있으면 화면에 표시
    const urlParams = new URLSearchParams(window.location.search);
    const studentNum = urlParams.get("studentNum") || "";
    const studentName = urlParams.get("studentName") || "";
    const studentId = urlParams.get("studentId") || "";
    if (studentNum && studentName && studentId) {
        studentNumElement.textContent = studentNum;
        studentNameElement.textContent = studentName;
        studentIdElement.textContent = studentId;
        studentIdInput.value = studentId;
    }

    // 비밀번호 토글 기능
    togglePasswordIcons.forEach(icon => {
        icon.addEventListener("click", function () {
            const passwordInput = icon.previousElementSibling;
            const isHidden = passwordInput.type === "password";
            passwordInput.type = isHidden ? "text" : "password";
            icon.src = isHidden ? "../static/img/eyeOnIcon.png" : "../static/img/eyeOffIcon.png";
            icon.alt = isHidden ? "Hide Password" : "Show Password";
        });
    });

    // 돋보기 아이콘 클릭 시 모달 열기
    searchStudentIcon.addEventListener("click", function () {
        studentSearchModal.classList.remove("hidden");
        studentSearchModal.classList.add("visible");
    });

    // 모달 외부 클릭 시 닫기
    studentSearchModal.addEventListener("click", function (event) {
        if (!modalContent.contains(event.target)) {
            studentSearchModal.classList.remove("visible");
            studentSearchModal.classList.add("hidden");
        }
    });

    // 학생 목록 행 클릭 시 정보 반영 및 모달 닫기
    studentRows.forEach(row => {
        row.addEventListener("click", function () {
            const tds = row.querySelectorAll("td");
            studentNumElement.textContent = tds[0].textContent.trim();
            studentNameElement.textContent = tds[1].textContent.trim();
            studentIdElement.textContent = tds[2].textContent.trim();
            studentIdInput.value = tds[2].textContent.trim();

            studentSearchModal.classList.remove("visible");
            studentSearchModal.classList.add("hidden");
        });
    });
});