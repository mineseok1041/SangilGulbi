document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("adminForm").addEventListener("submit", function(event) {
        event.preventDefault();

        const adminId = document.getElementById("adminId").value.trim();
        const adminPassword = document.getElementById("adminPassword").value.trim();
        const resultMessage = document.getElementById("resultMessage");

        // 비밀번호 유효성 검사 정규식 (영문, 숫자, 특수문자 포함 8자 이상)
        const passwordRegex = /^(?=.*[A-Za-z])(?=.*\d)(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{8,}$/;

        // 필수 입력값 확인
        if (!adminId || !adminPassword) {
            alert("아이디와 비밀번호를 입력해주세요.");
            return;
        }

        // 비밀번호 유효성 검사
        if (!passwordRegex.test(adminPassword)) {
            alert("비밀번호는 영어, 숫자, 특수문자가 포함되어야 하며 최소 8자 이상이어야 합니다.");
            return;
        }

        // 성공 메시지 표시
        resultMessage.textContent = "관리자가 추가되었습니다!";
        resultMessage.style.display = "block";

        // 입력 폼 초기화
        document.getElementById("adminForm").reset();

        // 일정 시간 후 메시지 숨기기 (예: 3초 후)
        setTimeout(() => {
            resultMessage.style.display = "none";
        }, 3000);
    });
});
