document.addEventListener('DOMContentLoaded', function () {
  document.querySelectorAll('.approve').forEach(btn => {
    btn.addEventListener('click', function () {
      const teacherId = this.getAttribute('data-id');
      fetch('/teacher/approveTeacher', {
        method: 'POST',
        headers: {'Content-Type': 'application/x-www-form-urlencoded'},
        body: 'teacherId=' + encodeURIComponent(teacherId)
      })
      .then(res => res.json())
      .then(data => {
        if (data.success) location.reload();
        else alert(data.error || "승인 실패");
      });
    });
  });

  document.querySelectorAll('.reject').forEach(btn => {
    btn.addEventListener('click', function () {
      const teacherId = this.getAttribute('data-id');
      fetch('/teacher/deleteTeacherAccount', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({teacherId})
      })
      .then(res => res.json())
      .then(data => {
        if (data.success) location.reload();
        else alert(data.error || "거부 실패");
      });
    });
  });
});