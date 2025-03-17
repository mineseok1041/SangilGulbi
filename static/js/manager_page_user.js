document.addEventListener("DOMContentLoaded", function() {
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

    selectAll.addEventListener("change", function() {
        checkboxes.forEach(cb => cb.checked = selectAll.checked);
        updateSelectedUsers();
    });

    checkboxes.forEach(cb => cb.addEventListener("change", updateSelectedUsers));

    searchInput.addEventListener("input", function() {
        const keyword = searchInput.value.toLowerCase();
        rows.forEach(row => row.style.display = row.innerText.toLowerCase().includes(keyword) ? "" : "none");
    });
});

// 모달 열기
function openModal(modalClass) {
    var modal = document.querySelector("." + modalClass);
    modal.style.display = "flex"; // 모달을 flex로 보이게 함
}

// 모달 닫기
function closeModal(modalClass) {
    var modal = document.querySelector("." + modalClass);
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
function togglePasswordVisibility(inputClass, icon) {
    var input = document.querySelector("." + inputClass);

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
    var newPassword = document.querySelector('.newPassword').value;
    var confirmPassword = document.querySelector('.confirmPassword').value;

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

function updatePointValue(selectClass, inputClass) {
    const select = document.querySelector("." + selectClass);
    const input = document.querySelector("." + inputClass);
    const customInputContainer = select.nextElementSibling;
    const customInput = customInputContainer.querySelector('.customInput');

    const selectedOption = select.options[select.selectedIndex];

    if (selectedOption.value === "custom") {
        customInputContainer.style.display = 'block';
        input.removeAttribute('readonly');
        input.value = "0";
        input.focus();
    } else {
        customInputContainer.style.display = 'none';
        input.setAttribute('readonly', true);
        input.value = selectedOption.value;
    }
}

document.querySelectorAll('.rewardInput, .penaltyInput').forEach(input => {
    input.addEventListener('input', function() {
        if (this.className === 'penaltyInput' && this.value > 0) {
            this.value = 0;
        }
    });
});

document.querySelectorAll('.customInput').forEach(input => {
    input.addEventListener('input', function() {
        const penaltyInput = document.querySelector('.penaltyInput');
        penaltyInput.value = this.value;
    });
});

$(document).ready(function() {
    $("#submitBtnAdd").click(function() {
        var formId = $(this).data("form"); // 눌린 버튼의 data-form 속성 값 가져오기
        var formData = $("#" + formId).serialize(); // 해당 폼의 데이터 직렬화

        var checkedUserIds = [];
        $(".userCheckbox:checked").each(function() {
            checkedUserIds.push($(this).attr("name")); // 체크된 항목의 name 값(=user.id) 추가
        });

        if (checkedUserIds.length === 0) {
            alert("적어도 한 명 이상의 사용자를 선택하세요.");
            return;
        }

        formData += "&userIds=" + checkedUserIds.join(",");

        $.ajax({
            type: "POST",
            url: "/management/addPoint.do",
            data: formData,
            dataType: "json",
            success: function(data) {
                alert(data.message);
                location.reload();
            },
            error: function(request, status, error) {
                alert("상점 부여에 실패했습니다");
                location.reload();
            }
        });
    });
});

$(document).ready(function() {
    $("#submitBtnDel").click(function() {
        var formId = $(this).data("form"); // 눌린 버튼의 data-form 속성 값 가져오기
        var formData = $("#" + formId).serialize(); // 해당 폼의 데이터 직렬화

        var checkedUserIds = [];
        $(".userCheckbox:checked").each(function() {
            checkedUserIds.push($(this).attr("name")); // 체크된 항목의 name 값(=user.id) 추가
        });

        if (checkedUserIds.length === 0) {
            alert("적어도 한 명 이상의 사용자를 선택하세요.");
            return;
        }

        formData += "&userIds=" + checkedUserIds.join(",");

        $.ajax({
            type: "POST",
            url: "/management/addPoint.do",
            data: formData,
            dataType: "json",
            success: function(data) {
                alert(data.message);
                location.reload();
            },
            error: function(request, status, error) {
                alert("벌점 부여에 실패했습니다");
                location.reload();
            }
        });
    });
});