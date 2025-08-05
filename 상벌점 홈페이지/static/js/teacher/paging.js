document.addEventListener("DOMContentLoaded", function () {
    const currentPage = parseInt(document.getElementById("currentPage").value);
    const maxPage = parseInt(document.getElementById("maxPage").value);

    const pageButtons = document.querySelectorAll(".pageNation-btn");

    const prevButton = pageButtons[0]; // ← 버튼
    const nextButton = pageButtons[2]; // → 버튼

    if (currentPage <= 1) {
        prevButton.classList.add("disabled");
        prevButton.disabled = true;
    }

    if (currentPage >= maxPage) {
        nextButton.classList.add("disabled");
        nextButton.disabled = true;
    }
});