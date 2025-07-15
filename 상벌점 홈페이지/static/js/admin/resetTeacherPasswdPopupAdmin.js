document.addEventListener("DOMContentLoaded", function () {
    // 요소 캐싱
    const teacherSearchModal = document.querySelector(".teacherSearchModal");
    const modalContent = document.querySelector(".modalContent");
    const teacherRows = document.querySelectorAll(".teacherTable tbody tr");
    const teacherNameElement = document.querySelector(".teacherName");
    const teacherIdElement = document.querySelector(".teacherId");
    const teacherIdInput = document.querySelector(".teacherIdInput");
    const searchTeacherIcon = document.querySelector(".searchTeacherIcon");
    const togglePasswordIcons = document.querySelectorAll(".togglePassword");

    // URL 파라미터로 값이 있으면 화면에 표시
    const urlParams = new URLSearchParams(window.location.search);
    const teacherName = urlParams.get("teacherName") || "";
    const teacherId = urlParams.get("teacherId") || "";
    if (teacherName && teacherId) {
        teacherNameElement.textContent = teacherName;
        teacherIdElement.textContent = teacherId;
        teacherIdInput.value = teacherId;
    }

    // 비밀번호 토글 기능
    togglePasswordIcons.forEach(icon => {
        icon.addEventListener("click", function () {
            const passwordInput = icon.previousElementSibling;
            const isHidden = passwordInput.type === "password";
            passwordInput.type = isHidden ? "text" : "password";
            icon.src = isHidden ? "../static/img/eyeOnIcon.png" : "../static/img/eyeOffIcon.png";
            icon.alt = isHidden ? "Hide Password" : "Show Password";
        });
    });

    // 돋보기 아이콘 클릭 시 모달 열기
    searchTeacherIcon.addEventListener("click", function () {
        teacherSearchModal.classList.remove("hidden");
        teacherSearchModal.classList.add("visible");
    });

    // 모달 외부 클릭 시 닫기
    teacherSearchModal.addEventListener("click", function (event) {
        if (!modalContent.contains(event.target)) {
            teacherSearchModal.classList.remove("visible");
            teacherSearchModal.classList.add("hidden");
        }
    });

    // 선생님 목록 행 클릭 시 정보 반영 및 모달 닫기
    teacherRows.forEach(row => {
        row.addEventListener("click", function () {
            const tds = row.querySelectorAll("td");
            teacherNameElement.textContent = tds[0].textContent.trim();
            teacherIdElement.textContent = tds[1].textContent.trim();
            teacherIdInput.value = tds[1].textContent.trim();

            teacherSearchModal.classList.remove("visible");
            teacherSearchModal.classList.add("hidden");
        });
    });

    // ---------- 선생님 검색 ----------
    const teacherModalContent = teacherSearchModal.querySelector(".modalContent");
    const teacherSearchInput = document.querySelector(".teacherSearchModal .teacherSearchInput");
    const teacherSearchButton = document.querySelector(".teacherSearchModal .teacherSearchButton");
    const teacherTableBody = teacherSearchModal.querySelector(".teacherTable tbody");

    const giveTeacherNameElement = document.querySelector(".giveTeacherName");
    const giveTeacherIdElement = document.querySelector(".giveTeacherId");

    searchTeacherIcon.addEventListener("click", () => {
        teacherSearchModal.classList.remove("hidden");
        teacherSearchModal.classList.add("visible");
        loadTeachers("");
    });

    teacherSearchModal.addEventListener("click", function (event) {
        if (!teacherModalContent.contains(event.target)) {
            teacherSearchModal.classList.add("hidden");
        }
    });

    teacherSearchButton.addEventListener("click", () => {
        const keyword = teacherSearchInput.value.trim();
        loadTeachers(keyword);
    });

    function loadTeachers(keyword) {
        fetch(`/admin/searchTeachers?keyword=${encodeURIComponent(keyword)}`)
            .then(res => res.json())
            .then(data => {
                teacherTableBody.innerHTML = "";
                if (data.length === 0) {
                    teacherTableBody.innerHTML = "<tr><td colspan='2'>검색 결과 없음</td></tr>";
                    return;
                }
                data.forEach(teacher => {
                    const row = document.createElement("tr");
                    row.innerHTML = `
                        <td>${teacher.id}</td>
                        <td>${teacher.name}</td>
                    `;
                    row.addEventListener("click", () => {
                        giveTeacherIdElement.textContent = teacher.id;
                        giveTeacherNameElement.textContent = teacher.name;
                        teacherSearchModal.classList.add("hidden");
                    });
                    teacherTableBody.appendChild(row);
                });
            });
    }
});