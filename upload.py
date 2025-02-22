from flask import Blueprint, request, redirect, url_for, session, current_app
from werkzeug.utils import secure_filename
import os
import usersSVC
from usersDTO import usersDTO

upload_bp = Blueprint('upload', __name__)

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
        
        user_id = session['id']
        filename = f"{user_id}_{filename}"
        
        upload_folder = os.path.join(current_app.root_path, 'static', 'uploads')
        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder)
        
        file.save(os.path.join(upload_folder, filename))

        if 'id' in session:
            users_service = usersSVC.usersSVC()
            users = usersDTO(id=session['id'])
            users.profile_pic = filename
            users_service.updateProfilePic(users)
        
        session['profile_pic'] = filename
        
        return redirect(url_for('mypage'))
    return redirect(url_for('mypage'))