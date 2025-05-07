function togglePasswordVisibility(inputId, icon) {
    var input = document.getElementById(inputId);
//아이콘 이미지 클릭시 password 타입을 text 형태로 바꿔 비밀 번호 표시
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
