from flask import Flask, render_template, Blueprint
from flask_cors import CORS
import student_app

app  = Flask(__name__)
CORS(app)
app.register_blueprint(student_app.blue_student)

app.secret_key = 'ggulbi'

# 메인페이지
@app.route('/')
def index():
    return render_template('index.html')

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
    return render_template('mypage.html')

# 관리페이지 메인
@app.route('/mgmt')
def manager_page():
    return render_template('manager_page_main.html')

# 관리페이지 유저 관리
@app.route('/mgmt_user')
def manager_page_user():
    return render_template('manager_page_user.html')

# 수상내역
@app.route('/awards')
def awards():
    return render_template('awards.html')

@app.route('/rhythm')
def rhythm():
    return render_template('rhythm.html')

if __name__ == '__main__':
    app.run()