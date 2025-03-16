from usersDTO import usersDTO
import cx_Oracle

class usersDAO:
    # 데이터베이스 연결 정보 설정
    def __init__(self):
        self.dsn = cx_Oracle.makedsn('localhost', 1521, service_name='xe')
        self.db_user = 'sangil'
        self.db_password = '1234'

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
                raise ValueError(f"ID {reqDTO.id} not found")
        # 데이터베이스 오류 발생 시 예외 처리    
        except cx_Oracle.DatabaseError as e:
            raise Exception(f"DB Error: {e}")
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def getStudentsList(self, page: int) -> list[usersDTO]:
        limit = 50 # 한 페이지에 보여줄 사용자 수
        startNo = (page - 1) * limit + 1
        endNo = page * limit

        query = "SELECT * FROM users WHERE no BETWEEN :startNo AND :endNo AND identity = 2"
        
        conn = None
        cursor = None
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            cursor.execute(query, {'startNo': startNo, 'endNo': endNo})
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

    def getManagersList(self, page: int) -> list[usersDTO]:
        limit = 50 # 한 페이지에 보여줄 관리자 수
        startNo = (page - 1) * limit + 1
        endNo = page * limit

        query = "SELECT * FROM users WHERE no BETWEEN :startNo AND :endNo AND identity IN (0, 1)"
        
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
        query = "INSERT INTO users(id, password, name, email, birth) VALUES(:1, :2, :3, :4, :5)"
        
        conn = None
        cursor = None
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            cursor.execute(query, [reqDTO.id, reqDTO.password, reqDTO.name, reqDTO.email, reqDTO.birth])
            
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
    # 포인트 추가
    def addPoint(self, reqDTO: usersDTO, point: int):
        # 포인트 추가 쿼리
        query = "UPDATE users SET point = point + :1 WHERE id = :2"
        
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

    # 프로필 사진 업데이트
    def updateProfilePic(self, reqDTO: usersDTO):
        # 프로필 사진 업데이트 쿼리
        query = "UPDATE users SET profile_pic = :1 WHERE id = :2"
        
        conn = None
        cursor = None
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            # 프로필 사진 업데이트 쿼리 실행
            cursor.execute(query, [reqDTO.profile_pic, reqDTO.id])
            
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
    def updateLastLogin(self, user_id: str):
        query = "UPDATE users SET lastlogin = TO_CHAR(SYSDATE, 'YYYYMMDD HH24:MI:SS') WHERE id = :1"
        conn = self.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(query, [user_id])
            conn.commit()
        except cx_Oracle.DatabaseError as e:
            print(f"Database error: {e}")
        finally:
            cursor.close()
            conn.close()