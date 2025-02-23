from flask import Flask, redirect, render_template, session, url_for, request, Response
import requests
from flask_cors import CORS
import users_app
import upload
import os
import usersSVC
from usersDTO import usersDTO

app = Flask(__name__)
CORS(app)
app.register_blueprint(users_app.blue_users)
app.register_blueprint(upload.upload_bp)

app.secret_key = 'ggulbi'

app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'static', 'uploads')

# 메인페이지
@app.route('/')
def index():
    if 'id' in session:
        return render_template('index.html')
    elif 'SangilGulbiUserID' in request.cookies and 'SangilGulbiUserPWD' in request.cookies:
        resp = requests.post(url_for('users.dologin', _external=True))
        return Response(resp.content, status=resp.status_code, headers=dict(resp.headers))
    else:
        return render_template('index.html')
    
@app.route('/check')
def check():
    id = request.cookies.get('SangilGulbiUserID')
    password = request.cookies.get('SangilGulbiUserPWD')
    print(id, password)
    return redirect(url_for('index'))

# 로그인
@app.route('/login')
def login():
    return render_template('login.html')

# 비밀번호 찾기
@app.route('/forget')
def forget():
    return render_template('forget.html')

# 회원가입
@app.route('/signup')
def signup():
    return render_template('signup.html')

# 마이페이지
@app.route('/mypage')
def mypage():
    if 'id' not in session:
        return redirect(url_for('login'))
    
    users_service = usersSVC.usersSVC()
    user = users_service.getUsersInfo(usersDTO(id=session['id']))
    
    return render_template('mypage.html', user=user)

# 마이페이지 수정
@app.route('/mypage_Popup')
def mypage_Popup():
    if 'id' not in session:
        return redirect(url_for('login'))
    
    users_service = usersSVC.usersSVC()
    user = users_service.getUsersInfo(usersDTO(id=session['id']))
    
    return render_template('mypage_Popup.html', user=user)

# 관리페이지 메인
@app.route('/mgmt')
def manager_page():
    return render_template('manager_page_main.html')

# 관리페이지 유저 관리
@app.route('/mgmt_user')
def manager_page_user():
    return render_template('manager_page_user.html')

# 관리페이지 관리자 추가
@app.route('/mgmt_add')
def manager_page_add():
    return render_template('manager_page_add.html')

# 수상내역
@app.route('/awards')
def awards():
    return render_template('awards.html')

@app.route('/rhythm')
def rhythm():
    return render_template('rhythm.html')

if __name__ == '__main__':
    app.run()