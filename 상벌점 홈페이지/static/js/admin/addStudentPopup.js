document.addEventListener("DOMContentLoaded", function () {
    const togglePasswordIcons = document.querySelectorAll(".togglePassword");
    
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