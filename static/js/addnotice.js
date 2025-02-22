document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("addNoticeBtn").addEventListener("click", addNotice);
});

async function addNotice() {
    let title = document.getElementById("title").value.trim();
    let content = document.getElementById("content").value.trim();

    if (!title || !content) {
        alert("제목과 내용을 입력해주세요.");
        return;
    }

    let newNotice = {
        title: title,
        author: "사용자", // 실제 로그인한 사용자 정보를 서버에서 처리 가능
        date: new Date().toISOString().split("T")[0], // YYYY-MM-DD 형식
        views: 0,
        content: content
    };

    try {
        let response = await fetch("/api/notices", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(newNotice)
        });

        if (!response.ok) {
            throw new Error("공지사항 추가에 실패했습니다.");
        }

        alert("공지사항이 추가되었습니다.");
        window.location.href = "/mainnotice"; // 공지 목록 페이지로 이동
    } catch (error) {
        console.error("Error:", error);
        alert("오류가 발생했습니다. 다시 시도해주세요.");
    }
}
