import os
from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.utils import secure_filename
from models import db, User, Point

app = Flask(__name__)
app.config['SECRET_KEY'] = 'HoneyBeeclub'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///honeybee.db'

# static/uploads 폴더를 절대 경로로 설정
app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'static', 'uploads')
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}  # 허용된 파일 확장자

db.init_app(app)

# 업로드 폴더가 없으면 생성
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# 관리자 계정 생성 로직
def create_admin():
    with app.app_context():  # 애플리케이션 컨텍스트 설정
        db.create_all()  # 테이블 생성
        admin = User.query.filter_by(username='admin').first()
        if not admin:
            admin = User(username='admin', password='adminpassword', is_admin=True)
            db.session.add(admin)
            db.session.commit()
            print("admin account created!")

# 관리자 계정이 없으면 생성
create_admin()

# 파일 확장자 체크 함수
def allowed_file(filename):
    # 파일 이름에 확장자가 포함되어 있고, 허용된 확장자인지 확인
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            session['user_id'] = user.id
            return redirect(url_for('dashboard'))
        else:
            return '사용자 이름 또는 비밀번호가 잘못되었습니다.'
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # 'admin' 사용자 이름 막기
        if username.lower() == 'admin':
            return "관리자 계정은 생성할 수 없습니다."

        # 사용자 이름 중복 체크
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            return "사용자 이름이 이미 존재합니다. 다른 것을 선택하세요."

        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    # 사용자 정보 가져오기
    user = User.query.get(session['user_id'])
    
    # 총 상벌점 계산
    total_points = user.total_points()

    return render_template('dashboard.html', user=user, total_points=total_points)

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    user = User.query.get(session['user_id'])
    if not user.is_admin:
        return 'Unauthorized'
    
    if request.method == 'POST':
        # 상벌점 추가 처리
        if 'username' in request.form and 'points' in request.form:
            username = request.form['username']
            points = int(request.form['points'])
            user_to_update = User.query.filter_by(username=username).first()
            if user_to_update:
                # 상벌점 기록 추가
                new_point = Point(user_id=user_to_update.id, points=points)
                db.session.add(new_point)
                db.session.commit()
                return redirect(url_for('admin'))  # 상벌점 추가 후 관리자 페이지로 리다이렉트
            else:
                return 'User not found'
        
    return render_template('admin.html')

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    user = User.query.get(session['user_id'])

    if request.method == 'POST':
        # 프로필 사진 업로드 처리
        if 'file' not in request.files:
            return 'No file part'
        file = request.files['file']
        
        if file.filename == '':
            return 'No selected file'
        
        if not allowed_file(file.filename):
            return '파일 확장자가 잘못되었습니다. 허용되는 확장자 : png, jpg, jpeg, gif.'

        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        
        # 파일 저장
        file.save(file_path)
        
        # 데이터베이스에 파일명 저장
        user.profile_pic = filename
        db.session.commit()

    # 프로필 사진을 static/uploads/ 경로에서 불러오기
    profile_pic_url = url_for('static', filename='uploads/' + user.profile_pic) if user.profile_pic else None

    return render_template('profile.html', user=user, profile_pic_url=profile_pic_url)

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
