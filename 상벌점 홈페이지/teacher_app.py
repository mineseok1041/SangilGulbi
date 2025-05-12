from flask import Flask, redirect, render_template, session, url_for, Blueprint, request, flash

from usersSVC import usersSVC
from usersDTO import usersDTO
from pointSVC import pointSVC
from pointReasonDTO import pointReasonDTO
from pointLogDTO import pointLogDTO

teacherBlue = Blueprint('teacher', __name__, url_prefix='/teacher')

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
    
        return render_template('teacher/indexTeacher.html', usersDTO=teacherDTO, studentList=studentList, teacherList=teacherList)
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
    
@teacherBlue.route('/community')
def community():
    try:
        if 'id' not in session:
            return redirect(url_for('index'))

        teacherDTO = usersDTO(id=session['id'], name=session['name'], identity=session['identity'])

        return render_template('teacher/communityTeacher.html', usersDTO=teacherDTO)
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
