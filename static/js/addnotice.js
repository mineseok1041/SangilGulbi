document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("addNoticeBtn").addEventListener("click", addNotice);
});

function addNotice() {
    let title = document.getElementById("title").value.trim();
    let content = document.getElementById("content").value.trim();

    if (!title || !content) {
        alert("제목과 내용을 입력해주세요.");
        return;
    }

    let notices = JSON.parse(localStorage.getItem("notices")) || [];

    let newNotice = {
        id: new Date().getTime(), // 유니크한 ID
        title: title,
        author: "사용자", // 현재 로그인된 사용자 (추후 서버에서 가져올 수도 있음)
        date: new Date().toISOString().split("T")[0], // YYYY-MM-DD 형식
        views: 0,
        content: content
    };

    notices.unshift(newNotice); // 새로운 공지를 맨 위에 추가
    localStorage.setItem("notices", JSON.stringify(notices));

    alert("공지사항이 추가되었습니다.");
    window.location.href = "/mainnotice"; // 공지 목록 페이지로 이동
}
