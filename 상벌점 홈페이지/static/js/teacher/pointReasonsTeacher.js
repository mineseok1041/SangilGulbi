document.addEventListener('DOMContentLoaded', function () {
  const stars = document.querySelectorAll('.star');

  stars.forEach(function (star) {
    star.addEventListener('click', function () {
      star.classList.toggle('active');
    });
  });
});
