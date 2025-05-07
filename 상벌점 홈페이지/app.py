from flask import Flask, redirect, render_template, session, url_for, request, Response
from flask_cors import CORS

import requests
import upload
import os

from usersSVC import usersSVC
from usersDTO import usersDTO
from noticeSVC import NoticeSVC
from noticeDTO import NoticeDTO

import users_app
import management_app
import notice_app

app = Flask(__name__)
CORS(app)
app.secret_key = 'ggulbi'

app.register_blueprint(users_app.blue_users)
app.register_blueprint(upload.upload_bp)
app.register_blueprint(notice_app.blue_notice)
app.register_blueprint(management_app.blue_management)
# app.register_blueprint(mypage_app.blue_mypage)

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
    
# 학생&선생님 선택
@app.route('/select')
def select():
    if 'id' in session:
        return redirect(url_for('index'))
    return render_template('select.html')

# 로그인 페이지
@app.route('/login')
def login():
    if 'id' in session:
        return redirect(url_for('index'))
    return render_template('login.html')

# 회원가입 페이지
@app.route('/signup')
def signup():
    if 'id' in session:
        return redirect(url_for('index'))
    return render_template('signup.html')

# 마이페이지
@app.route('/mypage')
def mypage():
    if 'id' not in session:
        return redirect(url_for('login'))
    
    users_service = usersSVC()
    user = users_service.getUsersInfo(usersDTO(id=session['id']))
    pointLogs = users_service.getPointLogByStdID(usersDTO(id=session['id']))
    
    return render_template('mypage.html', user=user, pointLogs=pointLogs)

# 마이페이지 수정 팝업
@app.route('/mypage_Popup')
def mypage_Popup():
    if 'id' not in session:
        return redirect(url_for('login'))
    
    users_service = usersSVC()
    user = users_service.getUsersInfo(usersDTO(id=session['id']))
    
    return render_template('mypage_Popup.html', user=user)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port=16369)