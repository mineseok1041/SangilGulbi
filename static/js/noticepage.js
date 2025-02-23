// 페이지가 로드될 때 공지사항 정보를 불러오는 함수 실행
document.addEventListener("DOMContentLoaded", loadNotice);

// 공지사항 상세 정보를 로드하는 함수
function loadNotice() {
    // 로컬 스토리지에서 선택된 공지사항 ID 가져오기
    let noticeId = localStorage.getItem("selectedNotice");

    // 로컬 스토리지에서 저장된 공지사항 목록 가져오기 (없으면 빈 배열)
    let notices = JSON.parse(localStorage.getItem("notices")) || [];

    // 선택된 ID와 일치하는 공지사항 찾기
    let notice = notices.find(n => n.id == noticeId);

    // 해당 공지사항이 없으면 알림을 띄우고 공지 목록 페이지로 이동
    if (!notice) {
        alert("공지사항을 찾을 수 없습니다.");
        window.location.href = "/mainnotice"; // 공지 목록 페이지로 이동
        return;
    }

    // HTML 요소에 공지사항 데이터 표시
    document.getElementById("title").textContent = notice.title; // 제목
    document.getElementById("author").textContent = "작성자: " + notice.author; // 작성자
    document.getElementById("date").textContent = "작성일: " + notice.date; // 작성일
    document.getElementById("content").textContent = notice.content; // 내용
}
