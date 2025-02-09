function loadNotices() {
    let noticeList = document.getElementById("notice-list");
    noticeList.innerHTML = ""; // 기존 목록 초기화

    let notices = JSON.parse(localStorage.getItem("notices")) || [];

    // 페이징 처리
    let startIndex = (currentPage - 1) * itemsPerPage;
    let endIndex = startIndex + itemsPerPage;
    let paginatedNotices = notices.slice(startIndex, endIndex);

    paginatedNotices.forEach((notice, index) => {
        let row = document.createElement("tr");
        row.innerHTML = `
            <td>${startIndex + index + 1}</td>
            <td>${notice.title}</td>
            <td>${notice.author}</td>
            <td>${notice.date}</td>
            <td>${notice.views}</td>
        `;
        noticeList.appendChild(row);
    });

    document.getElementById("page-info").innerText = `${currentPage} / ${Math.ceil(notices.length / itemsPerPage)}`;

    // 🔥 테이블 아래 회색 줄이 유지되도록 다시 추가
    addTableFooter();
}

function addTableFooter() {
    let container = document.querySelector(".container"); // 전체 컨테이너 선택
    let existingFooter = document.querySelector(".table-footer");

    if (existingFooter) {
        existingFooter.remove(); // 기존 footer 제거 후 다시 추가
    }

    let footer = document.createElement("div");
    footer.className = "table-footer";

    for (let i = 0; i < 5; i++) {
        let line = document.createElement("div");
        line.style.width = "75%";
        line.style.height = "1px";
        line.style.backgroundColor = "lightgray";
        line.style.margin = "10px 0";
        footer.appendChild(line);
    }

    container.appendChild(footer); // 컨테이너 맨 아래 추가
}

function prevPage() {
    if (currentPage > 1) {
        currentPage--;
        loadNotices();
        addTableFooter(); // 🔥 페이지 변경 시 다시 추가
    }
}

function nextPage() {
    let notices = JSON.parse(localStorage.getItem("notices")) || [];
    if (currentPage < Math.ceil(notices.length / itemsPerPage)) {
        currentPage++;
        loadNotices();
        addTableFooter(); // 🔥 페이지 변경 시 다시 추가
    }
}
