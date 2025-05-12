from flask import Flask, redirect, render_template, session, url_for, Blueprint

from usersSVC import usersSVC
from usersDTO import usersDTO
from pointSVC import pointSVC
from pointLogDTO import pointLogDTO

studentBlue = Blueprint('student', __name__, url_prefix='/student')

usersSVC = usersSVC()
pointSVC = pointSVC()

@studentBlue.route('/')
def index():
    try:
        if 'id' not in session:
            return redirect(url_for('index'))
        
        respDTO = usersSVC.getUsersInfo(usersDTO(id=session['id']))
        pointLogList = pointSVC.getPointLogByStdID(usersDTO(id=session['id']))
        pointLogStudent = [usersSVC.getUsersInfo(usersDTO(id=log.studentId)) for log in pointLogList]
        pointLogTeacher = [usersSVC.getUsersInfo(usersDTO(id=log.giveTeacherId)) for log in pointLogList]

        return render_template('student/indexStudent.html', usersDTO=respDTO, pointLogList=pointLogList, pointLogStudent=pointLogStudent, pointLogTeacher=pointLogTeacher)
    except Exception as e:
        print(e)
        return redirect(url_for('index'))

@studentBlue.route('/pointLog')
def pointLog():
    if 'id' not in session:
        return redirect(url_for('index'))
    
    respDTO = usersDTO(id=session['id'], name=session['name'], stdNum=session['stdNum'], identity=session['identity'])
    pointLogList = pointSVC.getPointLogByStdID(usersDTO(id=session['id']))
    pointLogStudent = [usersSVC.getUsersInfo(usersDTO(id=log.studentId)) for log in pointLogList]
    pointLogTeacher = [usersSVC.getUsersInfo(usersDTO(id=log.giveTeacherId)) for log in pointLogList]
    
    return render_template('student/pointLogStudent.html', usersDTO=respDTO, pointLogList=pointLogList, pointLogStudent=pointLogStudent, pointLogTeacher=pointLogTeacher)

@studentBlue.route('/community')
def community():
    if 'id' not in session:
        return redirect(url_for('index'))
    
    respDTO = usersDTO(id=session['id'], name=session['name'], stdNum=session['stdNum'], identity=session['identity'])
    
    return render_template('student/communityStudent.html')