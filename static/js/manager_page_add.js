
// 비밀번호 보기/숨기기 토글 함수
function togglePasswordVisibility(inputId, icon) {
    var input = document.getElementById(inputId);

    if (input.type === "password") {
        input.type = "text"; // 비밀번호 보이게 설정
        icon.src = icon.getAttribute("data-show"); // 보임 아이콘으로 변경
    } else {
        input.type = "password"; // 비밀번호 숨기기
        icon.src = icon.getAttribute("data-hide"); // 숨김 아이콘으로 변경
    }
}

document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("adminForm").addEventListener("submit", function (event) {
        event.preventDefault();

        const adminId = document.getElementById("adminId").value.trim();
        const adminPassword = document.getElementById("adminPassword").value.trim();
        const adminConfirmPassword = document.getElementById("adminConfirmPassword").value.trim();
        const resultMessage = document.getElementById("resultMessage");


        // 비밀번호 유효성 검사 정규식 (영문, 숫자, 특수문자 포함 8자 이상)
        const passwordRegex = /^(?=.*[A-Za-z])(?=.*\d)(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{8,}$/;

        if (!adminId || !adminPassword || !adminConfirmPassword) {
            alert("아이디와 비밀번호를 입력해주세요.");
            return;
        }

        if (adminPassword !== adminConfirmPassword) {
            alert("비밀번호와 비밀번호 확인이 일치하지 않습니다.");
            return;
        }

        if (!passwordRegex.test(adminPassword)) {
            alert("비밀번호는 영어, 숫자, 특수문자가 포함되어야 하며 최소 8자 이상이어야 합니다.");
            return;
        }

        // "저장되었습니다" 메시지만 출력
        resultMessage.textContent = "저장되었습니다!";
        resultMessage.style.color = "green";
        resultMessage.style.display = "block";

        // 입력 폼 초기화
        document.getElementById("adminForm").reset();

        // 3초 후 메시지 숨기기
        setTimeout(() => {
            resultMessage.style.display = "none";
        }, 3000);
    });
});
