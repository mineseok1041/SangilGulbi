from flask import Blueprint, request, redirect, url_for, session, current_app
from werkzeug.utils import secure_filename
import os
import studentSVC
from studentDTO import studentDTO

upload_bp = Blueprint('upload', __name__)

# 허용된 파일 확장자 설정
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@upload_bp.route('/upload_profile_pic', methods=['POST'])
def upload_profile_pic():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        
        # 사용자 ID를 파일 이름에 추가하여 고유하게 만듭니다.
        user_id = session['id']
        filename = f"{user_id}_{filename}"
        
        # 업로드 폴더가 존재하지 않으면 생성
        upload_folder = os.path.join(current_app.root_path, 'static', 'uploads')
        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder)
        
        file.save(os.path.join(upload_folder, filename))
        
        # 데이터베이스에 파일명을 저장하는 로직 추가
        if 'id' in session:
            student_service = studentSVC.studentSVC()
            student = studentDTO(id=session['id'])
            student.profile_pic = filename
            student_service.updateProfilePic(student)
        
        # 세션에 프로필 사진 경로를 저장
        session['profile_pic'] = filename
        
        return redirect(url_for('mypage'))
    return redirect(url_for('mypage'))