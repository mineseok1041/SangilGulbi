let currentPage = 1;
let itemsPerPage = 5;
let searchKeyword = "";

document.addEventListener("DOMContentLoaded", function () {
    loadNotices();
    document.getElementById("searchBtn").addEventListener("click", searchNotices);
});

function loadNotices() {
    let noticeList = document.querySelector(".notice-list");
    noticeList.innerHTML = "";

    let notices = JSON.parse(localStorage.getItem("notices")) || [];

    let filteredNotices = notices;

    if (searchKeyword.trim() !== "") {
        filteredNotices = notices.filter(notice => 
            notice.title.includes(searchKeyword) || 
            notice.author.includes(searchKeyword)
        );
    }

    if (filteredNotices.length === 0) {
        let message = searchKeyword.trim() !== "" 
            ? "검색어와 연관된 목록이 없습니다." 
            : "업로드 된 공지사항이 없습니다.";

        noticeList.innerHTML = `<tr><td colspan="6" style="text-align:center;">${message}</td></tr>`;
        document.getElementById("page-info").innerText = "0 / 0";
        return;
    }

    let totalPages = Math.ceil(filteredNotices.length / itemsPerPage);
    if (currentPage > totalPages) currentPage = totalPages || 1;

    let startIndex = (currentPage - 1) * itemsPerPage;
    let endIndex = startIndex + itemsPerPage;
    let paginatedNotices = filteredNotices.slice(startIndex, endIndex);

    paginatedNotices.forEach((notice, index) => {
        let row = document.createElement("tr");
        row.innerHTML = `
            <td>${startIndex + index + 1}</td>
            <td class="notice-title" onclick="viewNotice(${notice.id})">${notice.title}</td>
            <td>${notice.author}</td>
            <td>${notice.date}</td>
            <td>${notice.views}</td>
            <td><button class="delete-btn" onclick="deleteNotice(${notice.id})">삭제</button></td>
        `;
        noticeList.appendChild(row);
    });

    document.getElementById("page-info").innerText = `${currentPage} / ${totalPages}`;
}


// 🔥 공지 삭제 기능 추가
function deleteNotice(id) {
    if (!confirm("정말 삭제하시겠습니까?")) return;

    let notices = JSON.parse(localStorage.getItem("notices")) || [];
    let updatedNotices = notices.filter(notice => notice.id !== id);

    localStorage.setItem("notices", JSON.stringify(updatedNotices));
    alert("공지사항이 삭제되었습니다.");
    loadNotices();
}

function searchNotices() {
    searchKeyword = document.getElementById("search").value.trim();
    currentPage = 1;
    loadNotices();
}

function prevPage() {
    if (currentPage > 1) {
        currentPage--;
        loadNotices();
    }
}

function nextPage() {
    let notices = JSON.parse(localStorage.getItem("notices")) || [];

    if (searchKeyword.trim() !== "") {
        notices = notices.filter(notice => 
            notice.title.includes(searchKeyword) || 
            notice.author.includes(searchKeyword)
        );
    }

    let totalPages = Math.ceil(notices.length / itemsPerPage);
    if (currentPage < totalPages) {
        currentPage++;
        loadNotices();
    }
}

function viewNotice(id) {
    localStorage.setItem("selectedNotice", id);
    window.location.href = "/noticepage";
}
