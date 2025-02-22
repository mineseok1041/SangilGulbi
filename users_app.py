from flask import Blueprint, request, redirect, url_for, flash, session, make_response, render_template
import usersSVC
from usersDTO import usersDTO

blue_users = Blueprint('users', __name__, url_prefix='/users')

SVC = usersSVC.usersSVC()

@blue_users.route('/signup.do', methods=['POST'])
def dosignup():
    try:
        id = request.form['id']
        password = request.form['password']
        name = request.form['name']
        email = request.form['email']
        birth = request.form['birth']
        birth = birth.replace("-", "")

        reqDTO = usersDTO(id=id, password=password, name=name, email=email, birth=birth)

        SVC.signup(reqDTO)
        print("signup success")
        
        return redirect(url_for('index'))
    except Exception as e:
        print(e)
        return redirect(url_for('signup'))
    
@blue_users.route('/login.do', methods=['POST'])
def dologin():
    try:
        if request.form.get('id') and request.form.get('password'):
            id = request.form.get('id')
            password = request.form.get('password')
        elif 'SangilGulbiUserID' in request.cookies and 'SangilGulbiUserPWD' in request.cookies:
            id = request.cookies.get('SangilGulbiUserID')
            password = request.cookies.get('SangilGulbiUserPWD')
        else:
            return redirect(url_for('login'))

        reqDTO = usersDTO(id=id, password=password)
        
        if SVC.login(reqDTO):
            loginDTO = SVC.getUsersInfo(reqDTO)
            
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
    
@blue_users.route('/logout.do')
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

@blue_users.route('/IDcheck.do', methods=['POST'])
def IDcheck():
    try:
        reqDTO = usersDTO(id=request.form['id'])
        if SVC.isIDExist(reqDTO):
            return "false"
        else:
            return "true"
    except Exception as e:
        print(e)
        return False

@blue_users.route('/update_user_info', methods=['POST'])
def update_user_info():
    if 'id' not in session:
        return redirect(url_for('login'))
    
    users_service = usersSVC.usersSVC()
    num = str(request.form['num'])
    currentgrade = int(num[0])
    currentclass = int(num[1])*10+int(num[2])
    currentnum = int(num[3])*10+int(num[4])
    
    user = usersDTO(
        id=session['id'],
        currentgrade=currentgrade,
        currentclass=currentclass,
        currentnum=currentnum,
        name=request.form['name'],
        phone=request.form['phone'],
        email=request.form['email']
    )
    users_service.updateUserInfo(user)
    
    return redirect(url_for('mypage'))