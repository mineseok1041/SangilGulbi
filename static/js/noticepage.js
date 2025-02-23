document.addEventListener("DOMContentLoaded", loadNotice);

function loadNotice() {
    let noticeId = localStorage.getItem("selectedNotice");
    let notices = JSON.parse(localStorage.getItem("notices")) || [];
    let notice = notices.find(n => n.id == noticeId);

    if (!notice) {
        alert("공지사항을 찾을 수 없습니다.");
        window.location.href = "/mainnotice";
        return;
    }

    document.getElementById("title").textContent = notice.title;
    document.getElementById("author").textContent = "작성자: " + notice.author;
    document.getElementById("date").textContent = "작성일: " + notice.date;
    document.getElementById("content").textContent = notice.content;

    // 조회수 증가
    notice.views++;
    localStorage.setItem("notices", JSON.stringify(notices));
}
