document.addEventListener("DOMContentLoaded", function () {
    // 요소 캐싱
    const teacherSearchModal = document.querySelector(".teacherSearchModal");
    const modalContent = document.querySelector(".modalContent");
    const teacherRows = document.querySelectorAll(".teacherTable tbody tr");
    const teacherNameElement = document.querySelector(".teacherName");
    const teacherIdElement = document.querySelector(".teacherId");
    const teacherIdInput = document.querySelector(".teacherIdInput");
    const searchTeacherIcon = document.querySelector(".searchTeacherIcon");
    const togglePasswordIcons = document.querySelectorAll(".togglePassword");

    // URL 파라미터로 값이 있으면 화면에 표시
    const urlParams = new URLSearchParams(window.location.search);
    const teacherName = urlParams.get("teacherName") || "";
    const teacherId = urlParams.get("teacherId") || "";
    if (teacherName && teacherId) {
        teacherNameElement.textContent = teacherName;
        teacherIdElement.textContent = teacherId;
        teacherIdInput.value = teacherId;
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
    searchTeacherIcon.addEventListener("click", function () {
        teacherSearchModal.classList.remove("hidden");
        teacherSearchModal.classList.add("visible");
    });

    // 모달 외부 클릭 시 닫기
    teacherSearchModal.addEventListener("click", function (event) {
        if (!modalContent.contains(event.target)) {
            teacherSearchModal.classList.remove("visible");
            teacherSearchModal.classList.add("hidden");
        }
    });

    // 선생님 목록 행 클릭 시 정보 반영 및 모달 닫기
    teacherRows.forEach(row => {
        row.addEventListener("click", function () {
            const tds = row.querySelectorAll("td");
            teacherNameElement.textContent = tds[0].textContent.trim();
            teacherIdElement.textContent = tds[1].textContent.trim();
            teacherIdInput.value = tds[1].textContent.trim();

            teacherSearchModal.classList.remove("visible");
            teacherSearchModal.classList.add("hidden");
        });
    });
});