from noticeDAO import NoticeDAO
from noticeDTO import NoticeDTO

class NoticeSVC:
    def __init__(self):
        self.DAO = NoticeDAO()

    def get_all_notices(self):
        return self.DAO.get_all_notices()

    def get_notice_by_id(self, notice_id):
        return self.DAO.get_notice_by_id(notice_id)

    def add_notice(self, notice):
        self.DAO.add_notice(notice)

    def update_notice(self, notice):
        self.DAO.update_notice(notice)

    def delete_notice(self, notice_id):
        self.DAO.delete_notice(notice_id)