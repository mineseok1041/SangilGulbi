from flask import Flask, redirect, render_template, session, url_for, Blueprint

teacherBlue = Blueprint('teacher', __name__, url_prefix='/teacher')

@teacherBlue.route('/')
def index():
    try:
        if 'id' not in session:
            return redirect(url_for('index'))
    
        return render_template('teacher/indexTeacher.html')
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
    
@teacherBlue.route('/community')
def community():
    try:
        if 'id' not in session:
            return redirect(url_for('index'))
    
        return render_template('teacher/communityTeacher.html')
    except Exception as e:
        print(e)
        return redirect(url_for('index'))
    
