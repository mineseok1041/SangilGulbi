from flask import Blueprint, request, redirect, url_for, session, current_app
from werkzeug.utils import secure_filename
import os
import usersSVC
from usersDTO import usersDTO

# Blueprint 생성
upload_bp = Blueprint('upload', __name__)

# 허용되는 파일 확장자 목록
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# 파일 이름이 허용되는 확장자인지 확인하는 함수
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# 프로필 사진 업로드 처리 라우트
@upload_bp.route('/upload_profile_pic', methods=['POST'])
def upload_profile_pic():
    # 요청에 파일이 포함되어 있는지 확인
    if 'file' not in request.files:
        return redirect(request.url)
    
    file = request.files['file']
    
    # 파일 이름이 비어 있는지 확인
    if file.filename == '':
        return redirect(request.url)
    
    # 파일이 있고 허용된 확장자인지 확인
    if file and allowed_file(file.filename):
        # 파일 이름 안전하게 변환
        filename = secure_filename(file.filename)
        # 세션에서 사용자 ID 가져오기
        user_id = session['id']
        # 파일 이름을 사용자 ID로 설정
        filename = f"{user_id}"
        
        # 업로드 폴더 경로 설정
        upload_folder = os.path.join(current_app.root_path, 'static', 'uploads')
        # 업로드 폴더가 존재하지 않으면 생성
        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder)
        
        # 파일 저장
        file.save(os.path.join(upload_folder, filename))

        # 세션에 ID가 있는지 확인
        if 'id' in session:
            # 사용자 서비스 인스턴스 생성
            users_service = usersSVC.usersSVC()
            # 사용자 DTO 생성
            users = usersDTO(id=session['id'])
            # 프로필 사진 파일 이름 설정
            users.profile_pic = filename
            # 프로필 사진 업데이트
            users_service.updateProfilePic(users)
            
        # 세션에 프로필 사진 파일 이름 저장
        session['profile_pic'] = filename
        
        # 마이페이지로 리다이렉션
        return redirect(url_for('mypage'))
    
    # 파일이 없거나 허용되지 않은 확장자인 경우 마이페이지로 리다이렉션
    return redirect(url_for('mypage'))