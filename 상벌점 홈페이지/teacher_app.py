from flask import Blueprint, render_template, request, redirect, url_for, session
from noticeDTO import NoticeDTO
from noticeSVC import NoticeSVC

teacherBlue = Blueprint('teacher', __name__, url_prefix='/teacher')
SVC = NoticeSVC()

@teacherBlue.route('/')
def index():
    try:
        if 'id' not in session:
            return redirect(url_for('index'))
        notices = SVC.get_all_notices()  # 게시글 목록 가져오기
        return render_template('teacher/indexTeacher.html', notices=notices)
    except Exception as e:
        print(e)
        return redirect(url_for('index'))

@teacherBlue.route('/pointLog')
def pointLog():
    try:
        if 'id' not in session:
            return redirect(url_for('index'))
        return render_template('teacher/givePointLog.html')
    except Exception as e:
        print(e)
        return redirect(url_for('index'))

@teacherBlue.route('/studentManagement')
def studentManagement():
    try:
        if 'id' not in session:
            return redirect(url_for('index'))
        return render_template('teacher/studentManagement.html')
    except Exception as e:
        print(e)
        return redirect(url_for('index'))

@teacherBlue.route('/teacherManagement')
def teacherManagement():
    try:
        if 'id' not in session:
            return redirect(url_for('index'))
        return render_template('teacher/teacherManagement.html')
    except Exception as e:
        print(e)
        return redirect(url_for('index'))

# ------------------ community(게시판) 기능 ------------------

@teacherBlue.route('/community')
def communityList():
    try:
        if 'id' not in session:
            return redirect(url_for('index'))
        notices = SVC.get_all_notices()
        return render_template('teacher/communityTeacher.html', notices=notices)
    except Exception as e:
        print(e)
        return redirect(url_for('index'))

@teacherBlue.route('/community/<int:noticeId>')
def communityDetail(noticeId):
    try:
        if 'id' not in session:
            return redirect(url_for('index'))
        notice = SVC.get_notice_by_id(noticeId)
        return render_template('teacher/communityInfoTeacher.html', notice=notice)
    except Exception as e:
        print(e)
        return redirect(url_for('teacher.communityList'))

@teacherBlue.route('/community/add', methods=['GET', 'POST'])
def communityAdd():
    try:
        if 'id' not in session:
            return redirect(url_for('index'))
        if request.method == 'POST':
            title = request.form['title']
            content = request.form['content']
            author = session['id']
            notice = NoticeDTO(title=title, content=content, author=author)
            SVC.add_notice(notice)
            return redirect(url_for('teacher.communityList'))
        return render_template('teacher/communityAddTeacher.html')
    except Exception as e:
        print(e)
        return redirect(url_for('teacher.communityList'))

@teacherBlue.route('/community/edit/<int:noticeId>', methods=['GET', 'POST'])
def communityEdit(noticeId):
    try:
        if 'id' not in session:
            return redirect(url_for('index'))
        notice = SVC.get_notice_by_id(noticeId)
        if request.method == 'POST':
            notice.title = request.form['title']
            notice.content = request.form['content']
            # notice.author = notice.author
            SVC.update_notice(notice)
            return redirect(url_for('teacher.communityDetail', noticeId=noticeId))
        return render_template('teacher/communityEditTeacher.html', notice=notice)
    except Exception as e:
        print(e)
        return redirect(url_for('teacher.communityList'))

@teacherBlue.route('/community/delete/<int:noticeId>', methods=['POST'])
def communityDelete(noticeId):
    try:
        if 'id' not in session:
            return redirect(url_for('index'))
        SVC.delete_notice(noticeId)
        return redirect(url_for('teacher.communityList'))
    except Exception as e:
        print(e)
        return redirect(url_for('teacher.communityList'))