let currentPage = 1;
let itemsPerPage = 5;
let searchKeyword = "";

document.addEventListener("DOMContentLoaded", function () {
    loadNotices();
    document.getElementById("searchBtn").addEventListener("click", searchNotices);
});

// ✅ 공지사항 목록 로드
function loadNotices() {
    let noticeList = document.querySelector(".notice-list");
    noticeList.innerHTML = "";

    let notices = JSON.parse(localStorage.getItem("notices")) || [];
    let filteredNotices = searchKeyword.trim() !== ""
        ? notices.filter(notice => notice.title.includes(searchKeyword) || notice.author.includes(searchKeyword))
        : notices;

    if (filteredNotices.length === 0) {
        let message = searchKeyword.trim() !== "" 
            ? "검색어와 연관된 목록이 없습니다." 
            : "업로드 된 공지사항이 없습니다.";
        noticeList.innerHTML = `<tr><td colspan="4" style="text-align:center;">${message}</td></tr>`; // 🔥 삭제 버튼 칼럼 제외
        document.getElementById("page-info").innerText = "0 / 0";
        return;
    }

    let totalPages = Math.ceil(filteredNotices.length / itemsPerPage);
    if (currentPage > totalPages) currentPage = totalPages || 1;

    let startIndex = (currentPage - 1) * itemsPerPage;
    let paginatedNotices = filteredNotices.slice(startIndex, startIndex + itemsPerPage);

    paginatedNotices.forEach((notice, index) => {
        let row = document.createElement("tr");
        row.innerHTML = `
            <td>${startIndex + index + 1}</td>
            <td class="notice-title" onclick="viewNotice(${notice.id})">${notice.title}</td>
            <td>${notice.author}</td>
            <td>${notice.date}</td>
        `;
        noticeList.appendChild(row);
    });

    document.getElementById("page-info").innerText = `${currentPage} / ${totalPages}`;
}

// ✅ 검색 기능
function searchNotices() {
    searchKeyword = document.getElementById("search").value.trim();
    currentPage = 1;
    loadNotices();
}

// ✅ 페이지 이동
function prevPage() {
    if (currentPage > 1) {
        currentPage--;
        loadNotices();
    }
}

function nextPage() {
    let notices = JSON.parse(localStorage.getItem("notices")) || [];
    if (searchKeyword.trim() !== "") {
        notices = notices.filter(notice => notice.title.includes(searchKeyword) || notice.author.includes(searchKeyword));
    }
    if (currentPage < Math.ceil(notices.length / itemsPerPage)) {
        currentPage++;
        loadNotices();
    }
}

// ✅ 공지 상세 보기
function viewNotice(id) {
    localStorage.setItem("selectedNotice", id);
    window.location.href = "/noticepage";
}
