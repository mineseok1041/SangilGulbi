document.addEventListener("DOMContentLoaded", function () {

    const dateCell = document.querySelectorAll('.date-cell');

    dateCell.forEach(cell => {
        const originalText = cell.textContent.trim(); // 예: "20250514 09:18:56"
        const datePart = originalText.split(' ')[0];  // "20250514"

        // 날짜 형식 변경
        const formattedDate = `${datePart.slice(0, 4)}/${datePart.slice(4, 6)}/${datePart.slice(6, 8)}`;

        cell.textContent = formattedDate; // "2025/05/14"
    });

    const noticeDate = document.querySelectorAll('.noticeDate');
    noticeDate.forEach(cell => {
        const originalText = cell.textContent.trim(); // 예: "20250514 09:18:56"
        const datePart = originalText.split(' ')[0];  // "20250514"

        // 날짜 형식 변경
        const formattedDate = `${datePart.slice(0, 4)}/${datePart.slice(4, 6)}/${datePart.slice(6, 8)}`;

        cell.textContent = formattedDate; // "2025/05/14"
    });
        const rows = document.querySelectorAll(".community tbody tr");
    rows.forEach((row, index) => {
        if (index >= 3) {
            row.style.display = "none"; // 8번째 이후 데이터 숨김
        }
    });
});

document.querySelector('.nav-toggle').addEventListener('click', function() {
    document.querySelector('.sidebar').classList.toggle('active');
});
