document.addEventListener("DOMContentLoaded", function () {
    const table = document.querySelector(".pointLog_table");
    const tableBody = table.querySelector("tbody");
    const filterIcon = document.querySelector(".filterIcon");
    const filterPopup = document.querySelector(".filterPopup");
    const resetFiltersButton = filterPopup.querySelector(".resetFilters");
    const checkboxes = filterPopup.querySelectorAll("input[type='checkbox']");
    const pointCancelButton = document.querySelector(".pointCancel");
    const searchInput = document.querySelector(".searchBar .searchInput");
    const searchButton = document.querySelector(".searchButton");

    // 상세/선택 이벤트 등록 함수
    function bindRowEvents() {
        // 드롭다운 토글
        document.querySelectorAll('.main-row').forEach(row => {
            row.addEventListener('click', function () {
                const dropdown = row.nextElementSibling;
                if (!dropdown || !dropdown.classList.contains('dropdown-row')) return;
                const isOpen = dropdown.style.display === 'table-row';
                document.querySelectorAll('.dropdown-row').forEach(r => r.style.display = 'none');
                if (!isOpen) dropdown.style.display = 'table-row';
            });
        });

        // 선택 강조
        document.querySelectorAll('.main-row').forEach(row => {
            row.addEventListener("click", function (event) {
                event.stopPropagation();
                if (row.classList.contains("selected-row")) {
                    row.classList.remove("selected-row");
                } else {
                    document.querySelectorAll('.main-row').forEach(r => r.classList.remove("selected-row"));
                    row.classList.add("selected-row");
                }
            });
        });
    }

    // 날짜 형식 변경 함수
    function formatDateCell(cell) {
        if (!cell) return;
        const originalText = cell.textContent.trim();
        const match = originalText.match(/^(\d{4})(\d{2})(\d{2})/);
        if (match) {
            cell.textContent = `${match[1]}/${match[2]}/${match[3]}`;
        }
    }

    // 검색 버튼 클릭 이벤트
    searchButton.addEventListener("click", function () {
        const keyword = searchInput.value.trim();
        fetch(`/teacher/searchPointLogs?keyword=${encodeURIComponent(keyword)}`)
            .then(res => res.json())
            .then(data => {
                tableBody.innerHTML = "";
                data.forEach(log => {
                    // 메인 행
                    const mainRow = document.createElement("tr");
                    mainRow.className = "main-row";
                    mainRow.setAttribute("data-no", log.no);
                    mainRow.innerHTML = `
                        <td>${log.studentName}</td>
                        <td>${log.reason}</td>
                        <td>${log.point}</td>
                        <td>${log.giveTeacherName}</td>
                    `;

                    // 상세(드롭다운) 행 - 기존과 똑같이!
                    const dropdownRow = document.createElement("tr");
                    dropdownRow.className = "dropdown-row";
                    dropdownRow.style.display = "none";
                    dropdownRow.innerHTML = `
                        <td colspan="4" style="background:#f7f7f7;">
                            <div style="padding:10px;">
                                날짜 : <span class="date-cell">${log.addDate || ""}</span><br>
                                학번 : ${log.studentNum || ""}<br>
                                사유 : ${log.reason || ""}<br>
                                의견 : ${log.opinion || ""}<br>
                            </div>
                        </td>
                    `;

                    tableBody.appendChild(mainRow);
                    tableBody.appendChild(dropdownRow);

                    // 날짜 포맷
                    const dateCell = dropdownRow.querySelector('.date-cell');
                    formatDateCell(dateCell);
                });

                // 새로 그린 행에 이벤트 재등록
                bindRowEvents();
            });
    });

    // 엔터키로도 검색 가능하게
    searchInput.addEventListener("keydown", function (event) {
        if (event.key === "Enter") {
            searchButton.click();
        }
    });

    // 최초 로딩 시 기존 행 이벤트 바인딩
    bindRowEvents();

    // 날짜 형식 변경 (기존 행)
    document.querySelectorAll('.dropdown-row .date-cell').forEach(formatDateCell);

    // 외부 클릭 시 선택 해제
    document.addEventListener("click", function (event) {
        if (!table.contains(event.target)) {
            document.querySelectorAll('.main-row').forEach(row => row.classList.remove("selected-row"));
        }
    });

    // 필터 팝업 토글
    filterIcon.addEventListener("click", function (event) {
        event.stopPropagation();
        filterPopup.classList.toggle("hidden");
    });

    document.addEventListener("click", function (event) {
        if (!filterPopup.contains(event.target) && !filterIcon.contains(event.target)) {
            filterPopup.classList.add("hidden");
        }
    });

    // 필터 초기화
    resetFiltersButton.addEventListener("click", function () {
        checkboxes.forEach(checkbox => {
            checkbox.checked = false;
        });
        document.querySelectorAll('.main-row').forEach(row => {
            row.style.display = "";
        });
    });

    pointCancelButton.addEventListener("click", () => {
        const selectedRow = document.querySelector(".pointLog_table .selected-row");

        if (!selectedRow) {
            alert("취소할 로그를 선택해주세요");
            return;
        }

        const logNo = selectedRow.dataset.no;

        if (confirm("해당 상벌점 부여를 취소하시겠습니까?")) {
            fetch("/teacher/pointCancel.do", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ logNo })
            })
            .then(res => res.json())
            .then(data => {
                alert(data.message || "취소되었습니다.");
                location.reload();
            })
            .catch(err => {
                alert("오류가 발생했습니다.");
            });
        }
    });

    // ---------- 사이드바 토글 및 외부 클릭 닫기 ----------
    const navToggle = document.querySelector('.nav-toggle');
    const sidebar = document.querySelector('.sidebar');

    if (navToggle && sidebar) {
        // 햄버거 버튼 클릭
        navToggle.addEventListener('click', function(e) {
            e.stopPropagation(); // 이벤트 전파 방지
            sidebar.classList.toggle('active');
            document.body.classList.toggle('sidebar-open', sidebar.classList.contains('active'));
        });

        // 사이드바 내부 클릭 시 이벤트 전파 방지
        sidebar.addEventListener('click', function(e) {
            e.stopPropagation();
        });

        // 문서 전체 클릭 시 사이드바 닫기
        document.addEventListener('click', function() {
            if (sidebar.classList.contains('active')) {
                sidebar.classList.remove('active');
                document.body.classList.remove('sidebar-open');
            }
        });
    }
});