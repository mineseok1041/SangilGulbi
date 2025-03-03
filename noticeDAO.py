from noticeDTO import NoticeDTO
import cx_Oracle

class NoticeDAO:
    def __init__(self):
        self.dsn = cx_Oracle.makedsn('localhost', 1521, service_name='xe')
        self.db_user = 'sangil'
        self.db_password = '1234'

    def get_connection(self):
        return cx_Oracle.connect(self.db_user, self.db_password, self.dsn)

    def get_all_notices(self) -> list[NoticeDTO]:
        query = "SELECT * FROM notice ORDER BY created_date DESC"
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        notices = [NoticeDTO(*row) for row in rows]
        cursor.close()
        conn.close()
        return notices

    def get_notice_by_id(self, notice_id: int) -> NoticeDTO:
        query = "SELECT * FROM notice WHERE id = :1"
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute(query, [notice_id])
        row = cursor.fetchone()
        if row:
            notice = NoticeDTO(*row)
            if isinstance(notice.content, cx_Oracle.LOB):
                notice.content = notice.content.read()  # LOB 데이터를 읽어옴
        else:
            notice = None
        cursor.close()
        conn.close()
        return notice

    def add_notice(self, notice: NoticeDTO):
        query = "INSERT INTO notice (id, title, content, author) VALUES (seq_notice_id.NEXTVAL, :1, :2, :3)"
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute(query, [notice.title, notice.content, notice.author])
        conn.commit()
        cursor.close()
        conn.close()

    def update_notice(self, notice: NoticeDTO):
        query = "UPDATE notice SET title = :1, content = :2, updated_date = TO_CHAR(SYSDATE, 'YYYYMMDD HH24:MI:SS') WHERE id = :3"
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute(query, [notice.title, notice.content, notice.id])
        conn.commit()
        cursor.close()
        conn.close()

    def delete_notice(self, notice_id: int):
        query = "DELETE FROM notice WHERE id = :1"
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute(query, [notice_id])
        conn.commit()
        cursor.close()
        conn.close()