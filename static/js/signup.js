$(document).ready(function() {
    
});
function togglePasswordVisibility(inputId, icon) {
    var input = document.getElementById(inputId);

    if (input.type === "password") {
        input.type = "text";
        setTimeout(() => {
            icon.src = icon.getAttribute("data-show");
        }, 10); // 지연을 줘서 밀림 방지
    } else {
        input.type = "password";
        setTimeout(() => {
            icon.src = icon.getAttribute("data-hide");
        }, 10);
    }
}

let isIDValid = false;

function checkIDValid() {
    var userId = $("#id").val();

    if (!userId.trim()) {
        $("#isValidID").text("아이디를 입력하세요.").css("color", "red");
        return;
    }

    $.ajax({
        type: "POST",
        url: "/users/IDcheck.do",
        data: { id: userId },
        dataType: "json",
        success: function(data) {
            $("#isValidID").text("사용 가능한 아이디입니다.").css("color", "green");
            isIDValid = true;
            updateSubmitButton();
        },
        error: function() {
            $("#isValidID").text("사용 중인 아이디입니다.").css("color", "red");
            isIDValid = false;
            updateSubmitButton();
        }
    });
}

function updateSubmitButton() {
    $(".join").prop("disabled", !isIDValid);
}

// 아이디 입력값이 변경되면 다시 중복 확인 필요
$("#id").on("input", function() {
    isIDValid = false;
    $("#isValidID").text("중복 확인을 해주세요.").css("color", "red");
    updateSubmitButton();
});

// 처음에는 회원가입 버튼 비활성화
updateSubmitButton();