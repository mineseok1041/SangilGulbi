from noticeDAO import NoticeDAO
from noticeDTO import NoticeDTO

class NoticeSVC:
    def __init__(self):
        self.DAO = NoticeDAO()

    # 모든 공지사항 가져오기
    def get_all_notices(self):
        return self.DAO.get_all_notices()

    # 공지사항 ID로 공지사항 가져오기
    def get_notice_by_id(self, notice_id):
        return self.DAO.get_notice_by_id(notice_id)

    # 공지사항 추가
    def add_notice(self, notice):
        self.DAO.add_notice(notice)

    # 공지사항 수정
    def update_notice(self, notice):
        self.DAO.update_notice(notice)

    # 공지사항 삭제
    def delete_notice(self, notice_id):
        self.DAO.delete_notice(notice_id)