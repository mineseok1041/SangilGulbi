from flask import Flask, render_template, url_for

app = Flask(__name__, static_folder='static')

@app.route('/')
def manager_page():
    return render_template('manager_page_main.html')

@app.route('/user')
def manager_page_user():
    return render_template('manager_page_user.html')

if __name__ == '__main__':
    app.run(debug=True)
