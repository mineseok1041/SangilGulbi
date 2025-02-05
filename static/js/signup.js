alert("signup.js loaded");

function IDcheck() {
    let id = $("#id").val();

    $.ajax({
        url: "http://127.0.0.1:5000/student/IDcheck.do",
        type: "POST",
        dataType: "text",
        data: { id: id },
        success: function(response) {
            console.log(response);
            if (response == "true") {
                alert("사용 가능한 아이디입니다.");
            } else {
                alert("이미 사용중인 아이디입니다.");
            }
        },
        error: function(err) {
            console.error("Error occurred: ", err);
        },
    });
}