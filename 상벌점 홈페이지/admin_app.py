from flask import Flask, redirect, render_template, session, url_for, Blueprint, request, flash, jsonify

from usersSVC import usersSVC
from usersDTO import usersDTO
from pointSVC import pointSVC
from pointReasonDTO import pointReasonDTO
from pointLogDTO import pointLogDTO
from noticeDTO import NoticeDTO
from noticeSVC import NoticeSVC

adminBlue = Blueprint('admin', __name__, url_prefix='/admin')

usersSVC = usersSVC()
pointSVC = pointSVC()

@adminBlue.route('/')
def index():
    try:
        if 'id' not in session:
            return redirect(url_for('auth.login'))

        return render_template('admin/indexAdmin.html')
    except Exception as e:
        print(e)
        return redirect(url_for('auth.login'))
    
@adminBlue.route('/studentManagement')
def studentManagement():
    try:
        if 'id' not in session:
            return redirect(url_for('auth.login'))

        return render_template('admin/studentManagementAdmin.html')
    except Exception as e:
        print(e)
        return redirect(url_for('auth.login'))
    
@adminBlue.route('/teacherManagement')
def teacherManagement():
    try:
        if 'id' not in session:
            return redirect(url_for('auth.login'))

        return render_template('admin/teacherManagement.html')
    except Exception as e:
        print(e)
        return redirect(url_for('auth.login'))
    
@adminBlue.route('/addStudentPopup')
def addStudentPopup():
    try:
        if 'id' not in session:
            return redirect(url_for('auth.login'))

        return render_template('admin/addStudentPopup.html')
    except Exception as e:
        print(e)
        return redirect(url_for('auth.login'))
    
@adminBlue.route('/addTeacherPopup')
def addTeacherPopup():
    try:
        if 'id' not in session:
            return redirect(url_for('auth.login'))

        return render_template('admin/addTeacherPopup.html')
    except Exception as e:
        print(e)
        return redirect(url_for('auth.login'))
    
@adminBlue.route('/resetTeacherPasswdPopup')
def resetTeacherPasswdPopup():
    try:
        if 'id' not in session:
            return redirect(url_for('auth.login'))

        return render_template('admin/resetTeacherPasswdPopup.html')
    except Exception as e:
        print(e)
        return redirect(url_for('auth.login'))
    
@adminBlue.route('/teacherSignupApprovalPopup')
def teacherSignupApprovalPopup():
    try:
        if 'id' not in session:
            return redirect(url_for('auth.login'))

        return render_template('admin/teacherSignupApprovalPopup.html')
    except Exception as e:
        print(e)
        return redirect(url_for('auth.login'))