function togglePasswordVisibility(inputId, icon) {
    var input = document.getElementById(inputId);

    if (input.type === "password") {
        input.type = "text";
        setTimeout(() => {
            icon.src = icon.getAttribute("data-show");
        }, 10); // 지연을 줘서 밀림 방지
    } else {
        input.type = "password";
        setTimeout(() => {
            icon.src = icon.getAttribute("data-hide");
        }, 10);
    }
}