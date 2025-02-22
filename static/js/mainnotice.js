let currentPage = 1;
let itemsPerPage = 5;
let searchKeyword = "";

document.addEventListener("DOMContentLoaded", function () {
    loadNotices();
    checkAdminControls(); // 관리자 권한 체크
    document.getElementById("searchBtn").addEventListener("click", searchNotices);
});

// ✅ 관리자 권한 체크 및 삭제 열 숨김 처리
function checkAdminControls() {
    let userRole = localStorage.getItem("userRole");
    let addNoticeBtn = document.querySelector(".add-box .add");
    let deleteColumnHeader = document.getElementById("delete-column");

    // 공지 추가 버튼 설정
    if (addNoticeBtn) {
        addNoticeBtn.style.display = userRole === "admin" ? "block" : "none";
    }

    // 삭제 열 헤더 숨김
    if (deleteColumnHeader) {
        deleteColumnHeader.style.display = userRole === "admin" ? "table-cell" : "none";
    }
}

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
        noticeList.innerHTML = `<tr><td colspan="5" style="text-align:center;">${message}</td></tr>`;
        document.getElementById("page-info").innerText = "0 / 0";
        return;
    }

    let totalPages = Math.ceil(filteredNotices.length / itemsPerPage);
    if (currentPage > totalPages) currentPage = totalPages || 1;

    let startIndex = (currentPage - 1) * itemsPerPage;
    let paginatedNotices = filteredNotices.slice(startIndex, startIndex + itemsPerPage);

    let userRole = localStorage.getItem("userRole");

    paginatedNotices.forEach((notice, index) => {
        let row = document.createElement("tr");
        row.innerHTML = `
            <td>${startIndex + index + 1}</td>
            <td class="notice-title" onclick="viewNotice(${notice.id})">${notice.title}</td>
            <td>${notice.author}</td>
            <td>${notice.date}</td>
            ${userRole === "admin" ? `<td class="delete-column"><button class="delete-btn" onclick="deleteNotice(${notice.id})">삭제</button></td>` : ""}
        `;
        noticeList.appendChild(row);
    });

    // ✅ 관리자 아닌 경우 삭제 버튼 숨김
    if (userRole !== "admin") {
        document.querySelectorAll(".delete-column").forEach(el => el.style.display = "none");
    }

    document.getElementById("page-info").innerText = `${currentPage} / ${totalPages}`;
}

// ✅ 공지 삭제 기능 (관리자만 가능)
function deleteNotice(id) {
    if (localStorage.getItem("userRole") !== "admin") {
        alert("삭제 권한이 없습니다.");
        return;
    }
    if (!confirm("정말 삭제하시겠습니까?")) return;

    let notices = JSON.parse(localStorage.getItem("notices")) || [];
    localStorage.setItem("notices", JSON.stringify(notices.filter(notice => notice.id !== id)));
    alert("공지사항이 삭제되었습니다.");
    loadNotices();
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
