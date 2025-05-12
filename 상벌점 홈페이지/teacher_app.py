from flask import Flask, redirect, render_template, session, url_for, Blueprint, request, flash

from usersSVC import usersSVC
from usersDTO import usersDTO

teacherBlue = Blueprint('teacher', __name__, url_prefix='/teacher')

usersSVC = usersSVC()

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
    
        return render_template('teacher/givePointLog.html', usersDTO=teacherDTO)
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

        return render_template('teacher/teacherManagement.html', usersDTO=teacherDTO)
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
    
        return render_template('teacher/giveBonusPointPopup.html', usersDTO=teacherDTO, studentList=studentList, teacherList=teacherList)
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
            
        return render_template('teacher/givePenaltyPointPopup.html', usersDTO=teacherDTO, studentList=studentList, teacherList=teacherList)
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

        print(stdId, reason, point, writeTeacherId, giveTeacherId, opinion)
        
        usersSVC.givePoint(stdDTO, writerDTO, giverDTO, point, reason)

        return "<script>alert('상점이 부과되었습니다.'); opener.location.reload(); window.close();</script>"
    except Exception as e:
        print(e)
        flash(str(e))
        return redirect(url_for('giveBonusPoint'))
    
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

        print(stdId, reason, point, writeTeacherId, giveTeacherId, opinion)
        
        usersSVC.givePoint(stdDTO, writerDTO, giverDTO, point, reason)

        return "<script>alert('벌점이 부과되었습니다.'); opener.location.reload(); window.close();</script>"
    except Exception as e:
        print(e)
        flash(str(e))
        return redirect(url_for('giveBonusPoint'))
