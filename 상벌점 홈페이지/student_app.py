from flask import Flask, redirect, render_template, session, url_for, Blueprint

from usersSVC import usersSVC
from usersDTO import usersDTO

studentBlue = Blueprint('student', __name__, url_prefix='/student')

usersSVC = usersSVC()

@studentBlue.route('/')
def index():
    try:
        if 'id' not in session:
            return redirect(url_for('index'))
        
        respDTO = usersSVC.getUsersInfo(usersDTO(id=session['id']))

        return render_template('student/indexStudent.html', usersDTO=respDTO)
    except Exception as e:
        print(e)
        return redirect(url_for('index'))

@studentBlue.route('/pointLog')
def pointLog():
    if 'id' not in session:
        return redirect(url_for('index'))
    
    return render_template('student/pointLogStudent.html')

@studentBlue.route('/community')
def community():
    if 'id' not in session:
        return redirect(url_for('index'))
    
    return render_template('student/communityStudent.html')