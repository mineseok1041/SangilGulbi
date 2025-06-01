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
        notices = SVC.get_all_notices()
        return render_template('admin/indexAdmin.html', notices=notices)
    except Exception as e:
        print(e)
        return redirect(url_for('auth.login'))

@adminBlue.route('/studentManagement')
@adminAuth
def studentManagement():
    try:
        return render_template('admin/studentManagementAdmin.html')
    except Exception as e:
        print(e)
        return redirect(url_for('auth.login'))

@adminBlue.route('/teacherManagement')
@adminAuth
def teacherManagement():
    try:
        return render_template('admin/teacherManagementAdmin.html')
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
        return render_template('admin/teacherSignupApprovalPopupAdmin.html')
    except Exception as e:
        print(e)
        return redirect(url_for('auth.login'))

@adminBlue.route('/pointLog')
@adminAuth
def pointLog():
    try:
        return render_template('admin/givePointLogAdmin.html')
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
        if 'id' not in session:
            return redirect(url_for('auth.login'))
        
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