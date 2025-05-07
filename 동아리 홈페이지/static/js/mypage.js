const info_openPopup = () => {
    // 팝업을 띄울 페이지 URL
    var popupURL = "mypage_InfoPopup.html";
    // 팝업 창의 속성
    var option = "width=600,height=400,scrollbars=yes";
    // 팝업 열기
    window.open(popupURL, "Popup", option);
  }

  const info_closePopup = () => {
    // 팝업 닫기
    window.close();
  }

  const score_openPopup = () => {
    // 팝업을 띄울 페이지 URL
    var popupURL = "mypage_ScorePopup.html";
    // 팝업 창의 속성
    var option = "width=600,height=400,scrollbars=yes";
    // 팝업 열기
    window.open(popupURL, "Popup", option);
  }

  const score_closePopup = () => {
    // 팝업 닫기
    window.close();
  }