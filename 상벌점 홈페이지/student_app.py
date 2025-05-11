from flask import Blueprint, render_template, request, redirect, url_for, session
from noticeDTO import NoticeDTO
from noticeSVC import NoticeSVC
from usersSVC import usersSVC
from usersDTO import usersDTO

studentBlue = Blueprint('student', __name__, url_prefix='/student')
usersSVC = usersSVC()
noticeSVC = NoticeSVC()

@studentBlue.route('/')
def index():
    try:
        if 'id' not in session:
            return redirect(url_for('index'))
        respDTO = usersSVC.getUsersInfo(usersDTO(id=session['id']))
        notices = noticeSVC.get_all_notices()
        return render_template('student/indexStudent.html', usersDTO=respDTO, notices=notices)
    except Exception as e:
        print(e)
        return redirect(url_for('index'))

@studentBlue.route('/pointLog')
def pointLog():
    if 'id' not in session:
        return redirect(url_for('index'))
    return render_template('student/pointLogStudent.html')

# ------------------ community(게시판) 기능 ------------------

@studentBlue.route('/community')
def communityList():
    if 'id' not in session:
        return redirect(url_for('index'))
    notices = noticeSVC.get_all_notices()
    return render_template('student/communityStudent.html', notices=notices)

@studentBlue.route('/community/<int:noticeId>')
def communityDetail(noticeId):
    if 'id' not in session:
        return redirect(url_for('index'))
    notice = noticeSVC.get_notice_by_id(noticeId)
    return render_template('student/communityInfoStudent.html', notice=notice)