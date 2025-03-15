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

function updatePoints(inputClass) {
    const user = document.querySelector(".userSelect").value;
    const reason = document.querySelector(".reasonSelect").options[document.querySelector(".reasonSelect").selectedIndex].text;
    const points = document.querySelector("." + inputClass).value;

    if (!user || !points) {
        alert("사용자와 사유를 선택해주세요.");
        return;
    }

    alert(`${user}에게 '${reason}' 사유로 ${points}점을 적용했습니다.`);


    
    
    // 실제 서버로 데이터 전송하는 로직을 추가하면 됨 (예: fetch API)
    // 예시:
    // fetch('/api/updatePoints', {
    //     method: 'POST',
    //     headers: {
    //         'Content-Type': 'application/json'
    //     },
    //     body: JSON.stringify({ user, reason, points })
    // }).then(response => {
    //     if (response.ok) {
    //         alert(`${points}점 등록이 완료되었습니다!`);
    //     } else {
    //         alert('점수 등록에 실패했습니다.');
    //     }
    // }).catch(error => {
    //     console.error('Error:', error);
    //     alert('점수 등록 중 오류가 발생했습니다.');
    // });

    // 점수 등록이 완료되었음을 알리는 메시지
    alert(`${points}점 등록이 완료되었습니다!`);
}

// 수상 내역 저장 함수
function saveAward() {
    const awardTitle = document.querySelector(".awardTitle").value;
    const awardDescription = document.querySelector(".awardDescription").value;

    if (!awardTitle || !awardDescription) {
        alert("수상 제목과 설명을 입력해주세요.");
        return;
    }

    alert(`수상 내역이 저장되었습니다.\n제목: ${awardTitle}\n설명: ${awardDescription}`);
    
    // 실제 서버로 데이터 전송하는 로직을 추가하면 됨 (예: fetch API)
    // 예시:
    // fetch('/api/saveAward', {
    //     method: 'POST',
    //     headers: {
    //         'Content-Type': 'application/json'
    //     },
    //     body: JSON.stringify({ awardTitle, awardDescription })
    // }).then(response => {
    //     if (response.ok) {
    //         alert('수상 내역이 저장되었습니다.');
    //     } else {
    //         alert('수상 내역 저장에 실패했습니다.');
    //     }
    // }).catch(error => {
    //     console.error('Error:', error);
    //     alert('수상 내역 저장 중 오류가 발생했습니다.');
    // });
}