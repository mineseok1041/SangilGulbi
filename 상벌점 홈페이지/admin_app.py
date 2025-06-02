from flask import Flask, redirect, render_template, session, url_for, Blueprint, request, flash, jsonify

from usersSVC import usersSVC
from usersDTO import usersDTO
from pointSVC import pointSVC
from pointReasonDTO import pointReasonDTO
from pointLogDTO import pointLogDTO
from noticeDTO import NoticeDTO
from noticeSVC import NoticeSVC
from auth_app import adminAuth

adminBlue = Blueprint('admin', __name__, url_prefix='/admin')

SVC = NoticeSVC()
usersSVC = usersSVC()
pointSVC = pointSVC()

@adminBlue.route('/')
@adminAuth
def index():
    try:
        studentList = usersSVC.getStudentsList(1)[:5]  # 학생 목록 (최근 활동 기준 상위 5명)
        teacherList = usersSVC.getTeachersList(1)[:5]  # 선생님 목록 (최근 활동 기준 상위 5명)
        notices = SVC.get_all_notices() # 공지사항 목록 (최신순)
        unverifiedTeachers = usersSVC.getUnverifiedTeachers()  # 승인 대기 중인 선생님 계정

        return render_template('admin/indexAdmin.html', notices=notices, studentList=studentList, teacherList=teacherList, unverifiedTeachers=unverifiedTeachers)
    except Exception as e:
        print(e)
        return redirect(url_for('auth.login'))

@adminBlue.route('/studentManagement')
@adminAuth
def studentManagement():
    try:
        studentList = usersSVC.getStudentsList(1)
        return render_template('admin/studentManagementAdmin.html', studentList=studentList)
    except Exception as e:
        print(e)
        return redirect(url_for('auth.login'))

@adminBlue.route('/teacherManagement')
@adminAuth
def teacherManagement():
    try:
        teacherList = usersSVC.getTeachersList(1)  # 선생님 목록 (페이지 1)
        return render_template('admin/teacherManagementAdmin.html', teacherList=teacherList)
    except Exception as e:
        print(e)
        return redirect(url_for('auth.login'))

@adminBlue.route('/addStudentPopup')
@adminAuth
def addStudentPopup():
    try:
        return render_template('admin/addStudentPopupAdmin.html')
    except Exception as e:
        print(e)
        return redirect(url_for('auth.login'))

@adminBlue.route('/addTeacherPopup')
@adminAuth
def addTeacherPopup():
    try:
        return render_template('admin/addTeacherPopupAdmin.html')
    except Exception as e:
        print(e)
        return redirect(url_for('auth.login'))

@adminBlue.route('/resetTeacherPasswordPopup')
@adminAuth
def resetTeacherPasswordPopup():
    try:
        return render_template('admin/resetTeacherPasswdPopupAdmin.html')
    except Exception as e:
        print(e)
        return redirect(url_for('auth.login'))

@adminBlue.route('/resetStudentPasswordPopup')
@adminAuth
def resetStudentPasswordPopup():
    try:
        return render_template('admin/resetStudentPasswdPopupAdmin.html')
    except Exception as e:
        print(e)
        return redirect(url_for('auth.login'))

@adminBlue.route('/teacherSignupApprovalPopup')
@adminAuth
def teacherSignupApprovalPopup():
    try:
        unverified_teachers = usersSVC.getUnverifiedTeachers()
        return render_template('admin/teacherSignupApprovalPopupAdmin.html', unverified_teachers=unverified_teachers)
    except Exception as e:
        print(e)
        return redirect(url_for('auth.login'))

@adminBlue.route('/pointLog')
@adminAuth
def pointLog():
    try:
        pointLogList = pointSVC.getPointLog(1)
        return render_template('admin/givePointLogAdmin.html', pointLogList=pointLogList)
    except Exception as e:
        print(e)
        return redirect(url_for('auth.login'))

@adminBlue.route('/pointReasons')
@adminAuth
def pointReasons():
    try:
        return render_template('admin/pointReasonsAdmin.html')
    except Exception as e:
        print(e)
        return redirect(url_for('auth.login'))

@adminBlue.route('/community')
@adminAuth
def community():
    try:
        teacherDTO = usersDTO(id=session['id'], name=session['name'], identity=session['identity'])
        notices = SVC.get_all_notices()
        return render_template('admin/communityAdmin.html', notices=notices)
    except Exception as e:
        print(e)
        return redirect(url_for('auth.login'))

@adminBlue.route('/community/add')
@adminAuth
def communityAdd():
    try:
        return render_template('admin/communityAddAdmin.html')
    except Exception as e:
        print(e)
        return redirect(url_for('auth.login'))

@adminBlue.route('/community/edit')
@adminAuth
def communityEdit():
    try:
        return render_template('admin/communityEditAdmin.html')
    except Exception as e:
        print(e)
        return redirect(url_for('auth.login'))

@adminBlue.route('/community/info')
@adminAuth
def communityInfo():
    try:
        return render_template('admin/communityInfoAdmin.html')
    except Exception as e:
        print(e)
        return redirect(url_for('auth.login'))

@adminBlue.route('/giveBonusPointPopup')
@adminAuth
def giveBonusPointPopup():
    try:
        return render_template('admin/giveBonusPointPopupAdmin.html')
    except Exception as e:
        print(e)
        return redirect(url_for('auth.login'))

@adminBlue.route('/givePenaltyPointPopup')
@adminAuth
def givePenaltyPointPopup():
    try:
        return render_template('admin/givePenaltyPointPopupAdmin.html')
    except Exception as e:
        print(e)
        return redirect(url_for('auth.login'))

@adminBlue.route('/approveTeacher', methods=['POST'])
@adminAuth
def approveTeacher():
    try:
        teacher_id = request.json.get('teacherId')  # JSON 데이터에서 teacherId 가져오기
        if not teacher_id:
            raise Exception("선생님 ID가 제공되지 않았습니다.")
        
        # 승인 처리
        usersSVC.updateTeacherVerified(teacher_id, verified=1)
        return jsonify({"success": True, "message": "선생님 계정이 승인되었습니다."})
    except Exception as e:
        print(f"Error in approveTeacher: {e}")
        return jsonify({"success": False, "message": str(e)})

@adminBlue.route('/rejectTeacher', methods=['POST'])
@adminAuth
def rejectTeacher():
    try:
        teacher_id = request.json.get('teacherId')  # JSON 데이터에서 teacherId 가져오기
        if not teacher_id:
            raise Exception("선생님 ID가 제공되지 않았습니다.")
        
        # 거부 처리 (삭제 또는 다른 처리)
        usersSVC.delUsers(usersDTO(id=teacher_id))
        return jsonify({"success": True, "message": "선생님 계정이 거부되었습니다."})
    except Exception as e:
        print(f"Error in rejectTeacher: {e}")
        return jsonify({"success": False, "message": str(e)})