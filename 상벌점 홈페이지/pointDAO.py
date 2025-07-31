import cx_Oracle
from typing import Literal
from usersDTO import usersDTO
from pointLogDTO import pointLogDTO
from pointReasonDTO import pointReasonDTO

class pointDAO:
    def __init__(self):
        self.dsn = cx_Oracle.makedsn('localhost', 1521, service_name='xe')
        self.db_user = 'sangil'
        self.db_password = 'nobeesnohoney'

    # 데이터베이스 연결 생성
    def get_connection(self):
        return cx_Oracle.connect(self.db_user, self.db_password, self.dsn)
    
    # 포인트 추가
    def addPoint(self, reqDTO: usersDTO, point: int):
        # 포인트 추가 쿼리
        query = "UPDATE users SET addpoint = addpoint + :1 WHERE id = :2"
        
        conn = None
        cursor = None
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            # 포인트 추가 쿼리 실행
            cursor.execute(query, [point, reqDTO.id])
            
            conn.commit()
        except cx_Oracle.DatabaseError as e: 
            raise Exception(f"DB Error: {e}")
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def delPoint(self, reqDTO: usersDTO, point: int):
        # 포인트 추가 쿼리
        query = "UPDATE users SET delpoint = delpoint + :1 WHERE id = :2"
        
        conn = None
        cursor = None
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            # 포인트 추가 쿼리 실행
            cursor.execute(query, [point, reqDTO.id])
            
            conn.commit()
        except cx_Oracle.DatabaseError as e: 
            raise Exception(f"DB Error: {e}")
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def getPointReason(self, type: Literal['bonus', 'penalty']) -> list[pointReasonDTO]:
        query = "SELECT * FROM pointReason WHERE type = :1"

        conn = None
        cursor = None
        try:
            conn = self.get_connection()
            cursor = conn.cursor()

            cursor.execute(query, [type])

            results = cursor.fetchall()

            return [pointReasonDTO(*row) for row in results]
        except cx_Oracle.DatabaseError as e:
            raise Exception(f"DB Error: {e}")
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def recordPointLog(self, type: Literal['bonus', 'penalty'], stdDTO: usersDTO, writeTeacherDTO: usersDTO, giveTeacherDTO, point: int, reason: str, opinion: str):
        query = "INSERT INTO pointLog(type, studentId, studentNum, studentName, writeTeacherId, writeTeacherName, giveTeacherId, giveTeacherName, point, reason, opinion) VALUES(:1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11)"
        
        conn = None
        cursor = None
        
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            cursor.execute(query, [type, stdDTO.id, stdDTO.stdNum, stdDTO.name, writeTeacherDTO.id, writeTeacherDTO.name, giveTeacherDTO.id, giveTeacherDTO.name, point, reason, opinion])
            
            conn.commit()
        except cx_Oracle.DatabaseError as e:
            raise Exception(f"DB Error: {e}")
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
    
    def getPointLog(self, page: int, type: Literal['all', 'bonus', 'penalty']) -> list[pointLogDTO]:
        limit = 20
        startNo = (page - 1) * limit + 1
        endNo = page * limit

        query = """
                SELECT *
                FROM (
                    SELECT a.*, ROWNUM AS rn
                    FROM (
                        SELECT * FROM pointLog ORDER BY no DESC
                    ) a
                    WHERE ROWNUM <= :endNo
                )
                WHERE rn >= :startNo
            """

        conn = None
        cursor = None
        try:
            conn = self.get_connection()
            cursor = conn.cursor()

            cursor.execute(query, {'startNo': startNo, 'endNo': endNo})
            results = cursor.fetchall()
            
            return [pointLogDTO(*row[:-1]) for row in results]
        except cx_Oracle.DatabaseError as e:
            raise Exception(f"DB Error: {e}")
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
    
    def getPointLogByStdID(self, usersDTO: usersDTO, page: int, type: Literal['all', 'bonus', 'penalty']) -> list[pointLogDTO]:
        stdID = usersDTO.id
        limit = 20
        startNo = (page - 1) * limit + 1
        endNo = page * limit

        query = """
                SELECT *
                FROM (
                    SELECT a.*, ROWNUM AS rn
                    FROM (
                        SELECT * FROM pointLog WHERE studentId = :stdID ORDER BY no DESC
                    ) a
                    WHERE ROWNUM <= :endNo
                )
                WHERE rn >= :startNo
            """
        
        conn = None
        cursor = None

        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            cursor.execute(query, {'stdID': stdID, 'startNo': startNo, 'endNo': endNo})
            results = cursor.fetchall()

            return [pointLogDTO(*row[:-1]) for row in results]
        
        except cx_Oracle.DatabaseError as e:
            raise Exception(f"DB Error: {e}")
        
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def getPointLogByTeacherID(self, usersDTO: usersDTO, page: int, type: Literal['all', 'bonus', 'penalty']) -> list[pointLogDTO]:
        limit = 20
        startNo = (page - 1) * limit + 1
        endNo = page * limit

        query = """
                SELECT *
                FROM (
                    SELECT a.*, ROWNUM AS rn
                    FROM (
                        SELECT * FROM pointLog WHERE giveTeacherId = :teacherID ORDER BY no DESC
                    ) a
                    WHERE ROWNUM <= :endNo
                )
                WHERE rn >= :startNo
            """        
        conn = None
        cursor = None

        try:
            teacherID = usersDTO.id
            # if type == 'bonus':
            #     query += " AND type = 'bonus'"
            # elif type == 'penalty':
            #     query += " AND type = 'penalty'"
            # query += " ORDER BY no DESC"

            conn = self.get_connection()
            cursor = conn.cursor()
            
            cursor.execute(query, {'teacherID': teacherID, 'startNo': startNo, 'endNo': endNo})
            results = cursor.fetchall()

            return [pointLogDTO(*row[:-1]) for row in results]
        
        except cx_Oracle.DatabaseError as e:
            raise Exception(f"DB Error: {e}")
        
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def getPointLogByNo(self, logNo: int) -> pointLogDTO:
        query = "SELECT * FROM pointLog WHERE no = :1"

        conn = None
        cursor = None
        try:
            conn = self.get_connection()
            cursor = conn.cursor()

            cursor.execute(query, [logNo])
            row = cursor.fetchone()

            if row:
                return pointLogDTO(*row)
            else:
                raise Exception("로그를 찾을 수 없습니다.")
        except cx_Oracle.DatabaseError as e:
            raise Exception(f"DB Error: {e}")
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def getTeacherPointLogMaxPage(self, teacherDTO) -> int:
        query = "SELECT CEIL(COUNT(*) / 20) FROM pointLog WHERE giveTeacherId = :1"

        conn = None
        cursor = None
        try:
            conn = self.get_connection()
            cursor = conn.cursor()

            cursor.execute(query, [teacherDTO.id])
            max_page = cursor.fetchone()[0]

            return int(max_page) if max_page else 1
        except cx_Oracle.DatabaseError as e:
            raise Exception(f"DB Error: {e}")
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
    
    def getStudentPointLogMaxPage(self, studentDTO) -> int:
        query = "SELECT CEIL(COUNT(*) / 20) FROM pointLog WHERE studentId = :1"

        conn = None
        cursor = None
        try:
            conn = self.get_connection()
            cursor = conn.cursor()

            cursor.execute(query, [studentDTO.id])
            max_page = cursor.fetchone()[0]

            return int(max_page) if max_page else 1
        except cx_Oracle.DatabaseError as e:
            raise Exception(f"DB Error: {e}")
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def getPointLogMaxPage(self) -> int:
        query = "SELECT CEIL(COUNT(*) / 20) FROM pointLog"

        conn = None
        cursor = None
        try:
            conn = self.get_connection()
            cursor = conn.cursor()

            cursor.execute(query)
            max_page = cursor.fetchone()[0]

            return int(max_page) if max_page else 1
        except cx_Oracle.DatabaseError as e:
            raise Exception(f"DB Error: {e}")
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def deletePointLog(self, logNo: int):
        query = "DELETE FROM pointLog WHERE no = :1"

        conn = None
        cursor = None
        try:
            conn = self.get_connection()

            cursor = conn.cursor()
            cursor.execute(query, [logNo])

            conn.commit()
        except cx_Oracle.DatabaseError as e:
            raise Exception(f"DB Error: {e}")
        finally:
            cursor.close()
            conn.close()
