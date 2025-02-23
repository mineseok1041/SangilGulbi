const openPopup = () => {
  // 팝업 띄울 페이지 URL
  var popupURL = "/mypage_Popup";
  // 팝업 창 속성
  var option = "width=600,height=400,scrollbars=yes";
  window.open(popupURL, "Popup", option);
}

const closePopup = () => {
  window.close();
}