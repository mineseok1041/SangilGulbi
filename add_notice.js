function saveNotice() {
    let title = document.getElementById("title").value;
    let author = document.getElementById("author").value;
    let date = new Date().toISOString().split('T')[0]; // 작성일 (YYYY-MM-DD)
    let views = 0; // 조회수 초기값

    if (!title || !author) {
        alert("제목과 작성자를 입력해주세요.");
        return;
    }

    // 기존 공지사항 데이터 가져오기
    let notices = JSON.parse(localStorage.getItem("notices")) || [];

    // 새 공지사항 추가
    notices.push({ id: notices.length + 1, title, author, date, views });

    // localStorage에 저장
    localStorage.setItem("notices", JSON.stringify(notices));

    // 메인 페이지로 이동
    window.location.href = "index.html";
}