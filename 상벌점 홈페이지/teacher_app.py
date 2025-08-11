from flask import Flask, redirect, render_template, session, url_for, Blueprint, request, flash, jsonify
from datetime import datetime
from usersSVC import usersSVC
from usersDTO import usersDTO
from pointSVC import pointSVC
from pointReasonDTO import pointReasonDTO
from pointLogDTO import pointLogDTO
from noticeDTO import NoticeDTO
from noticeSVC import NoticeSVC
from auth_app import teacherAuth

teacherBlue = Blueprint('teacher', __name__, url_prefix='/teacher')

SVC = NoticeSVC()
usersSVC = usersSVC()
pointSVC = pointSVC()

@teacherBlue.route('/')
@teacherAuth
def index():
    try:
        pointLogList = pointSVC.getPointLogByStdID(usersDTO(id=session['id']), 1, 'all')

        # 상점과 벌점 분리
        bonusPointLogList = [log for log in pointLogList if log.type == 'bonus']
        penaltyPointLogList = [log for log in pointLogList if log.type == 'penalty']
        
        # bonusPointLogList = pointSVC.getPointLogByTeacherID(usersDTO(id=session['id']), 1, 'bonus')
        # penaltyPointLogList = pointSVC.getPointLogByTeacherID(usersDTO(id=session['id']), 1, 'penalty')
        notices = SVC.get_all_notices()  # 게시글 목록 가져오기
    
        return render_template('teacher/indexTeacher.html', notices=notices, bonusPointLogList=bonusPointLogList, penaltyPointLogList=penaltyPointLogList)
    except Exception as e:
        print(e)
        return redirect(url_for('auth.login'))

@teacherBlue.route('/pointLog')
@teacherAuth
def pointLog():
    try:
        page = request.args.get('page', default=1, type=int)
        maxPage = pointSVC.getTeacherPointLogMaxPage(usersDTO(id=session['id']))
        
        pointLogList = pointSVC.getPointLogByTeacherID(usersDTO(id=session['id']), page, 'all')

        if page > maxPage:
            page = maxPage
        if page < 1:
            page = 1
    
        return render_template('teacher/givePointLog.html', pointLogList=pointLogList, currentPage=page, maxPage=maxPage)
    except Exception as e:
        print(e)
        return redirect(url_for('index'))
    
@teacherBlue.route('/pointReasons')
@teacherAuth
def pointReasons():
    bonusPointReasons = pointSVC.getPointReason('bonus')
    penaltyPointReasons = pointSVC.getPointReason('penalty')

    favoritePointNo = pointSVC.getFavoritePointReasonNo(usersDTO(id=session['id']))
    
    return render_template('teacher/pointReasonsTeacher.html', bonusPointReasonDTO=bonusPointReasons, penaltyPointReasonDTO=penaltyPointReasons, favoritePointNo=favoritePointNo)

@teacherBlue.route('/studentManagement')
@teacherAuth
def studentManagement():
    try:
        page = request.args.get('page', default=1, type=int)
        maxPage = usersSVC.getStudentMaxPage()

        teacherDTO = usersDTO(id=session['id'], name=session['name'], identity=session['identity'])
        studentList = usersSVC.getStudentsList(page)

        if page > maxPage:
            page = maxPage
        if page < 1:
            page = 1
    
        return render_template('teacher/studentManagementTeacher.html', usersDTO=teacherDTO, studentList=studentList, currentPage=page, maxPage=maxPage)
    except Exception as e:
        print(e)
        return redirect(url_for('auth.login'))

@teacherBlue.route('/resetStudentPasswordPopup', methods=['GET'])
@teacherAuth
def resetStudentPasswordPopup():
    studentNum = request.args.get('studentNum', '')
    studentName = request.args.get('studentName', '')
    studentId = request.args.get('studentId', '')
    studentList = usersSVC.getStudentsList(1)  # 학생 검색 모달용
    return render_template(
        'teacher/resetStudentPasswdPopup.html',
        studentNum=studentNum,
        studentName=studentName,
        studentId=studentId,
        studentList=studentList
    )

@teacherBlue.route('/resetStudentPasswordPopup.do', methods=['POST'])
@teacherAuth
def resetStudentPasswordPopup_do():
    studentId = request.form.get('studentId')
    password = request.form.get('password')
    passwordCheck = request.form.get('passwordCheck')
    if not studentId or not password or not passwordCheck:
        return "<script>alert('모든 정보를 입력해주세요.'); history.back();</script>"
    if password != passwordCheck:
        return "<script>alert('비밀번호가 일치하지 않습니다.'); history.back();</script>"
    try:
        usersSVC.usersDAO.updatePassword(studentId, password)
        return "<script>alert('비밀번호가 변경되었습니다.'); window.close();</script>"
    except Exception as e:
        return f"<script>alert('오류: {e}'); history.back();</script>"
    
@teacherBlue.route('/resetTeacherPasswordPopup', methods=['GET'])
@teacherAuth
def resetTeacherPasswordPopup():
    teacherName = request.args.get('teacherName', '')
    teacherId = request.args.get('teacherId', '')
    teacherList = usersSVC.getTeachersList(1)
    return render_template(
        'teacher/resetTeacherPasswdPopup.html',
        teacherName=teacherName,
        teacherId=teacherId,
        teacherList=teacherList
    )

@teacherBlue.route('/resetTeacherPasswordPopup.do', methods=['POST'])
@teacherAuth
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
    
@teacherBlue.route('/deleteStudentAccount', methods=['POST'])
@teacherAuth
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

@teacherBlue.route('/deleteTeacherAccount', methods=['POST'])
@teacherAuth
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

# ------------------ community(게시판) 기능 ------------------

@teacherBlue.route('/community')
@teacherAuth
def community():
    try:
        teacherDTO = usersDTO(id=session['id'], name=session['name'], identity=session['identity'])
        notices = SVC.get_all_notices()
        return render_template('teacher/communityTeacher.html', usersDTO=teacherDTO, notices=notices)
    except Exception as e:
        print(e)
        return redirect(url_for('index'))
    
@teacherBlue.route('/community/<int:noticeId>')
@teacherAuth
def communityDetail(noticeId):
    try:
        notice = SVC.get_notice_by_id(noticeId)
        return render_template('teacher/communityInfoTeacher.html', notice=notice)
    except Exception as e:
        print(e)
        return redirect(url_for('teacher.community'))

@teacherBlue.route('/community/add', methods=['GET', 'POST'])
@teacherAuth
def communityAdd():
    try:
        if request.method == 'POST':
            title = request.form['title']
            content = request.form['content']
            author = session['id']
            notice = NoticeDTO(title=title, content=content, author=author)
            SVC.add_notice(notice)
            return redirect(url_for('teacher.community'))
        return render_template('teacher/communityAddTeacher.html')
    except Exception as e:
        print(e)
        return redirect(url_for('teacher.community'))

@teacherBlue.route('/community/edit/<int:noticeId>', methods=['GET', 'POST'])
@teacherAuth
def communityEdit(noticeId):
    try:
        notice = SVC.get_notice_by_id(noticeId)
        if request.method == 'POST':
            notice.title = request.form['title']
            notice.content = request.form['content']
            SVC.update_notice(notice)
            return redirect(url_for('teacher.communityDetail', noticeId=noticeId))
        return render_template('teacher/communityEditTeacher.html', notice=notice)
    except Exception as e:
        print(e)
        return redirect(url_for('teacher.community'))

@teacherBlue.route('/community/delete/<int:noticeId>', methods=['POST'])
@teacherAuth
def communityDelete(noticeId):
    try:
        SVC.delete_notice(noticeId)
        return redirect(url_for('teacher.community'))
    except Exception as e:
        print(e)
        return redirect(url_for('teacher.community'))
    
@teacherBlue.route('/giveBonusPoint')
@teacherAuth
def giveBonusPoint():
    try:
        teacherDTO = usersDTO(id=session['id'], name=session['name'], identity=session['identity'])
        studentList = usersSVC.getStudentsList(1)
        teacherList = usersSVC.getTeachersList(1)
        pointReasonList = pointSVC.getFavPointReason('bonus', usersDTO(id=session['id']))
        currentDate = datetime.now().strftime('%Y/%m/%d')

        print(pointReasonList)
    
        return render_template('teacher/giveBonusPointPopup.html', usersDTO=teacherDTO, studentList=studentList, teacherList=teacherList, pointReasonList=pointReasonList, currentDate=currentDate)
    except Exception as e:
        print(e)
        return redirect(url_for('index'))
    
@teacherBlue.route('/givePenaltyPoint')
@teacherAuth
def givePenaltyPoint():
    try:
        teacherDTO = usersDTO(id=session['id'], name=session['name'], identity=session['identity'])
        studentList = usersSVC.getStudentsList(1)
        teacherList = usersSVC.getTeachersList(1)
        pointReasonList = pointSVC.getFavPointReason('penalty', usersDTO(id=session['id']))
        currentDate = datetime.now().strftime('%Y/%m/%d')
            
        return render_template('teacher/givePenaltyPointPopup.html', usersDTO=teacherDTO, studentList=studentList, teacherList=teacherList, pointReasonList=pointReasonList, currentDate=currentDate)
    except Exception as e:
        print(e)
        return redirect(url_for('index'))
    
@teacherBlue.route('/giveBonusPoint.do', methods=['POST'])
@teacherAuth
def doGiveBonusPoint():
    try:
        stdId = request.form['stdId']
        reason = request.form['reason']
        point = request.form['point']
        writeTeacherId = request.form['writeTeacherId']
        giveTeacherId = request.form['giveTeacherId']
        opinion = request.form['opinion']

        stdDTO = usersDTO(id=stdId)
        writerDTO = usersDTO(id=writeTeacherId)
        giverDTO = usersDTO(id=giveTeacherId)
        point = int(point)
        
        pointSVC.givePoint(stdDTO, writerDTO, giverDTO, point, reason, opinion)

        return "<script>alert('상점이 부과되었습니다.'); opener.location.reload(); window.close();</script>"
    except Exception as e:
        print(e)
        flash('모든 항목을 작성해주세요')
        return redirect(url_for('teacher.giveBonusPoint'))
    
@teacherBlue.route('/givePenaltyPoint.do', methods=['POST'])
@teacherAuth
def doGivePenaltyPoint():
    try:
        stdId = request.form['stdId']
        reason = request.form['reason']
        point = request.form['point']
        writeTeacherId = request.form['writeTeacherId']
        giveTeacherId = request.form['giveTeacherId']
        opinion = request.form['opinion']

        stdDTO = usersDTO(id=stdId)
        writerDTO = usersDTO(id=writeTeacherId)
        giverDTO = usersDTO(id=giveTeacherId)
        point = int(point)*(-1)
        
        pointSVC.givePoint(stdDTO, writerDTO, giverDTO, point, reason, opinion)

        return "<script>alert('벌점이 부과되었습니다.'); opener.location.reload(); window.close();</script>"
    except Exception as e:
        print(e)
        flash('모든 항목을 작성해주세요')
        return redirect(url_for('teacher.giveBonusPoint'))

@teacherBlue.route('/resetTeacherPasswdPopup')
@teacherAuth
def resetTeacherPasswdPopup():
    teacherList = usersSVC.getTeachersList(1)
    try:
        if 'id' not in session:
            return redirect(url_for('index'))
        return render_template('teacher/resetTeacherPasswdPopup.html', teacherList=teacherList)
    except Exception as e:
        print(e)
        return 'Error'
    
@teacherBlue.route('/resetStudentPasswdPopup')
@teacherAuth
def resetStudentPasswdPopup():
    try:
        if 'id' not in session:
            return redirect(url_for('index'))
        
        return render_template('teacher/resetStudentPasswdPopup.html')
    except Exception as e:
        print(e)
        return 'Error'
    
@teacherBlue.route('/searchStudents')
@teacherAuth
def searchStudents():
    keyword = request.args.get('keyword', '').strip()
    try:
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
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@teacherBlue.route('/pointCancel.do' , methods=['POST'])
@teacherAuth
def pointCancel():
    try:
        data = request.get_json()
        logNo = int(data.get('no'))

        pointSVC.cancelPointLog(logNo)

        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})
    
@teacherBlue.route('/addFavoritePointReason.do/<int:pointNo>', methods=['POST'])
@teacherAuth
def addFavoritePointReason(pointNo):
    try:
        user = usersDTO(id=session.get('id'))
        pointReason = pointReasonDTO(no=pointNo)

        pointSVC.addFavoritePointReason(user, pointReason)
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@teacherBlue.route('/removeFavoritePointReason.do/<int:pointNo>', methods=['POST'])
@teacherAuth
def removeFavoritePointReason(pointNo):
    try:
        user = usersDTO(id=session.get('id'))
        pointReason = pointReasonDTO(no=pointNo)

        pointSVC.removeFavoritePointReason(user, pointReason)
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
