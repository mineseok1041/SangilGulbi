document.addEventListener('DOMContentLoaded', function () {
  const stars = document.querySelectorAll('.star');

  stars.forEach(function (star) {
    star.addEventListener('click', function () {
      star.classList.toggle('active');
    });
  });
      document.querySelector('.nav-toggle').addEventListener('click', function() {
    document.querySelector('.sidebar').classList.toggle('active');
});
});
