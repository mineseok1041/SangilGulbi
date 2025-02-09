const openPopup = () => {
    // 팝업을 띄울 페이지 URL
    var popupURL = "/mypage_Popup";
    // 팝업 창의 속성
    var option = "width=600,height=400,scrollbars=yes";
    // 팝업 열기
    window.open(popupURL, "Popup", option);
  }

  const closePopup = () => {
    // 팝업 닫기
    window.close();
  }