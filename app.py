from flask import Flask, render_template

app  = Flask(__name__)

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

# 수상내역
@app.route('/awards')
def awards():
    return render_template('awards.html')

if __name__ == '__main__':
    app.run()