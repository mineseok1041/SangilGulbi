document.addEventListener("DOMContentLoaded", function () {
    const rows = document.querySelectorAll(".studentInfo_table tbody tr");
    rows.forEach((row, index) => {
        if (index >= 8) {
            row.style.display = "none"; // 8번째 이후 데이터 숨김
        }
    });
});

document.addEventListener("DOMContentLoaded", function () {
    const rows = document.querySelectorAll(".teacherManagement_table tbody tr");
    rows.forEach((row, index) => {
        if (index >= 3) {
            row.style.display = "none"; // 8번째 이후 데이터 숨김
        }
    });
});

document.addEventListener("DOMContentLoaded", function () {
    const rows = document.querySelectorAll(".community_table tbody tr");
    rows.forEach((row, index) => {
        if (index >= 3) {
            row.style.display = "none"; // 8번째 이후 데이터 숨김
        }
    });
});

document.addEventListener("DOMContentLoaded", function () { 
    const bonusButton = document.querySelector(".giveBonus"); // "상점 부여" 버튼
    const penaltyButton = document.querySelector(".givePenalty"); // "벌점 부여" 버튼

    penaltyButton.addEventListener("click", function () {
        const popupWidth = 1280;
        const popupHeight = 720;
        const screenLeft = window.screenLeft || window.screenX; // 브라우저의 왼쪽 위치
        const screenTop = window.screenTop || window.screenY; // 브라우저의 상단 위치
        const screenWidth = window.innerWidth || document.documentElement.clientWidth; // 브라우저 너비
        const screenHeight = window.innerHeight || document.documentElement.clientHeight; // 브라우저 높이

        const left = screenLeft + (screenWidth - popupWidth) / 2; // 중앙 정렬 계산
        const top = screenTop + (screenHeight - popupHeight) / 2; // 중앙 정렬 계산

        const popup = window.open(
            "givePenaltyPointPopup.html",
            "popupWindow",
            `width=${popupWidth},height=${popupHeight},left=${left},top=${top}`
        );

            // 팝업 창에 데이터 전달
            popup.onload = function () {
                const studentNameInput = popup.document.querySelector(".student-name");
                if (studentNameInput) {
                    studentNameInput.value = studentName; // 학생 이름 전달
                }
            };
        });

    bonusButton.addEventListener("click", function () {
        const popupWidth = 1280;
        const popupHeight = 720;
        const screenLeft = window.screenLeft || window.screenX; // 브라우저의 왼쪽 위치
        const screenTop = window.screenTop || window.screenY; // 브라우저의 상단 위치
        const screenWidth = window.innerWidth || document.documentElement.clientWidth; // 브라우저 너비
        const screenHeight = window.innerHeight || document.documentElement.clientHeight; // 브라우저 높이

        const left = screenLeft + (screenWidth - popupWidth) / 2; // 중앙 정렬 계산
        const top = screenTop + (screenHeight - popupHeight) / 2; // 중앙 정렬 계산

        const popup = window.open(
            "giveBonusPointPopup.html",
            "popupWindow",
            `width=${popupWidth},height=${popupHeight},left=${left},top=${top}`
        );

            // 팝업 창에 데이터 전달
            popup.onload = function () {
                const studentNameInput = popup.document.querySelector(".student-name");
                if (studentNameInput) {
                    studentNameInput.value = studentName; // 학생 이름 전달
                }
            };
        });
});

