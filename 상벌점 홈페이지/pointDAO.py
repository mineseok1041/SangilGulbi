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
    
    def getPointLog(self, page: int) -> list[pointLogDTO]:
        limit = 30
        startNo = (page - 1) * limit + 1
        endNo = page * limit

        query = "SELECT * FROM pointLog WHERE no BETWEEN :startNo AND :endNo ORDER BY no DESC"

        conn = None
        cursor = None
        try:
            conn = self.get_connection()
            cursor = conn.cursor()

            cursor.execute(query, [startNo, endNo])
            results = cursor.fetchall()
            
            return [pointLogDTO(*row) for row in results]
        except cx_Oracle.DatabaseError as e:
            raise Exception(f"DB Error: {e}")
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
    
    def getPointLogByStdID(self, usersDTO: usersDTO) -> list[pointLogDTO]:
        stdID = usersDTO.id
        query = "SELECT * FROM pointLog WHERE studentId = :1"
        
        conn = None
        cursor = None

        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            cursor.execute(query, [stdID])
            results = cursor.fetchall()

            return [pointLogDTO(*row) for row in results]
        
        except cx_Oracle.DatabaseError as e:
            raise Exception(f"DB Error: {e}")
        
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def getPointLogByTeacherID(self, usersDTO: usersDTO, type: Literal['all', 'bonus', 'penalty']) -> list[pointLogDTO]:
        query = "SELECT * FROM pointLog WHERE giveTeacherId = :1"
        
        conn = None
        cursor = None

        try:
            teacherID = usersDTO.id
            if type == 'bonus':
                query += " AND type = 'bonus'"
            elif type == 'penalty':
                query += " AND type = 'penalty'"

            conn = self.get_connection()
            cursor = conn.cursor()
            
            cursor.execute(query, [teacherID])
            results = cursor.fetchall()

            return [pointLogDTO(*row) for row in results]
        
        except cx_Oracle.DatabaseError as e:
            raise Exception(f"DB Error: {e}")
        
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
