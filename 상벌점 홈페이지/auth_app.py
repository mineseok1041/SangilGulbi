from flask import Flask, redirect, render_template, session, url_for, Blueprint

authBlue = Blueprint('auth', __name__, url_prefix='/auth')

# 학생&선생님 선택
@authBlue.route('/who')
def who():
    if 'id' in session:
        return redirect(url_for('index'))
    
    return render_template('auth/who.html')

# 로그인 페이지
@authBlue.route('/login')
def login():
    if 'id' in session:
        return redirect(url_for('index'))
    return render_template('auth/login.html')


# 회원가입 페이지
@authBlue.route('/signup/<userType>')
def signup(userType):
    if 'id' in session:
        return redirect(url_for('index'))
    
    if userType == 'student':
        return render_template('auth/signupStudent.html')
    elif userType == 'teacher':
        return render_template('auth/signupTeacher.html')
    else:
        return redirect(url_for('who'))