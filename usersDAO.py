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
                
    def addPointLog(self, stdDTO: usersDTO, managerDTO: usersDTO, point: int, reasonNum: int):
        query = "INSERT INTO pointLog(stdId, managerId, point, reason) VALUES(:1, :2, :3, :4)"
        
        conn = None
        cursor = None
        addReasons = {
            1: "솔선하여 휴지를 줍는 행위",
            2: "분실된 교구, 분실물을 습득하여 타의 모범이 된 학생",
            3: "솔선하여 청소를 하거나 복도 교실주변의 껌을 제거한 학생",
            4: "특별실 관리 및 학교 학급활동에 모범이 되어 담당교사의 추천을 받은 학생",
            5: "수업에서 교재 교구 기자재 관리 및 안전관리에 모범적인 행동을 한 학생",
            6: "학습 준비물을 철저히 준비하여 수업 보조도구로 활용되도록 한 학생",
            7: "방과 후 업무 보조 및 환경정화 활동을 적극적으로 한 학생",
            8: "방과 후 업무 보조 및 환경정화 활동을 적극적으로 한 학생",
            9: "학교의 명예를 높인 학생 (경중에 따라 상벌점 운영소위원회에서 심의 후 부여)",
            10: "학교의 명예를 높인 학생 (경중에 따라 상벌점 운영소위원회에서 심의 후 부여)",
            11: "학교의 명예를 높인 학생 (경중에 따라 상벌점 운영소위원회에서 심의 후 부여)",
            12: "선행 효행 단체활동 불우이웃돕기 일손 돕기 등의 봉사활동을 하여 공인된 외부 기관에서 모범표창을 받았거나 이와 상응한 경우"
        }
        delReasons = {
            1: "명찰 미착용",
            2: "교복 착용상태 불량 및 임의 변형",
            3: "미인정결석 및 미인정조퇴 행위",
            4: "미인정 지각 및 미인정결과 행위",
            5: "보행 중 음식물 취식 및 교실 반입 행위",
            6: "등·하굣길 통행 위반한 행위",
            7: "실내에서 소란스런 행동을 한 경우",
            8: "쓰레기 무단투기 및 껌과 가래침을 실내에서 뱉는 행위",
            9: "청소 활동에 참여하지 않은 경우",
            10: "SNS, 메신저 등을 이용하여 협박, 허위 사실 등을 유포하거나 타인 또는 학교의 명예를 훼손한 학생",
            11: "불온 문서(불법 동영상 등 포함)를 은닉, 탐독, 제작, 게시 또는 유포한 학생",
            12: "월담 행위",
            13: "학교 단체 행사에 무단 또는 고의적으로 참가하지 않는 경우",
            14: "수업시간 중에 무단으로 교문 출입행위",
            15: "위 항목 외 선도규정의 훈계에 해당한 경우",
            16: "수업 태도가 불령하거나, 면학 분위기를 저해하는 행위(수업 중 스마트폰 사용 등)",
            17: "학교 시설물 등에 낙서하거나 훼손하는 행위",
            18: "라이터, 담배 또는 흉기를 소지한 경우",
            19: "무단으로 현장실습 업체에서 이탈하거나 결근한 경우",
            20: "경고 행위 적발 시 타인의 이름을 도용하거나 도주한 경우",
            21: "교사의 정당한 지시에 따르지 않는 경우",
            22: "학교 내·외에서 음주 및 흡연을 하였거나, 증거가 확실한 경우",
            23: "몸의 일부에 문신을 한 경우",
            24: "규정위반으로 처벌 기간 중 미인정 결석 및 결과 한 경우 (횟수마다)"
        }
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            if point >= 0:
                print(stdDTO.id, managerDTO.id, point, addReasons[reasonNum])
                cursor.execute(query, [stdDTO.id, managerDTO.id, point, addReasons[reasonNum]])
            elif point < 0:
                print(stdDTO.id, managerDTO.id, point, delReasons[reasonNum])
                cursor.execute(query, [stdDTO.id, managerDTO.id, point, delReasons[reasonNum]])

            
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