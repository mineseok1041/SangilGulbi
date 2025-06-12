from flask import Flask, redirect, render_template, session, url_for, Blueprint, request, flash, make_response
from usersDTO import usersDTO
from usersSVC import usersSVC
from functools import wraps


authBlue = Blueprint('auth', __name__, url_prefix='/auth')

usersSVC = usersSVC()

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
    
@authBlue.route('/signup.do/<userType>', methods=['POST'])
def dosignup(userType):
    try:
        if userType == 'student':
            id = request.form['id']
            password = request.form['password']
            name = request.form['name']
            stdNum = request.form['stdNum']

            reqDTO = usersDTO(id=id, password=password, name=name, stdNum=stdNum, identity=2)

            usersSVC.signup(reqDTO)

            flash("회원가입이 완료되었습니다.")
            return redirect(url_for('index'))
        
        elif userType == 'teacher':
            id = request.form['id']
            password = request.form['password']
            name = request.form['name']
            checkCode = request.form['checkCode']

            reqDTO = usersDTO(id=id, password=password, name=name, identity=1, checkCode=checkCode)
            usersSVC.signup(reqDTO)

            flash("회원가입이 완료되었습니다.")
            return redirect(url_for('index'))

        else:
            raise Exception("Invalid userType")
    except Exception as e:
        print(e)
        flash("회원가입에 실패했습니다. 다시 시도해주세요.")
        return redirect(url_for('auth.signup', userType=userType))
    
@authBlue.route('/login.do', methods=['POST'])
def dologin():
    try:
        if request.form.get('id') and request.form.get('password'):
            id = request.form.get('id')
            password = request.form.get('password')
        elif 'SangilGulbiUserID' in request.cookies and 'SangilGulbiUserPWD' in request.cookies:
            id = request.cookies.get('SangilGulbiUserID')
            password = request.cookies.get('SangilGulbiUserPWD')
        else:
            flash('아이디와 비밀번호를 입력해주세요')
            return redirect(url_for('auth.login'))

        reqDTO = usersDTO(id=id, password=password)
        
        if usersSVC.login(reqDTO):
            loginDTO = usersSVC.getUsersInfo(reqDTO)
            
            session['id'] = loginDTO.id
            session['name'] = loginDTO.name
            session['stdNum'] = loginDTO.stdNum
            session['identity'] = loginDTO.identity
            
            response = make_response(redirect(url_for('index')))
            if request.form.get('remember'):
                response.set_cookie('SangilGulbiUserID', loginDTO.id, max_age=60*60*24*365) # 1년
                response.set_cookie('SangilGulbiUserPWD', loginDTO.password, max_age=60*60*24*365) # 1년
        
        return response
    except Exception as e:
        print(e)
        flash(str(e))
        return redirect(url_for('auth.login'))
    
@authBlue.route('/logout.do')
def dologout():
    try:
        session.clear()
        resp = make_response(redirect(url_for('index')))
        resp.set_cookie('SangilGulbiUserID', '', expires=0)
        resp.set_cookie('SangilGulbiUserPWD', '', expires=0)
        return resp
    except Exception as e:
        print(e)
        return redirect(url_for('index'))
    
@authBlue.route('/myInfoEditPopup')
def myInfoEditPopup():
    if 'id' not in session:
        return redirect(url_for('index'))

    return render_template('auth/myInfoEditPopup.html')

@authBlue.route('/myInfoEdit.do', methods=['POST'])
def doMyInfoEdit():
    try:
        if 'id' not in session:
            return redirect(url_for('auth.login'))

        id = session['id']
        currentpassword = request.form.get('currentPassword')
        newPassword = request.form.get('newPassword')
        newPasswordCheck = request.form.get('newPasswordCheck')

        beforeDTO = usersDTO(id=id, password=currentpassword)
        usersSVC.changePassword(beforeDTO, newPassword, newPasswordCheck)

        return "<script>alert('비밀번호가 변경되었습니다.'); window.close();</script>"
    except Exception as e:
        message = str(e)
        return f"<script>alert('{message}'); history.back();</script>"
    
# 관리자 권한 확인 데코레이터
def adminAuth(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'id' not in session or session.get('identity') != 0:
            flash("관리자 권한이 필요합니다.")
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated_function