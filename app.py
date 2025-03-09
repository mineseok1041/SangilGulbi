from flask import Flask, redirect, render_template, session, url_for, request, Response
from flask_cors import CORS
import requests
import upload
from usersDTO import usersDTO
import usersSVC
from noticeSVC import NoticeSVC
from noticeDTO import NoticeDTO
import users_app
import os

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
    
    return render_template('mypage.html', user=user)

# 마이페이지 수정 팝업
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

# 수상내역 페이지
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

# 공지사항 목록
@app.route('/notice')
def notice_list():
    SVC = NoticeSVC()
    notices = SVC.get_all_notices()
    return render_template('mainnotice.html', notices=notices)

# 공지사항 상세
@app.route('/notice/<int:notice_id>')
def notice_detail(notice_id):
    SVC = NoticeSVC()
    notice = SVC.get_notice_by_id(notice_id)
    return render_template('noticepage.html', notice=notice)

# 공지사항 추가
@app.route('/notice/add', methods=['GET', 'POST'])
def add_notice():
    if 'id' not in session:
        return redirect(url_for('login'))  # 로그인하지 않은 경우 로그인 페이지로 리디렉션
    SVC = NoticeSVC()
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        author = session['id']
        notice = NoticeDTO(title=title, content=content, author=author)
        SVC.add_notice(notice)
        return redirect(url_for('notice_list'))
    return render_template('noticeadd.html')

# 공지사항 수정
@app.route('/notice/edit/<int:notice_id>', methods=['GET', 'POST'])
def edit_notice(notice_id):
    SVC = NoticeSVC()
    notice = SVC.get_notice_by_id(notice_id)
    if request.method == 'POST':
        notice.title = request.form['title']
        notice.content = request.form['content']
        SVC.update_notice(notice)
        return redirect(url_for('notice_detail', notice_id=notice_id))
    return render_template('noticeedit.html', notice=notice)

# 공지사항 삭제
@app.route('/notice/delete/<int:notice_id>', methods=['POST'])
def delete_notice(notice_id):
    SVC = NoticeSVC()
    SVC.delete_notice(notice_id)
    return redirect(url_for('notice_list'))

if __name__ == '__main__':
    app.run()