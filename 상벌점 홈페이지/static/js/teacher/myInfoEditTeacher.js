document.addEventListener("DOMContentLoaded", function () {
    // 요소 캐싱
    const teacherNumElement = document.querySelector(".teacherNum");
    const teacherNameElement = document.querySelector(".teacherName");
    const teacherIdElement = document.querySelector(".teacherId");
    const teacherIdInput = document.querySelector(".teacherIdInput");
    const togglePasswordIcons = document.querySelectorAll(".togglePassword");

    // URL 파라미터로 값이 있으면 화면에 표시
    const urlParams = new URLSearchParams(window.location.search);
    const teacherNum = urlParams.get("teacherNum") || "";
    const teacherName = urlParams.get("teacherName") || "";
    const teacherId = urlParams.get("teacherId") || "";
    if (teacherNum && teacherName && teacherId) {
        teacherNumElement.textContent = teacherNum;
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
});