from flask import Flask, redirect, Blueprint, render_template, session, url_for
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

# 마이페이지 수정
@app.route('/mypage_Popup')
def mypage_Popup():
    if 'id' not in session:
        return redirect(url_for('login'))
    
    student_service = studentSVC.studentSVC()
    user = student_service.getStudentInfo(studentDTO(id=session['id']))
    
    return render_template('mypage_Popup.html', user=user)

# 수상내역
@app.route('/awards')
def awards():
    return render_template('awards.html')

@app.route('/rhythm')
def rhythm():
    return render_template('rhythm.html')

if __name__ == '__main__':
    app.run()