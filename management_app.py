from flask import Blueprint

blue_management = Blueprint('management', __name__, url_prefix='/management')

@app.route('/')
def manager_page():
    return render_template('manager_page_main.html')

@app.route('/user/')
@app.route('/user')
def redirect_to_default():
    return redirect('/user/1')

@app.route('/user/<int:page>')
def manager_page_user():
    return render_template('manager_page_user.html')

@app.route('/manager/<int:page>')
def manager_page_add():
    return render_template('manager_page_managerList.html')