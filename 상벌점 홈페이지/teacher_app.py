from flask import Flask, redirect, render_template, session, url_for, Blueprint

teacherBlue = Blueprint('teacher', __name__, url_prefix='/teacher')

@teacherBlue.route('/')
def index():
    if 'id' not in session:
        return '학생메인'
        #return redirect(url_for('index'))
    
    return render_template('teacher/indexStudent.html')