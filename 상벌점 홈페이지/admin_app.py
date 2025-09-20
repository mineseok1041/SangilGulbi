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
        page = request.args.get('page', default=1, type=int)
        maxPage = usersSVC.getStudentMaxPage()

        studentList = usersSVC.getStudentsList(page)

        if page > maxPage:
            page = maxPage
        if page < 1:
            page = 1

        return render_template('admin/studentManagementAdmin.html', studentList=studentList, currentPage=page, maxPage=maxPage)
    except Exception as e:
        print(e)
        return redirect(url_for('auth.login'))

@adminBlue.route('/teacherManagement')
@adminAuth
def teacherManagement():
    try:
        page = int(request.args.get('page', 1))
        teacherList = usersSVC.getTeachersList(page)
        maxPage = usersSVC.getTeacherMaxPage()
        unverified_count = len(usersSVC.getUnverifiedTeachers())
        return render_template(
            'admin/teacherManagementAdmin.html',
            teacherList=teacherList,
            currentPage=page,
            maxPage=maxPage,
            unverified_count=unverified_count
        )
    except Exception as e:
        flash(str(e))
        return redirect(url_for('admin.index'))

@adminBlue.route('/addStudentPopup')
@adminAuth
def addStudentPopup():
    try:
        return render_template('admin/addStudentPopupAdmin.html')
    except Exception as e:
        print(e)
        return redirect(url_for('auth.login'))
    
@adminBlue.route('/addStudent.do', methods=['POST'])
@adminAuth
def addStudent():
    try:
        stdNum = request.form.get('stdNum')
        name = request.form.get('name')
        id = request.form.get('id')
        password = request.form.get('password')
        passwordCheck = request.form.get('passwordCheck')

        if password != passwordCheck:
            flash("비밀번호가 일치하지 않습니다.")
            return redirect(url_for('admin.addStudentPopup'))

        # 학생 추가
        usersSVC.signup(usersDTO(stdNum=stdNum, name=name, id=id, password=password, identity=2))
        return "<script>alert('학생이 성공적으로 추가되었습니다.'); window.close();</script>"
    except Exception as e:
        flash("학생 추가 중 오류가 발생했습니다: " + str(e))
        return redirect(url_for('admin.addStudentPopup'))
    
@adminBlue.route('/deleteStudentAccount', methods=['POST'])
@adminAuth
def deleteStudentAccount():
    try:
        data = request.get_json()
        studentId = data.get('studentId')
        if not studentId:
            return jsonify({"success": False, "error": "학생 ID가 없습니다."})
        usersSVC.delUsers(usersDTO(id=studentId))
        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})


@adminBlue.route('/addTeacherPopup')
@adminAuth
def addTeacherPopup():
    try:
        return render_template('admin/addTeacherPopupAdmin.html')
    except Exception as e:
        print(e)
        return redirect(url_for('auth.login'))
    
@adminBlue.route('/addTeacher.do', methods=['POST'])
@adminAuth
def addTeacher():
    try:
        name = request.form.get('name')
        id = request.form.get('id')
        password = request.form.get('password')
        passwordCheck = request.form.get('passwordCheck')

        if not name or not id or not password or not passwordCheck:
            return "<script>alert('모든 정보를 입력해주세요.'); history.back();</script>"
        if password != passwordCheck:
            return "<script>alert('비밀번호가 일치하지 않습니다.'); history.back();</script>"

        # 중복 아이디 체크
        if usersSVC.isIDExist(usersDTO(id=id)):
            return "<script>alert('이미 존재하는 아이디입니다. 다른 아이디를 입력해주세요.'); history.back();</script>"

        # 선생님 추가 (identity=1, verified=1로 바로 승인)
        usersSVC.signup(usersDTO(name=name, id=id, password=password, identity=1, verified=1))
        return "<script>alert('선생님 계정이 성공적으로 추가되었습니다.'); window.close();</script>"
    except Exception as e:
        return f"<script>alert('추가 중 오류 발생: {e}'); history.back();</script>"

@adminBlue.route('/resetTeacherPasswdPopup')
@adminAuth
def resetTeacherPasswdPopup():
    try:
        teacherName = request.args.get('teacherName', '')
        teacherId = request.args.get('teacherId', '')
        teacherList = usersSVC.getTeachersList(1)
        return render_template(
            'admin/resetTeacherPasswdPopupAdmin.html',
            teacherName=teacherName,
            teacherId=teacherId,
            teacherList=teacherList
        )
    except Exception as e:
        print(e)
        return redirect(url_for('auth.login'))
    
@adminBlue.route('/resetTeacherPasswordPopup.do', methods=['POST'])
@adminAuth
def resetTeacherPasswordPopup_do():
    teacherId = request.form.get('teacherId')
    password = request.form.get('password')
    passwordCheck = request.form.get('passwordCheck')
    if not teacherId or not password or not passwordCheck:
        return "<script>alert('모든 정보를 입력해주세요.'); history.back();</script>"
    if password != passwordCheck:
        return "<script>alert('비밀번호가 일치하지 않습니다.'); history.back();</script>"
    try:
        usersSVC.usersDAO.updatePassword(teacherId, password)
        return "<script>alert('비밀번호가 변경되었습니다.'); window.close();</script>"
    except Exception as e:
        return f"<script>alert('오류: {e}'); history.back();</script>"

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
        page = request.args.get('page', default=1, type=int)
        maxPage = pointSVC.getPointLogMaxPage()
        if page > maxPage:
            page = maxPage
        if page < 1:
            page = 1

        pointLogList = pointSVC.getPointLog(page, 'all')

        return render_template('admin/givePointLogAdmin.html', pointLogList=pointLogList, currentPage=page, maxPage=maxPage)
    except Exception as e:
        print(e)
        return redirect(url_for('auth.login'))
    
@adminBlue.route('/pointCancel.do' , methods=['POST'])
@adminAuth
def pointCancel():
    try:
        data = request.get_json()
        logNo = int(data.get('no'))

        pointSVC.cancelPointLog(logNo)

        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@adminBlue.route('/pointReasons')
@adminAuth
def pointReasons():
    try:
        bonusPointReasons = pointSVC.getPointReason('bonus')
        penaltyPointReasons = pointSVC.getPointReason('penalty')

        return render_template('admin/pointReasonsAdmin.html', bonusPointReasonDTO=bonusPointReasons, penaltyPointReasonDTO=penaltyPointReasons)
    except Exception as e:
        print(e)
        return redirect(url_for('auth.login'))

@adminBlue.route('/community')
@adminAuth
def community():
    try:
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

@adminBlue.route('/community/<int:noticeId>')
@adminAuth
def communityDetail(noticeId):
    try:
        if 'id' not in session:
            return redirect(url_for('index'))
        notice = SVC.get_notice_by_id(noticeId)
        return render_template('admin/communityInfoAdmin.html', notice=notice)
    except Exception as e:
        print(e)
        return redirect(url_for('admin.community'))

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
    
@adminBlue.route('/searchStudents')
@adminAuth
def search_students():
    keyword = request.args.get('keyword', '').strip()
    students = usersSVC.searchStudentsByKeyword(keyword)
    return jsonify([
        {
            'stdNum': s.stdNum,
            'name': s.name,
            'id': s.id,
            'lastlogindate': s.lastlogindate,
            'point': s.point
        } for s in students
    ])

@adminBlue.route('/searchTeachers')
@adminAuth
def search_teachers():
    keyword = request.args.get('keyword', '').strip()
    teachers = usersSVC.searchTeachersByKeyword(keyword)
    return jsonify([
        {
            'name': t.name,
            'id': t.id,
        } for t in teachers
    ])

@adminBlue.route('/deleteTeacherAccount', methods=['POST'])
@adminAuth
def deleteTeacherAccount():
    try:
        data = request.get_json()
        teacherId = data.get('teacherId')
        if not teacherId:
            return jsonify({"success": False, "error": "선생님 ID가 없습니다."})
        usersSVC.delUsers(usersDTO(id=teacherId))
        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})
    
@adminBlue.route('/searchPointLogs')
@adminAuth
def search_point_logs():
    keyword = request.args.get('keyword', '').strip()
    try:
        result = pointSVC.searchPointLogs(keyword)
        return jsonify([log.__dict__ for log in result])
    except Exception as e:
        return jsonify([])