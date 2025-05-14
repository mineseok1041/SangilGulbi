from flask import Flask, redirect, render_template, session, url_for, Blueprint, request, flash

from usersSVC import usersSVC
from usersDTO import usersDTO
from pointSVC import pointSVC
from pointReasonDTO import pointReasonDTO
from pointLogDTO import pointLogDTO
from noticeDTO import NoticeDTO
from noticeSVC import NoticeSVC

teacherBlue = Blueprint('teacher', __name__, url_prefix='/teacher')
SVC = NoticeSVC()

usersSVC = usersSVC()
pointSVC = pointSVC()

@teacherBlue.route('/')
def index():
    try:
        if 'id' not in session:
            return redirect(url_for('index'))
        
        teacherDTO = usersDTO(id=session['id'], name=session['name'], identity=session['identity'])
        studentList = usersSVC.getStudentsList(1)
        teacherList = usersSVC.getTeachersList(1)
        notices = SVC.get_all_notices()  # 게시글 목록 가져오기
    
        return render_template('teacher/indexTeacher.html', usersDTO=teacherDTO, notices=notices, studentList=studentList, teacherList=teacherList)
    except Exception as e:
        print(e)
        return redirect(url_for('index'))

@teacherBlue.route('/pointLog')
def pointLog():
    try:
        if 'id' not in session:
            return redirect(url_for('index'))
        
        teacherDTO = usersDTO(id=session['id'], name=session['name'], identity=session['identity'])
        pointLogList = pointSVC.getPointLog(1)
        pointLogStudent = [usersSVC.getUsersInfo(usersDTO(id=log.studentId)) for log in pointLogList]
        pointLogTeacher = [usersSVC.getUsersInfo(usersDTO(id=log.giveTeacherId)) for log in pointLogList]
    
        return render_template('teacher/givePointLog.html', usersDTO=teacherDTO, pointLogList=pointLogList, pointLogStudent=pointLogStudent, pointLogTeacher=pointLogTeacher)
    except Exception as e:
        print(e)
        return redirect(url_for('index'))
    
@teacherBlue.route('/pointReasons')
def pointReasons():
    if 'id' not in session:
        return redirect(url_for('index'))

    respDTO = usersDTO(id=session['id'], name=session['name'], stdNum=session['stdNum'], identity=session['identity'])
    bonusPointReasons = pointSVC.getPointReason('bonus')
    penaltyPointReasons = pointSVC.getPointReason('penalty')
    
    return render_template('teacher/pointReasonsTeacher.html', usersDTO=respDTO, bonusPointReasonDTO=bonusPointReasons, penaltyPointReasonDTO=penaltyPointReasons)

@teacherBlue.route('/studentManagement')
def studentManagement():
    try:
        if 'id' not in session:
            return redirect(url_for('index'))
        
        teacherDTO = usersDTO(id=session['id'], name=session['name'], identity=session['identity'])
        studentList = usersSVC.getStudentsList(1)
    
        return render_template('teacher/studentManagement.html', usersDTO=teacherDTO, studentList=studentList)
    except Exception as e:
        print(e)
        return redirect(url_for('index'))

@teacherBlue.route('/teacherManagement')
def teacherManagement():
    try:
        if 'id' not in session:
            return redirect(url_for('index'))

        teacherDTO = usersDTO(id=session['id'], name=session['name'], identity=session['identity'])
        teacherList = usersSVC.getTeachersList(1)

        return render_template('teacher/teacherManagement.html', usersDTO=teacherDTO, teacherList=teacherList)
    except Exception as e:
        print(e)
        return redirect(url_for('index'))

# ------------------ community(게시판) 기능 ------------------

@teacherBlue.route('/community')
def communityList():
    try:
        if 'id' not in session:
            return redirect(url_for('index'))

        teacherDTO = usersDTO(id=session['id'], name=session['name'], identity=session['identity'])
        notices = SVC.get_all_notices()
        return render_template('teacher/communityTeacher.html', usersDTO=teacherDTO, notices=notices)
    except Exception as e:
        print(e)
        return redirect(url_for('index'))

    except Exception as e:
        print(e)
        return redirect(url_for('index'))
    
@teacherBlue.route('/giveBonusPoint')
def giveBonusPoint():
    try:
        if 'id' not in session:
            return '로그인이 필요합니다'
        
        teacherDTO = usersDTO(id=session['id'], name=session['name'], identity=session['identity'])
        studentList = usersSVC.getStudentsList(1)
        teacherList = usersSVC.getTeachersList(1)
        pointReasonList = pointSVC.getPointReason('bonus')
    
        return render_template('teacher/giveBonusPointPopup.html', usersDTO=teacherDTO, studentList=studentList, teacherList=teacherList, pointReasonList=pointReasonList)
    except Exception as e:
        print(e)
        return redirect(url_for('index'))
    
@teacherBlue.route('/givePenaltyPoint')
def givePenaltyPoint():
    try:
        if 'id' not in session:
            return '로그인이 필요합니다'

        teacherDTO = usersDTO(id=session['id'], name=session['name'], identity=session['identity'])
        studentList = usersSVC.getStudentsList(1)
        teacherList = usersSVC.getTeachersList(1)
        pointReasonList = pointSVC.getPointReason('penalty')
            
        return render_template('teacher/givePenaltyPointPopup.html', usersDTO=teacherDTO, studentList=studentList, teacherList=teacherList, pointReasonList=pointReasonList)
    except Exception as e:
        print(e)
        return redirect(url_for('index'))
    
@teacherBlue.route('/giveBonusPoint.do', methods=['POST'])
def doGiveBonusPoint():
    try:
        stdId = request.form['stdId']
        reason = request.form['reason']
        point = request.form['point']
        writeTeacherId = request.form['writeTeacherId']
        giveTeacherId = request.form['giveTeacherId']
        opinion = request.form['opinion']

        stdDTO = usersDTO(id=stdId)
        writerDTO = usersDTO(id=writeTeacherId)
        giverDTO = usersDTO(id=giveTeacherId)
        point = int(point)
        
        pointSVC.givePoint(stdDTO, writerDTO, giverDTO, point, reason, opinion)

        return "<script>alert('상점이 부과되었습니다.'); opener.location.reload(); window.close();</script>"
    except Exception as e:
        print(e)
        flash(str(e))
        return redirect(url_for('teacher.giveBonusPoint'))
    
@teacherBlue.route('/givePenaltyPoint.do', methods=['POST'])
def doGivePenaltyPoint():
    try:
        stdId = request.form['stdId']
        reason = request.form['reason']
        point = request.form['point']
        writeTeacherId = request.form['writeTeacherId']
        giveTeacherId = request.form['giveTeacherId']
        opinion = request.form['opinion']

        stdDTO = usersDTO(id=stdId)
        writerDTO = usersDTO(id=writeTeacherId)
        giverDTO = usersDTO(id=giveTeacherId)
        point = int(point)*(-1)
        
        pointSVC.givePoint(stdDTO, writerDTO, giverDTO, point, reason, opinion)

        return "<script>alert('벌점이 부과되었습니다.'); opener.location.reload(); window.close();</script>"
    except Exception as e:
        print(e)
        flash(str(e))
        return redirect(url_for('teacher.giveBonusPoint'))

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
    
@teacherBlue.route('/teacherSignupApprovalPopup')
def teacherSignupApprovalPopup():
    try:
        if 'id' not in session:
            return redirect(url_for('index'))
        
        return render_template('teacher/teacherSignupApprovalPopup.html')
    except Exception as e:
        print(e)
        return 'Error'

@teacherBlue.route('/resetTeacherPasswdPopup')
def resetTeacherPasswdPopup():
    try:
        if 'id' not in session:
            return redirect(url_for('index'))
        
        return render_template('teacher/resetTeacherPasswdPopup.html')
    except Exception as e:
        print(e)
        return 'Error'
    
@teacherBlue.route('/resetStudentPasswdPopup')
def resetStudentPasswdPopup():
    try:
        if 'id' not in session:
            return redirect(url_for('index'))
        
        return render_template('teacher/resetStudentPasswdPopup.html')
    except Exception as e:
        print(e)
        return 'Error'