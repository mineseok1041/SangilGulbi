document.addEventListener("DOMContentLoaded", function () {
    // 요소 캐싱
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
});