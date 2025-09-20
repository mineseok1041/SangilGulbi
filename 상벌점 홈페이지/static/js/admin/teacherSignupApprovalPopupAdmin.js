document.addEventListener("DOMContentLoaded", function () {
    const approveButtons = document.querySelectorAll(".approve");
    const rejectButtons = document.querySelectorAll(".reject");

    // 승인 버튼 클릭 이벤트
    approveButtons.forEach(button => {
        button.addEventListener("click", function () {
            const teacherId = button.getAttribute("data-id"); // 버튼의 data-id 속성에서 teacherId 가져오기
            if (!teacherId) {
                alert("선생님 ID가 없습니다.");
                return;
            }

            fetch("/admin/approveTeacher", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ teacherId }) // teacherId를 JSON으로 전달
            })
            .then(res => res.json())
            .then(data => {
                alert(data.message);
                if (data.success) {
                    location.reload();
                }
            })
            .catch(err => console.error("Error:", err));
        });
    });

    // 거부 버튼 클릭 이벤트
    rejectButtons.forEach(button => {
        button.addEventListener("click", function () {
            const teacherId = button.getAttribute("data-id");
            if (!teacherId) {
                alert("선생님 ID가 없습니다.");
                return;
            }

            fetch("/admin/rejectTeacher", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ teacherId })
            })
            .then(res => res.json())
            .then(data => {
                alert(data.message);
                if (data.success) {
                    location.reload();
                }
            })
            .catch(err => console.error("Error:", err));
        });
    });
});

window.resizeTo(320, 650);