from usersDTO import usersDTO
import cx_Oracle

class usersDAO:
    # 데이터베이스 연결 정보 설정
    def __init__(self):
        self.dsn = cx_Oracle.makedsn('localhost', 1521, service_name='xe')
        self.db_user = 'sangil'
        self.db_password = 'nobeesnohoney'

    # 데이터베이스 연결 생성
    def get_connection(self):
        return cx_Oracle.connect(self.db_user, self.db_password, self.dsn)

    def getUsersInfo(self, reqDTO: usersDTO) -> usersDTO:
        query = "SELECT * FROM users WHERE id = :1"
        
        conn = None
        cursor = None
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            cursor.execute(query, [reqDTO.id])
            row = cursor.fetchone()
            
            if row:
                return usersDTO(*row)
            else:
                return usersDTO(id=reqDTO.id, name='탈퇴한 사용자', stdNum='탈퇴한 사용자')
        # 데이터베이스 오류 발생 시 예외 처리    
        except cx_Oracle.DatabaseError as e:
            raise Exception(f"DB Error: {e}")
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def getStudentsList(self, page: int) -> list[usersDTO]:
        limit = 20 # 한 페이지에 보여줄 사용자 수
        startNo = (page - 1) * limit + 1
        endNo = page * limit

        query = "SELECT * FROM users WHERE no BETWEEN :startNo AND :endNo AND identity = 2"
        
        conn = None
        cursor = None
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            cursor.execute(query)
            rows = cursor.fetchall()
            
            result = []
            for row in rows:
                result.append(usersDTO(*row))
            
            return result
        except cx_Oracle.DatabaseError as e:
            raise Exception(f"DB Error: {e}")
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    
    def isIDExist(self, reqDTO: usersDTO) -> bool:
        query = "SELECT COUNT(*) FROM users WHERE id = :1"
        
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute(query, [reqDTO.id])
        count = cursor.fetchone()[0]
        
        cursor.close()
        conn.close()
        
        return count > 0

    def isPWDCorrect(self, reqDTO: usersDTO) -> bool:
        query = "SELECT COUNT(*) FROM users WHERE id = :1 AND password = :2"

        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute(query, [reqDTO.id, reqDTO.password])
        count = cursor.fetchone()[0]
        
        cursor.close()
        conn.close()
        
        return count > 0

    def addUsers(self, reqDTO: usersDTO):
        conn = None
        cursor = None
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            if reqDTO.identity == 2:  # 학생
                query = "INSERT INTO users(id, password, name, stdNum, identity, verified) VALUES(:1, :2, :3, :4, :5, 1)"
                cursor.execute(query, [reqDTO.id, reqDTO.password, reqDTO.name, reqDTO.stdNum, reqDTO.identity])
            elif reqDTO.identity == 1:  # 선생님
                query = "INSERT INTO users(id, password, name, identity, verified, checkCode) VALUES(:1, :2, :3, :4, 0, :5)"
                cursor.execute(query, [reqDTO.id, reqDTO.password, reqDTO.name, reqDTO.identity, reqDTO.checkCode])

            conn.commit()
        except cx_Oracle.DatabaseError as e:
            raise Exception(f"DB Error: {e}")
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def delUsers(self, reqDTO: usersDTO):
        query = "DELETE FROM users WHERE id = :1"
        
        conn = None
        cursor = None
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            cursor.execute(query, [reqDTO.id])
            
            conn.commit()
        except cx_Oracle.DatabaseError as e:
            raise Exception(f"DB Error: {e}")
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    # 학번 수정
    def altStdNum(self, reqDTO: usersDTO):
        # 학년이 1, 2, 3 중 하나인지 확인
        if reqDTO.currentgrade not in [1, 2, 3]:
            raise ValueError(f"Invalid grade: {reqDTO.currentgrade}. Must be 1, 2, or 3.")
        # 학번 수정 쿼리
        query = "UPDATE users SET currentgrade = :1, currentclass = :2, currentnum = :3 WHERE id = :4"
        
        conn = None
        cursor = None
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            # 학번 수정 쿼리 실행
            cursor.execute(query, [reqDTO.currentgrade, reqDTO.currentclass, reqDTO.currentnum, reqDTO.id])
            
            conn.commit()
        except cx_Oracle.DatabaseError as e:
            raise Exception(f"DB Error: {e}")
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    # 사용자 정보 업데이트
    def updateUserInfo(self, reqDTO: usersDTO):
        # 사용자 정보 업데이트 쿼리
        query = "UPDATE users SET currentgrade = :1, currentclass = :2, currentnum = :3, name = :4, phone = :5, email = :6 WHERE id = :7"
        
        conn = None
        cursor = None
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            # 사용자 정보 업데이트 쿼리 실행
            cursor.execute(query, [reqDTO.currentgrade, reqDTO.currentclass, reqDTO.currentnum, reqDTO.name, reqDTO.phone, reqDTO.email, reqDTO.id])
            
            conn.commit()
        except cx_Oracle.DatabaseError as e:
            raise Exception(f"DB Error: {e}")
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
                
    # 마지막 로그인 시간 업데이트
    def updateLastLogin(self, reqDTO: usersDTO):
        conn = self.get_connection()
        cursor = conn.cursor()
        try:
            query = "UPDATE users SET lastlogindate = TO_CHAR(SYSDATE, 'YYYY/MM/DD') WHERE id = :1"
            cursor.execute(query, [reqDTO.id])
            query = "UPDATE users SET lastlogintime = TO_CHAR(SYSDATE, 'HH24:MI:SS') WHERE id = :1"
            cursor.execute(query, [reqDTO.id])

            conn.commit()
        except cx_Oracle.DatabaseError as e:
            print(f"Database error: {e}")
        finally:
            cursor.close()
            conn.close()

    def isVerified(self, reqDTO: usersDTO) -> bool:
        query = "SELECT COUNT(*) FROM users WHERE id = :1 AND verified = 1"
        
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute(query, [reqDTO.id])
        count = cursor.fetchone()[0]
        
        cursor.close()
        conn.close()
        
        print(count)
        return count > 0
    
    def updatePassword(self, userId: str, newPassword: str):
        query = "UPDATE users SET password = :1 WHERE id = :2"
        conn = self.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(query, [newPassword, userId])
            conn.commit()
        except Exception as e:
            raise Exception(f"비밀번호 변경 실패: {e}")
        finally:
            cursor.close()
            conn.close()
            
    def getTeachersList(self, page: int) -> list[usersDTO]:
        limit = 20
        startNo = (page - 1) * limit + 1
        endNo = page * limit
        
        # 승인된(verified=1) 선생님만 조회
        query = "SELECT * FROM users WHERE no BETWEEN :startNo AND :endNo AND identity = 1 AND verified = 1"
        
        conn = None
        cursor = None
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            cursor.execute(query, [startNo, endNo])
            rows = cursor.fetchall()
            return [usersDTO(*row) for row in rows]
        except cx_Oracle.DatabaseError as e:
            raise Exception(f"DB Error: {e}")
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
            
    def getUnverifiedTeachers(self) -> list[usersDTO]:
        query = "SELECT * FROM users WHERE identity = 1 AND verified = 0"
        
        conn = None
        cursor = None
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            cursor.execute(query)
            rows = cursor.fetchall()
            
            unverified_teachers = [usersDTO(*row) for row in rows]
            return unverified_teachers
        except cx_Oracle.DatabaseError as e:
            raise Exception(f"Database Error in getUnverifiedTeachers: {e}")
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
            
    def updateTeacherVerified(self, teacher_id: str, verified: int):
        query = "UPDATE users SET verified = :1 WHERE id = :2"
        conn = None
        cursor = None
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            cursor.execute(query, [verified, teacher_id])
            conn.commit()
        except cx_Oracle.DatabaseError as e:
            raise Exception(f"Database Error: {e}")
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def searchStudentsByKeyword(self, keyword: str) -> list[usersDTO]:
        query = """
            SELECT * FROM users
            WHERE identity = 2 AND (name LIKE :kw OR stdNum LIKE :kw)
        """
        conn = self.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(query, {'kw': f'%{keyword}%'})
            rows = cursor.fetchall()
            return [usersDTO(*row) for row in rows]
        finally:
            cursor.close()
            conn.close()

    def searchTeachersByKeyword(self, keyword: str) -> list[usersDTO]:
        query = """
            SELECT * FROM users
            WHERE identity = 1 AND verified = 1 AND (name LIKE :kw OR id LIKE :kw)
        """
        conn = self.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(query, {'kw': f'%{keyword}%'})
            rows = cursor.fetchall()
            return [usersDTO(*row) for row in rows]
        finally:
            cursor.close()
            conn.close()
