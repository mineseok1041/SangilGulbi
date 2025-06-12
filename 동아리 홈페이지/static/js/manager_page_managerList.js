document.addEventListener("DOMContentLoaded", function () {
    const selectAll = document.querySelector(".selectAll");
    const checkboxes = document.querySelectorAll(".userCheckbox");
    const searchInput = document.querySelector(".searchInput");
    const rows = document.querySelectorAll("tbody tr");
    const selectedUsers = document.querySelector(".selectedUsers");
    const selectedList = document.querySelector(".selectedList");

    function updateSelectedUsers() {
        selectedList.innerHTML = "";
        let hasSelection = false;

        checkboxes.forEach((checkbox, index) => {
            if (checkbox.checked) {
                hasSelection = true;
                if (rows[index] && rows[index].cells.length > 1) {
                    const userName = rows[index].cells[1].textContent;

                    const userBox = document.createElement("div");
                    userBox.classList.add("selectedUserBox");

                    const icon = document.createElement("img");
                    icon.src = "../img/user_profile.png";
                    icon.alt = "User Icon";

                    const nameSpan = document.createElement("span");
                    nameSpan.textContent = userName;

                    userBox.appendChild(icon);
                    userBox.appendChild(nameSpan);
                    selectedList.appendChild(userBox);
                }
            }
        });

        selectedUsers.style.display = hasSelection ? "block" : "none";
    }

    if (selectAll) {
        selectAll.addEventListener("change", function () {
            checkboxes.forEach(cb => cb.checked = selectAll.checked);
            updateSelectedUsers();
        });
    }

    checkboxes.forEach(cb => cb.addEventListener("change", updateSelectedUsers));

    searchInput.addEventListener("input", function () {
        const keyword = searchInput.value.trim().toLowerCase();

        rows.forEach(row => {
            const name = row.cells[1]?.textContent.trim().toLowerCase(); // 이름 열 (2번째 열)

            if (!keyword) {
                // 검색창이 비어 있으면 모든 행 표시
                row.style.display = "";
            } else if (name && name.includes(keyword)) {
                // 검색어와 일치하면 표시
                row.style.display = "";
            } else {
                // 일치하지 않으면 숨김
                row.style.display = "none";
            }
        });
    });
});

// 모달 열기
function openModal(modalClass) {
    const modal = document.querySelector("." + modalClass);
    if (modal) modal.style.display = "flex";
}

// 모달 닫기
function closeModal(modalClass) {
    const modal = document.querySelector("." + modalClass);
    if (modal) modal.style.display = "none";
}

// 모달 바깥쪽 클릭 시 닫기
window.onclick = function(event) {
    document.querySelectorAll('.modal').forEach(modal => {
        if (event.target === modal) modal.style.display = "none";
    });
}

// 비밀번호 보기/숨기기 토글 함수
function togglePasswordVisibility(inputClass, icon) {
    const input = document.querySelector("." + inputClass);
    if (!input || !icon) return;

    if (input.type === "password") {
        input.type = "text";
        icon.src = icon.getAttribute("data-show");
    } else {
        input.type = "password";
        icon.src = icon.getAttribute("data-hide");
    }
}

// 비밀번호 함수
function addManagerButton() {
    const password = document.querySelector('.Password').value;
    const managerPassword = document.querySelector('.managerPassword').value;
    const confirmPassword = document.querySelector('.confirmPassword').value;
    const confirmManagerPassword = document.querySelector('.confirmManagerPassword').value;

    if (password === "" || confirmPassword === "" || managerPassword === "" || confirmManagerPassword === "") {
        alert("모든 비밀번호를 입력해 주세요.");
        return;
    }

    if (password !== confirmPassword) {
        alert("비밀번호와 비밀번호 확인이 일치하지 않습니다.");
        return;
    }

    if (managerPassword !== confirmManagerPassword) {
        alert("관리자 비밀번호와 관리자 비밀번호 확인이 일치하지 않습니다.");
        return;
    }

    const passwordRegex = /^(?=.*[A-Za-z])(?=.*\d)(?=.*[!@#$%^&*])[^\s]{8,}$/;
    if (!passwordRegex.test(password)) {
        alert("비밀번호는 영어, 숫자, 특수문자가 포함되어야 하며 최소 8자 이상이어야 합니다.");
        return;
    }

    if (!passwordRegex.test(managerPassword)) {
        alert("관리자 비밀번호는 영어, 숫자, 특수문자가 포함되어야 하며 최소 8자 이상이어야 합니다.");
        return;
    }

    alert("비밀번호가 변경되었습니다.");
    // 여기서 서버로 변경된 비밀번호 전송 코드 추가 가능
}

// 선택된 관리자 삭제 확인
function confirmDeleteManagers() {
    const selectedIds = Array.from(document.querySelectorAll(".userCheckbox:checked"))
        .map(cb => cb.closest("tr").querySelector("td:nth-child(3)").textContent.trim());

    if (selectedIds.length === 0) {
        alert("삭제할 관리자를 선택하세요.");
        return;
    }

    if (confirm("선택한 관리자를 삭제하시겠습니까?")) {
        fetch("/management/delete_manager", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ ids: selectedIds }),
        })
        .then(response => {
            if (response.ok) {
                alert("삭제가 완료되었습니다.");
                location.reload();
            } else {
                alert("삭제 중 오류가 발생했습니다.");
            }
        });
    }
}