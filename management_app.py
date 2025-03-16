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
    try:
        data = request.form.to_dict()
        userIds = request.form.get("userIds")
        checkedUserList = userIds.split(",") if userIds else []
        addPointSelect = request.form.get("addPointSelect")
        delPointSelect = request.form.get("delPointSelect")
        
        if addPointSelect == None:
            pass
        elif addPointSelect == 1:
            point = 1
        elif addPointSelect == 2 or 3:
            point = 2
        elif addPointSelect == 4 or 5 or 7 or 9:
            point = 3
        elif addPointSelect == 6 or 8 or 10:
            point = 4
        elif addPointSelect == 11 or 12: 
            point = 5
        
        if delPointSelect == None:
            pass
        elif delPointSelect == 1 or 2 or 5 or 6 or 7:
            point = -1
        elif delPointSelect == 4 or 8 or 9 or 14:
            point = -2
        elif delPointSelect == 3 or 12 or 13 or 15:
            point = -3
        elif delPointSelect == 16 or 17 or  18 or 24:
            point = -4
        elif delPointSelect == 10 or 11 or 19 or 20 or 23: 
            point = -5
        elif delPointSelect == 21:
            point = -7
        elif delPointSelect == 22:
            point = -10
        
        for user in checkedUserList:
            reqDTO = usersDTO(id=user)
            SVC.addPoint(reqDTO, point)

        return jsonify({"status": "success", "message": "Data received successfully"}), 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"status": "error", "message": f"Error: {e}"}), 500