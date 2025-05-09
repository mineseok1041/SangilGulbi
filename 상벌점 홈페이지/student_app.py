from flask import Flask, redirect, render_template, session, url_for, Blueprint

studentBlue = Blueprint('student', __name__, url_prefix='/student')

@studentBlue.route('/')
def index():
    if 'id' not in session:
        return '학생메인'
        #return redirect(url_for('index'))
    
    return render_template('student/indexStudent.html')