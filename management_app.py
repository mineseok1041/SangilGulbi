from flask import Blueprint, request, redirect, url_for, flash, session, make_response, render_template
from usersDTO import usersDTO
import usersSVC

blue_management = Blueprint('management', __name__, url_prefix='/management')

SVC = usersSVC.usersSVC()

@blue_management.route('/')
def manager_page():
    return render_template('manager_page_main.html')

@blue_management.route('/user/')
@blue_management.route('/user')
def redirect_to_user_default():
    return redirect('user/1')

@blue_management.route('/user/<int:page>')
def manager_page_user(page):
    usersDTO = SVC.getUsersList(page)
    return render_template('manager_page_user.html', usersDTO=usersDTO)

@blue_management.route('/manager/')
@blue_management.route('/manager')
def redirect_to_manager_default():
    return redirect('manager/1')

@blue_management.route('/manager/<int:page>')
def manager_page_add(page):
    return render_template('manager_page_add.html')