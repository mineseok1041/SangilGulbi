from flask import Blueprint, render_template, request, redirect, url_for, session
from noticeDTO import NoticeDTO
from noticeSVC import NoticeSVC
from usersSVC import usersSVC
from usersDTO import usersDTO
from pointSVC import pointSVC
from pointLogDTO import pointLogDTO
from auth_app import studentAuth

studentBlue = Blueprint('student', __name__, url_prefix='/student')
usersSVC = usersSVC()
pointSVC = pointSVC()
noticeSVC = NoticeSVC()

@studentBlue.route('/')
@studentAuth
def index():
    try:
        if 'id' not in session:
            return redirect(url_for('auth.login'))
        
        # 사용자 정보 가져오기
        respDTO = usersSVC.getUsersInfo(usersDTO(id=session['id']))
        
        # 상벌점 내역 가져오기
        pointLogList = pointSVC.getPointLogByStdID(usersDTO(id=session['id']))
        
        # 상점과 벌점 분리
        bonusLogs = [log for log in pointLogList if log.type == 'bonus']
        penaltyLogs = [log for log in pointLogList if log.type == 'penalty']
        
        # 총 상점과 벌점 계산
        totalBonus = sum(log.point for log in bonusLogs)
        totalPenalty = sum(log.point for log in penaltyLogs)
        
        # 공지사항 가져오기
        notices = noticeSVC.get_all_notices()[:5]

        return render_template(
            'student/indexStudent.html',
            usersDTO=respDTO,
            notices=notices,
            bonusLogs=bonusLogs[:5],  # 상점 최근 5개
            penaltyLogs=penaltyLogs[:5],  # 벌점 최근 5개
            totalBonus=totalBonus,
            totalPenalty=totalPenalty
        )
    except Exception as e:
        print(e)
        return redirect(url_for('auth.login'))

@studentBlue.route('/pointLog')
@studentAuth
def pointLog():
    if 'id' not in session:
        return redirect(url_for('auth.login'))

    respDTO = usersDTO(id=session['id'], name=session['name'], stdNum=session['stdNum'], identity=session['identity'])
    pointLogList = pointSVC.getPointLogByStdID(usersDTO(id=session['id']))
    
    return render_template('student/pointLogStudent.html', usersDTO=respDTO, pointLogList=pointLogList)

@studentBlue.route('/pointReasons')
@studentAuth
def pointReasons():
    if 'id' not in session:
        return redirect(url_for('index'))

    respDTO = usersDTO(id=session['id'], name=session['name'], stdNum=session['stdNum'], identity=session['identity'])
    bonusPointReasons = pointSVC.getPointReason('bonus')
    penaltyPointReasons = pointSVC.getPointReason('penalty')
    
    return render_template('student/pointReasonsStudent.html', usersDTO=respDTO, bonusPointReasonDTO=bonusPointReasons, penaltyPointReasonDTO=penaltyPointReasons)

# ------------------ community(게시판) 기능 ------------------

@studentBlue.route('/community')
@studentAuth
def communityList():
    if 'id' not in session:
        return redirect(url_for('index'))
    
    respDTO = usersDTO(id=session['id'], name=session['name'], stdNum=session['stdNum'], identity=session['identity'])
    notices = noticeSVC.get_all_notices()

    return render_template('student/communityStudent.html', notices=notices, usersDTO=respDTO)

@studentBlue.route('/community/<int:noticeId>')
@studentAuth
def communityDetail(noticeId):
    if 'id' not in session:
        return redirect(url_for('index'))
    respDTO = usersDTO(id=session['id'], name=session['name'], stdNum=session['stdNum'], identity=session['identity'])
    notice = noticeSVC.get_notice_by_id(noticeId)
    return render_template('student/communityInfoStudent.html', notice=notice, usersDTO=respDTO)
