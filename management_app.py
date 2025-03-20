from flask import Blueprint, request, redirect, url_for, flash, session, make_response, render_template, jsonify
from usersDTO import usersDTO
import usersSVC

blue_management = Blueprint('management', __name__, url_prefix='/management')

SVC = usersSVC.usersSVC()

@blue_management.route('/')
def manager_page():
    if 'identity' not in session or session['identity'] not in [0, 1]:
        return redirect(url_for('index'))
    return render_template('manager_page_main.html')

@blue_management.route('/student/')
@blue_management.route('/student')
def redirect_to_student_default():
    if 'identity' not in session or session['identity'] not in [0, 1]:
        return redirect(url_for('index'))
    return redirect('student/1')

@blue_management.route('/student/<int:page>')
def manager_page_student(page):
    if 'identity' not in session or session['identity'] not in [0, 1]:
        return redirect(url_for('index'))
    usersDTO = SVC.getStudentsList(page)
    return render_template('manager_page_user.html', usersDTO=usersDTO)

@blue_management.route('/manager/')
@blue_management.route('/manager')
def redirect_to_manager_default():
    if 'identity' not in session or session['identity'] != 0:
        return redirect(url_for('index'))
    return redirect('manager/1')

@blue_management.route('/manager/<int:page>')
def manager_page_add(page):
    if 'identity' not in session or session['identity'] != 0:
        return redirect(url_for('index'))
    managers = SVC.getManagersList(page)
    return render_template('manager_page_manager.html', managers=managers)

@blue_management.route('/add_manager', methods=['POST'])
def add_manager():
    if 'identity' not in session or session['identity'] != 0:
        return redirect(url_for('index'))
    name = request.form['name']
    id = request.form['id']
    password = request.form['password']
    new_manager = usersDTO(name=name, id=id, password=password, identity=1)
    SVC.signup(new_manager)
    return redirect(url_for('management.manager_page_add', page=1))

@blue_management.route('/addPoint.do', methods=['POST'])
def addPoint():
    if 'identity' not in session or session['identity'] not in [0, 1]:
        return redirect(url_for('index'))
    try:
        data = request.form.to_dict()
        userIds = request.form.get("userIds")
        checkedUserList = userIds.split(",") if userIds else []
        addPointSelect = request.form.get("addPointSelect")
        delPointSelect = request.form.get("delPointSelect")

        addPointSelect = int(addPointSelect) if addPointSelect else None
        delPointSelect = int(delPointSelect) if delPointSelect else None
        
        point = 0
        if addPointSelect is None:
            pass
        elif addPointSelect == 1:
            point = 1
        elif addPointSelect in [2, 3]:
            point = 2
        elif addPointSelect in [4, 5, 7, 9]:
            point = 3
        elif addPointSelect in [6, 8, 10]:
            point = 4
        elif addPointSelect in [11, 12]:
            point = 5
        
        if delPointSelect is None:
            pass
        elif delPointSelect in [1, 2, 5, 6, 7]:
            point = -1
        elif delPointSelect in [4, 8, 9, 14]:
            point = -2
        elif delPointSelect in [3, 12, 13, 15]:
            point = -3
        elif delPointSelect in [16, 17, 18, 24]:
            point = -4
        elif delPointSelect in [10, 11, 19, 20, 23]: 
            point = -5
        elif delPointSelect == 21:
            point = -7
        elif delPointSelect == 22:
            point = -10

        print(point)
        
        for user in checkedUserList:
            reqDTO = usersDTO(id=user)
            SVC.addPoint(reqDTO, point)
            
        if point > 0:
            return jsonify({"status": "success", "message": f"상점 {point}점이 부여되었습니다."}), 200
        elif point < 0:
            return jsonify({"status": "success", "message": f"벌점 {point}점이 부여되었습니다."}), 200
        else:
            return jsonify({"status": "error", "message": f"Error: {e}"}), 500

    except Exception as e:
        return jsonify({"status": "error", "message": f"Error: {e}"}), 500