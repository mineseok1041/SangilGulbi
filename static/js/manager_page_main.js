// 사용자 박스 토글 함수
function toggleUserBox() {
    const userBox = document.querySelector('.user_box');
    const userInfo = document.querySelector('#userCount');

    // 박스 열기/닫기
    userBox.classList.toggle('open');
    if (userBox.classList.contains('open')) {
        userInfo.style.display = 'block';  // 사용자명 보이게 하기
    } else {
        userInfo.style.display = 'none';  // 사용자명 숨기기
    }
}