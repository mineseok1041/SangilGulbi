from flask import Flask, redirect, render_template, session, url_for, Blueprint

teacherBlue = Blueprint('teacher', __name__, url_prefix='/teacher')

@teacherBlue.route('/')
def index():
    try:
        if 'id' not in session:
            return redirect(url_for('index'))
    
        return render_template('teacher/indexStudent.html')
    except Exception as e:
        print(e)
        return redirect(url_for('index'))