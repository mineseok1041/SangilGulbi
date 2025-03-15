from flask import Blueprint, request, redirect, url_for, flash, session, make_response, render_template, jsonify
from usersDTO import usersDTO
import usersSVC

blue_management = Blueprint('management', __name__, url_prefix='/management')

SVC = usersSVC.usersSVC()

@blue_management.route('/')
def manager_page():
    return render_template('manager_page_main.html')

@blue_management.route('/student/')
@blue_management.route('/student')
def redirect_to_student_default():
    return redirect('student/1')

@blue_management.route('/student/<int:page>')
def manager_page_student(page):
    usersDTO = SVC.getStudentsList(page)
    return render_template('manager_page_user.html', usersDTO=usersDTO)

@blue_management.route('/manager/')
@blue_management.route('/manager')
def redirect_to_manager_default():
    return redirect('manager/1')

@blue_management.route('/manager/<int:page>')
def manager_page_add(page):
    return render_template('manager_page_manager.html')

@blue_management.route('/addPoint.do', methods=['POST'])
def addPoint():
    data = request.form.to_dict()  # 기존 폼 데이터 가져오기
    user_ids = request.form.get("userIds")  # 체크된 userIds 가져오기
    checked_user_list = user_ids.split(",") if user_ids else []  # 문자열을 리스트로 변환

    print("Checked user IDs:", checked_user_list)
    print("Received form data:", data)
        
    return jsonify({"status": "success", "message": "Data received successfully"}), 200
        