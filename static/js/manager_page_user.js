document.addEventListener("DOMContentLoaded", function () {
    const selectAll = document.getElementById("selectAll");
    const checkboxes = document.querySelectorAll(".userCheckbox");
    const searchInput = document.getElementById("searchInput");
    const rows = document.querySelectorAll("tbody tr");
    const selectedUsers = document.getElementById("selectedUsers");
    const selectedList = document.getElementById("selectedList");

    function updateSelectedUsers() {
        selectedList.innerHTML = "";
        let hasSelection = false;

        checkboxes.forEach((checkbox, index) => {
            if (checkbox.checked) {
                hasSelection = true;
                const userName = rows[index].cells[1].textContent;

                const userBox = document.createElement("div");
                userBox.classList.add("selected-user-box");

                const icon = document.createElement("img");
                icon.src = "../img/user_profile.png";
                icon.alt = "User Icon";

                const nameSpan = document.createElement("span");
                nameSpan.textContent = userName;

                userBox.appendChild(icon);
                userBox.appendChild(nameSpan);
                selectedList.appendChild(userBox);
            }
        });

        selectedUsers.style.display = hasSelection ? "block" : "none";
    }

    selectAll.addEventListener("change", function () {
        checkboxes.forEach(cb => cb.checked = selectAll.checked);
        updateSelectedUsers();
    });

    checkboxes.forEach(cb => cb.addEventListener("change", updateSelectedUsers));

    searchInput.addEventListener("input", function () {
        const keyword = searchInput.value.toLowerCase();
        rows.forEach(row => row.style.display = row.innerText.toLowerCase().includes(keyword) ? "" : "none");
    });
});

// 모달 열기
function openModal(modalId) {
    var modal = document.getElementById(modalId);
    modal.style.display = "flex"; // 모달을 flex로 보이게 함
}

// 모달 닫기
function closeModal(modalId) {
    var modal = document.getElementById(modalId);
    modal.style.display = "none"; // 모달을 숨김
}

// 모달 바깥쪽 클릭 시 닫기 (옵션)
window.onclick = function(event) {
    var modals = document.querySelectorAll('.modal');
    modals.forEach(function(modal) {
        if (event.target === modal) {
            modal.style.display = "none"; // 바깥 영역 클릭 시 모달 닫기
        }
    });
}

// 비밀번호 보기/숨기기 토글 함수
function togglePasswordVisibility(inputId, icon) {
    var input = document.getElementById(inputId);

    if (input.type === "password") {
        input.type = "text"; // 비밀번호 보이게 설정
        icon.src = icon.getAttribute("data-show"); // 보임 아이콘으로 변경
    } else {
        input.type = "password"; // 비밀번호 숨기기
        icon.src = icon.getAttribute("data-hide"); // 숨김 아이콘으로 변경
    }
}
// 비밀번호 변경 함수
function changePassword() {
    var newPassword = document.getElementById('newPassword').value;
    var confirmPassword = document.getElementById('confirmPassword').value;

    // 비밀번호가 일치하는지 확인
    if (newPassword === "" || confirmPassword === "") {
        alert("비밀번호를 입력해 주세요.");
        return;
    }

    if (newPassword !== confirmPassword) {
        alert("새 비밀번호와 비밀번호 확인이 일치하지 않습니다.");
        return;
    }

    // 비밀번호가 조건을 만족하는지 체크
    var passwordRegex = /^(?=.*[A-Za-z])(?=.*\d)(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{8,}$/;
    if (!passwordRegex.test(newPassword)) {
        alert("비밀번호는 영어, 숫자, 특수문자가 포함되어야 하며 최소 8자 이상이어야 합니다.");
        return;
    }

    // 비밀번호가 조건을 만족하면 비밀번호 변경 작업을 처리
    alert("비밀번호가 변경되었습니다.");
    // 여기에 서버로 변경된 비밀번호를 전송하는 코드가 필요함.
}

