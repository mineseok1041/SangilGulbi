document.addEventListener("DOMContentLoaded", function () {
    const table = document.querySelector(".studentInfo_table");
    const tableRows = Array.from(document.querySelectorAll(".studentInfo_table tbody tr"));
    const tableBody = table.querySelector("tbody");
    const headers = document.querySelectorAll(".studentInfo_table thead th.sortable");
    const resetButton = document.querySelector(".resetPasswd");
    const bonusButton = document.querySelector(".giveBonus");
    const penaltyButton = document.querySelector(".givePenalty");
    const filterIcon = document.querySelector(".filterIcon");
    const filterPopup = document.querySelector(".filterPopup");
    const resetFiltersButton = filterPopup ? filterPopup.querySelector(".resetFilters") : null;
    const deleteButton = document.querySelector(".deleteAccount");
    const searchInput = document.querySelector(".searchBar .searchInput");
    const searchButton = document.querySelector(".searchButton");

    let selectedStudent = null;

    // 행 클릭 이벤트 추가
    tableRows.forEach(row => {
        row.addEventListener("click", function (event) {
            event.stopPropagation();

            if (row.classList.contains("selected-row")) {
                row.classList.remove("selected-row");
                selectedStudent = null;
            } else {
                tableRows.forEach(r => r.classList.remove("selected-row"));
                row.classList.add("selected-row");

                const studentNum = row.cells[0].textContent.trim();
                const studentName = row.cells[1].textContent.trim();
                const studentId = row.cells[2].textContent.trim();
                selectedStudent = { studentNum, studentName, studentId };
            }
        });
    });

    // 페이지 로드 시 기본 정렬 (학번순)
    const sortedRows = tableRows.sort((a, b) => {
        const aNumber = a.querySelector("td:nth-child(1)").textContent.trim();
        const bNumber = b.querySelector("td:nth-child(1)").textContent.trim();
        return aNumber.localeCompare(bNumber);
    });
    tableBody.innerHTML = "";
    sortedRows.forEach(row => tableBody.appendChild(row));

    // 테이블 외부 클릭 시 선택 해제
    document.addEventListener("click", function (event) {
        if (!table.contains(event.target)) {
            tableRows.forEach(row => row.classList.remove("selected-row"));
            selectedStudent = null;
        }
    });

    // 필터 아이콘 클릭 이벤트
    if (filterIcon && filterPopup) {
        filterIcon.addEventListener("click", function () {
            filterPopup.classList.toggle("hidden");
        });
    }

    // 초기화 버튼 클릭 이벤트
    if (resetFiltersButton) {
        resetFiltersButton.addEventListener("click", function () {
            const checkboxes = filterPopup.querySelectorAll("input[type='checkbox']");
            checkboxes.forEach(checkbox => {
                checkbox.checked = false;
            });
            tableRows.forEach(row => {
                row.style.display = "";
            });
        });
    }

    // 팝업 외부 클릭 시 팝업 닫기
    document.addEventListener("click", function (event) {
        if (filterPopup && !filterPopup.contains(event.target) && !filterIcon.contains(event.target)) {
            filterPopup.classList.add("hidden");
        }
    });

    // 비밀번호 재설정 팝업
    if (resetButton) {
        resetButton.addEventListener("click", function () {
            let studentNum = "";
            let studentName = "";
            let studentId = "";

            if (selectedStudent) {
                studentNum = selectedStudent.studentNum;
                studentName = selectedStudent.studentName;
                studentId = selectedStudent.studentId;
            }
            const popupWidth = 600;
            const popupHeight = 800;
            const left = (window.innerWidth - popupWidth) / 2 + window.screenX;
            const top = (window.innerHeight - popupHeight) / 2 + window.screenY;

            window.open(
                `/teacher/resetStudentPasswordPopup?studentNum=${studentNum}&studentName=${encodeURIComponent(studentName)}&studentId=${encodeURIComponent(studentId)}`,
                "비밀번호 재설정",
                `width=600,height=800,left=${left},top=${top}`
            );
        });
    }

    // 삭제 버튼 클릭 이벤트
    if (deleteButton) {
        deleteButton.addEventListener("click", function () {
            if (!selectedStudent) {
                alert("삭제할 학생을 선택하세요.");
                return;
            }
            const confirmDelete = confirm(`정말로 ${selectedStudent.studentName}(${selectedStudent.studentId}) 학생 계정을 삭제하시겠습니까?`);
            if (!confirmDelete) return;

            fetch("/teacher/deleteStudentAccount", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ studentId: selectedStudent.studentId })
            })
            .then(res => res.json())
            .then(data => {
                if (data.success) {
                    alert("계정이 삭제되었습니다.");
                    location.reload();
                } else {
                    alert(data.error || "삭제 중 오류가 발생했습니다.");
                }
            })
            .catch(() => alert("삭제 요청 중 오류가 발생했습니다."));
        });
    }

    // 벌점 부여 팝업
    if (penaltyButton) {
        penaltyButton.addEventListener("click", function () {
            let studentNum = "";
            let studentName = "";
            let studentId = "";

            if (selectedStudent) {
                studentNum = selectedStudent.studentNum;
                studentName = selectedStudent.studentName;
                studentId = selectedStudent.studentId;
            }
            const popupWidth = 1280;
            const popupHeight = 720;
            const left = (window.innerWidth - popupWidth) / 2 + window.screenX;
            const top = (window.innerHeight - popupHeight) / 2 + window.screenY;

            window.open(
                `/teacher/givePenaltyPoint?studentNum=${studentNum}&studentName=${encodeURIComponent(studentName)}&studentId=${encodeURIComponent(studentId)}`,
                "벌점 부여",
                `width=${popupWidth},height=${popupHeight},left=${left},top=${top}`
            );
        });
    }

    // 상점 부여 팝업
    if (bonusButton) {
        bonusButton.addEventListener("click", function () {
            let studentNum = "";
            let studentName = "";
            let studentId = "";

            if (selectedStudent) {
                studentNum = selectedStudent.studentNum;
                studentName = selectedStudent.studentName;
                studentId = selectedStudent.studentId;
            }
            const popupWidth = 1280;
            const popupHeight = 720;
            const left = (window.innerWidth - popupWidth) / 2 + window.screenX;
            const top = (window.innerHeight - popupHeight) / 2 + window.screenY;

            window.open(
                `/teacher/giveBonusPoint?studentNum=${studentNum}&studentName=${encodeURIComponent(studentName)}&studentId=${encodeURIComponent(studentId)}`,
                "상점 부여",
                `width=${popupWidth},height=${popupHeight},left=${left},top=${top}`
            );
        });
    }

    // 정렬 기능 추가
    headers.forEach(header => {
        header.addEventListener("click", function () {
            const columnIndex = header.getAttribute("data-column") - 1;
            const isAscending = header.classList.contains("asc");
            const direction = isAscending ? -1 : 1;

            headers.forEach(h => h.classList.remove("asc", "desc"));
            header.classList.add(isAscending ? "desc" : "asc");

            const sortedRows = tableRows.sort((a, b) => {
                const aText = a.querySelectorAll("td")[columnIndex].textContent.trim();
                const bText = b.querySelectorAll("td")[columnIndex].textContent.trim();

                // 숫자 정렬 (총 상벌점)
                if (columnIndex === 4) {
                    const aValue = parseFloat(aText.replace("+", ""));
                    const bValue = parseFloat(bText.replace("+", ""));
                    return (aValue - bValue) * direction;
                }

                // 날짜 정렬 (마지막 활동)
                if (columnIndex === 3) {
                    return (new Date(aText) - new Date(bText)) * direction;
                }

                // 일반 텍스트 정렬
                return aText > bText ? direction : aText < bText ? -direction : 0;
            });

            tableBody.innerHTML = "";
            sortedRows.forEach(row => tableBody.appendChild(row));
        });
    });
    const dateCell = document.querySelectorAll('.date-cell');

    dateCell.forEach(cell => {
        const originalText = cell.textContent.trim(); // 예: "20250514 09:18:56"
        const datePart = originalText.split(' ')[0];  // "20250514"

        // 날짜 형식 변경
        const formattedDate = `${datePart.slice(0, 4)}/${datePart.slice(4, 6)}/${datePart.slice(6, 8)}`;

        cell.textContent = formattedDate; // "2025/05/14"
    });

    searchButton.addEventListener("click", function () {
        const keyword = searchInput.value.trim();
        fetch(`/teacher/searchStudents?keyword=${encodeURIComponent(keyword)}`)
            .then(res => res.json())
            .then(data => {
                tableBody.innerHTML = "";
                data.forEach(student => {
                    const tr = document.createElement("tr");
                    tr.innerHTML = `
                        <td>${student.stdNum ?? ""}</td>
                        <td>${student.name ?? ""}</td>
                        <td>${student.id ?? ""}</td>
                        <td>${student.lastlogindate ?? ""}</td>
                        <td>${student.point ?? ""}</td>
                    `;
                    tableBody.appendChild(tr);
                });
            });
    });

    // 엔터키로도 검색 가능하게
    searchInput.addEventListener("keydown", function (event) {
        if (event.key === "Enter") {
            event.preventDefault();
            searchButton.click();
        }
    });
});