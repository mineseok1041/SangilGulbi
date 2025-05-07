from flask import Flask, redirect, render_template, session, url_for, request, Response
from flask_cors import CORS
import requests
import upload
import management_app
import os
import usersSVC
from usersDTO import usersDTO
from noticeSVC import NoticeSVC
from noticeDTO import NoticeDTO
import users_app
import notice_app
import os

app = Flask(__name__)
CORS(app)

app.register_blueprint(users_app.blue_users)
app.register_blueprint(upload.upload_bp)
app.register_blueprint(notice_app.blue_notice)
app.register_blueprint(management_app.blue_management)


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

# 쿠키 확인
@app.route('/check')
def check():
    id = request.cookies.get('SangilGulbiUserID')
    password = request.cookies.get('SangilGulbiUserPWD')
    print(id, password)
    return redirect(url_for('index'))

# 로그인 페이지
@app.route('/login')
def login():
    return render_template('login.html')

# 비밀번호 찾기 페이지
@app.route('/forget')
def forget():
    return render_template('forget.html')

# 회원가입 페이지
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
    pointLogs = users_service.getPointLogByStdID(usersDTO(id=session['id']))
    
    return render_template('mypage.html', user=user, pointLogs=pointLogs)

# 마이페이지 수정 팝업
@app.route('/mypage_Popup')
def mypage_Popup():
    if 'id' not in session:
        return redirect(url_for('login'))
    
    users_service = usersSVC.usersSVC()
    user = users_service.getUsersInfo(usersDTO(id=session['id']))
    
    return render_template('mypage_Popup.html', user=user)

# 수상내역
@app.route('/awards')
def awards():
    return render_template('awards.html')

# 리듬게임 페이지
@app.route('/rhythm')
def rhythm():
    return render_template('rhythm.html')

# 룰렛 페이지
@app.route('/roulette')
def roulette():
    return render_template('roulette.html')

# 사다리 페이지
@app.route('/sadari')
def sadari():
    return render_template('sadari.html')

@app.route('/developers')
def developers():
    return render_template('developerInfo.html')

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port=16369)