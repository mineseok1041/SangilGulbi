document.addEventListener('DOMContentLoaded', function () {
  const stars = document.querySelectorAll('.star');

  stars.forEach(function (star) {
    star.addEventListener('click', async function () {
      const pointNo = star.dataset.pointno;
      const isActive = star.classList.contains('active');

      try {
        if (isActive) {
          await fetch(`/teacher/removeFavoritePointReason.do/${pointNo}`, { method: 'POST' });
          star.classList.remove('active');
        } else {
          await fetch(`/teacher/addFavoritePointReason.do/${pointNo}`, { method: 'POST' });
          star.classList.add('active');
        }
      } catch (err) {
        alert('즐겨찾기 처리 중 오류가 발생했습니다.');
        console.error(err);
      }
    });
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
