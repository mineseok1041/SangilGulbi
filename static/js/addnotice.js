// 페이지가 로드되면 addNotice 함수에 이벤트 리스너를 추가
document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("addNoticeBtn").addEventListener("click", addNotice);
});

// 공지사항 추가 함수
async function addNotice() {
    // 입력 필드에서 제목과 내용 가져오기
    let title = document.getElementById("title").value.trim();
    let content = document.getElementById("content").value.trim();

    // 제목 또는 내용이 비어 있으면 알림을 띄우고 종료
    if (!title || !content) {
        alert("제목과 내용을 입력해주세요.");
        return;
    }

    // 새로운 공지사항 객체 생성
    let newNotice = {
        title: title,
        author: "사용자", // 실제 로그인한 사용자 정보를 서버에서 처리할 수 있음
        date: new Date().toISOString().split("T")[0], // 현재 날짜 (YYYY-MM-DD 형식)
        views: 0, // 조회수 기본값 0
        content: content
    };

    try {
        // 서버에 공지사항 추가 요청 (POST 요청)
        let response = await fetch("/api/notices", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(newNotice) // 객체를 JSON 문자열로 변환하여 전송
        });

        // 응답이 정상적이지 않으면 오류 처리
        if (!response.ok) {
            throw new Error("공지사항 추가에 실패했습니다.");
        }

        // 성공적으로 추가되었음을 알리고 공지 목록 페이지로 이동
        alert("공지사항이 추가되었습니다.");
        window.location.href = "/mainnotice"; // 공지 목록 페이지로 리디렉션
    } catch (error) {
        // 오류 발생 시 콘솔에 출력하고 사용자에게 알림
        console.error("Error:", error);
        alert("오류가 발생했습니다. 다시 시도해주세요.");
    }
}
