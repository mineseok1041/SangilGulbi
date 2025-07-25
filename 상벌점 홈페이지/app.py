from flask import Flask, redirect, render_template, session, url_for, request, flash
from flask_cors import CORS

import requests
import os

from usersSVC import usersSVC
from usersDTO import usersDTO
from noticeSVC import NoticeSVC
from noticeDTO import NoticeDTO

import student_app
import teacher_app
import auth_app
import admin_app

app = Flask(__name__)
CORS(app)
app.secret_key = 'ggulbi'

app.register_blueprint(auth_app.authBlue)
app.register_blueprint(student_app.studentBlue)
app.register_blueprint(teacher_app.teacherBlue)
app.register_blueprint(admin_app.adminBlue)

# 메인페이지
@app.route('/')
def index():
    if session.get('identity') is not None:
        if session.get('identity') == 2:
            return redirect(url_for('student.index'))
        elif session.get('identity') == 1:
            return redirect(url_for('teacher.index'))
        elif session.get('identity') == 0:
            return redirect(url_for('admin.index'))
        else:
            return redirect(url_for('auth.dologout'))
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port=18888)