from flask import Blueprint, request, redirect, url_for, flash, session, make_response, render_template
import studentSVC
from studentDTO import studentDTO

blue_student = Blueprint('student', __name__, url_prefix='/student')

SVC = studentSVC.studentSVC()

@blue_student.route('/signup.do', methods=['POST'])
def dosignup():
    try:
        id = request.form['id']
        password = request.form['password']
        name = request.form['name']
        email = request.form['email']
        birth = request.form['birth']
        birth = birth.replace("-", "")

        reqDTO = studentDTO(id=id, password=password, name=name, email=email, birth=birth)

        SVC.signup(reqDTO)
        print("signup success")
        
        return redirect(url_for('index'))
    except Exception as e:
        print(e)
        return redirect(url_for('signup'))
    
@blue_student.route('/login.do', methods=['POST'])
def dologin():
    try:
        print('dologin')
        if request.form.get('id') and request.form.get('password'):
            id = request.form.get('id')
            password = request.form.get('password')
            print('form')
        elif 'SangilGulbiUserID' in request.cookies and 'SangilGulbiUserPWD' in request.cookies:
            id = request.cookies.get('SangilGulbiUserID')
            password = request.cookies.get('SangilGulbiUserPWD')
            print('cookie')
        else:
            print('no id or password')
            return redirect(url_for('login'))

        reqDTO = studentDTO(id=id, password=password)
        
        if SVC.login(reqDTO):
            loginDTO = SVC.getStudentInfo(reqDTO)
            
            session['id'] = loginDTO.id
            session['name'] = loginDTO.name
            session['profile_pic'] = loginDTO.profile_pic
        
            resp = make_response(redirect(url_for('index')))
            if request.form.get('remember'):
                resp.set_cookie('SangilGulbiUserID', loginDTO.id, max_age=60*60*24*365) # 1년
                resp.set_cookie('SangilGulbiUserPWD', loginDTO.password, max_age=60*60*24*365) # 1년

        return resp
    except Exception as e:
        print(e)
        return redirect(url_for('login'))
    
@blue_student.route('/logout.do')
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

@blue_student.route('/IDcheck.do', methods=['POST'])
def IDcheck():
    try:
        reqDTO = studentDTO(id=request.form['id'])
        if SVC.isIDExist(reqDTO):
            return "false"
        else:
            return "true"
    except Exception as e:
        print(e)
        return False

@blue_student.route('/update_user_info', methods=['POST'])
def update_user_info():
    if 'id' not in session:
        return redirect(url_for('login'))
    
    student_service = studentSVC.studentSVC()
    user = studentDTO(
        id=session['id'],
        firststdnum=request.form['num'],
        name=request.form['name'],
        phone=request.form['phone'],
        email=request.form['email']
    )
    student_service.updateUserInfo(user)
    
    return redirect(url_for('mypage'))