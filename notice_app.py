from flask import Blueprint, request, redirect, url_for, render_template, session
from noticeDTO import NoticeDTO
from noticeSVC import NoticeSVC

blue_notice = Blueprint('notice', __name__, url_prefix='/notice')
SVC = NoticeSVC()

@blue_notice.route('/')
def notice_list():
    notices = SVC.get_all_notices()
    return render_template('mainnotice.html', notices=notices)

@blue_notice.route('/<int:notice_id>')
def notice_detail(notice_id):
    notice = SVC.get_notice_by_id(notice_id)
    return render_template('noticepage.html', notice=notice)

@blue_notice.route('/add', methods=['GET', 'POST'])
def add_notice():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        author = session['id']
        notice = NoticeDTO(title=title, content=content, author=author)
        SVC.add_notice(notice)
        return redirect(url_for('notice.notice_list'))
    return render_template('noticeadd.html')

@blue_notice.route('/edit/<int:notice_id>', methods=['GET', 'POST'])
def edit_notice(notice_id):
    notice = SVC.get_notice_by_id(notice_id)
    if request.method == 'POST':
        notice.title = request.form['title']
        notice.content = request.form['content']
        SVC.update_notice(notice)
        return redirect(url_for('notice.notice_detail', notice_id=notice_id))
    return render_template('noticeedit.html', notice=notice)

@blue_notice.route('/delete/<int:notice_id>', methods=['POST'])
def delete_notice(notice_id):
    SVC.delete_notice(notice_id)
    return redirect(url_for('notice.notice_list'))