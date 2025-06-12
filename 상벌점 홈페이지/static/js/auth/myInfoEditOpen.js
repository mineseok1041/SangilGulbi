document.addEventListener("DOMContentLoaded", function () {
    const myInfoEditButton = document.querySelector(".myInfoEdit_nav"); // 내정보수정 버튼

    myInfoEditButton.addEventListener("click", function () {
        const popupWidth = 560;
        const popupHeight = 720;
        const screenLeft = window.screenLeft || window.screenX; // 브라우저의 왼쪽 위치
        const screenTop = window.screenTop || window.screenY; // 브라우저의 상단 위치
        const screenWidth = window.innerWidth || document.documentElement.clientWidth; // 브라우저 너비
        const screenHeight = window.innerHeight || document.documentElement.clientHeight; // 브라우저 높이

        const left = screenLeft + (screenWidth - popupWidth) / 2; // 중앙 정렬 계산
        const top = screenTop + (screenHeight - popupHeight) / 2; // 중앙 정렬 계산

        const popup = window.open(
            "/auth/myInfoEditPopup",
            "popupWindow",
            `width=${popupWidth},height=${popupHeight},left=${left},top=${top}`
        );
    });
});