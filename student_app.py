from flask import Blueprint, request, redirect, url_for, flash
import studentSVC
from studentDTO import studentDTO


blue_student = Blueprint('student', __name__, url_prefix='/student')

SVC = studentSVC.studentSVC()

@blue_student.route('/signup.do', methods=['POST'])
def dosignup():
    id = request.form['id']
    password = request.form['password']
    name = request.form['name']
    email = request.form['email']
    birth = request.form['birth']
    birth = birth.replace("-", "")
    
    reqDTO = studentDTO(id=id, password=password, name=name, email=email, birth=birth)

    try:
        SVC.signup(reqDTO)
        print("signup success")
        
        return redirect(url_for('index'))
    except Exception as e:
        print(e)
        return redirect(url_for('signup'))
    
@blue_student.route('/test')
def test():
    return "test success"