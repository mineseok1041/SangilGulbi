from flask import Blueprint, render_template, request, redirect, url_for, session
from noticeDTO import NoticeDTO
from noticeSVC import NoticeSVC
from usersSVC import usersSVC
from usersDTO import usersDTO
from pointSVC import pointSVC
from pointLogDTO import pointLogDTO

studentBlue = Blueprint('student', __name__, url_prefix='/student')
usersSVC = usersSVC()
pointSVC = pointSVC()
noticeSVC = NoticeSVC()

@studentBlue.route('/')
def index():
    try:
        if 'id' not in session:
            return redirect(url_for('auth.login'))
        respDTO = usersSVC.getUsersInfo(usersDTO(id=session['id']))
        pointLogList = pointSVC.getPointLogByStdID(usersDTO(id=session['id']))
        pointLogStudent = [usersSVC.getUsersInfo(usersDTO(id=log.studentId)) for log in pointLogList]
        pointLogTeacher = [usersSVC.getUsersInfo(usersDTO(id=log.giveTeacherId)) for log in pointLogList]
        notices = noticeSVC.get_all_notices()

        return render_template('student/indexStudent.html', usersDTO=respDTO, notices=notices, pointLogList=pointLogList, pointLogStudent=pointLogStudent, pointLogTeacher=pointLogTeacher)
    except Exception as e:
        print(e)
        return redirect(url_for('auth.login'))

@studentBlue.route('/pointLog')
def pointLog():
    if 'id' not in session:
        return redirect(url_for('auth.login'))

    respDTO = usersDTO(id=session['id'], name=session['name'], stdNum=session['stdNum'], identity=session['identity'])
    pointLogList = pointSVC.getPointLogByStdID(usersDTO(id=session['id']))
    
    return render_template('student/pointLogStudent.html', usersDTO=respDTO, pointLogList=pointLogList)


# ------------------ community(게시판) 기능 ------------------

@studentBlue.route('/community')
def communityList():
    if 'id' not in session:
        return redirect(url_for('index'))
    
    respDTO = usersDTO(id=session['id'], name=session['name'], stdNum=session['stdNum'], identity=session['identity'])
    notices = noticeSVC.get_all_notices()

    return render_template('student/communityStudent.html', notices=notices, usersDTO=respDTO)

@studentBlue.route('/community/<int:noticeId>')
def communityDetail(noticeId):
    if 'id' not in session:
        return redirect(url_for('index'))
    respDTO = usersDTO(id=session['id'], name=session['name'], stdNum=session['stdNum'], identity=session['identity'])
    notice = noticeSVC.get_notice_by_id(noticeId)
    return render_template('student/communityInfoStudent.html', notice=notice, usersDTO=respDTO)
