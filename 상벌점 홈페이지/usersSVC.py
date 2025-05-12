import usersDAO
import usersDTO
import pointLogDTO

class usersSVC:
    def __init__(self):
        self.usersDAO = usersDAO.usersDAO()
        
    def getUsersInfo(self, reqDTO:usersDTO) -> usersDTO:
        try:
            return self.usersDAO.getUsersInfo(reqDTO)
        except Exception as e:
            raise Exception(f"getUsersInfo Error: {e}")
    
    def signup(self, reqDTO:usersDTO):
        try:
            if self.usersDAO.isIDExist(reqDTO):
                raise Exception("ID already exists")
            else:
                self.usersDAO.addUsers(reqDTO)
        except Exception as e:
            raise Exception(e)
        
    def login(self, reqDTO:usersDTO) -> bool:
        try:
            if self.usersDAO.isIDExist(reqDTO):
                if self.usersDAO.isPWDCorrect(reqDTO):
                    if self.usersDAO.isVerified(reqDTO):
                        self.usersDAO.updateLastLogin(reqDTO)  # 마지막 로그인 시간 업데이트
                        return True
                    else:
                        raise Exception("관리자의 승인이 필요합니다.")
                else:
                    raise Exception("비밀번호가 일치하지 않습니다.")
            else:
                raise Exception("존재하지 않는 ID입니다.")
        except Exception as e:
            raise Exception(f"{e}")
        
    def isIDExist(self, reqDTO:usersDTO) -> bool:
        try:
            if self.usersDAO.isIDExist(reqDTO):
                return True
            else:
                return False
        except Exception as e:
            raise Exception(f"isIDExist Error: {e}")

    # 사용자 정보 업데이트 함수
    def updateUserInfo(self, reqDTO:usersDTO):
        try:
            # 사용자 정보 업데이트
            self.usersDAO.updateUserInfo(reqDTO)
        except Exception as e:
            raise Exception(f"updateUserInfo Error: {e}")
        
    def getStudentsList(self, page:int) -> list[usersDTO]: # type: ignore
        try:
            return self.usersDAO.getStudentsList(page)
        except Exception as e:
            raise Exception(f"getUsersList Error: {e}")
    
    def getTeachersList(self, page:int) -> list[usersDTO]: # type: ignore
        try:
            return self.usersDAO.getTeachersList(page)
        except Exception as e:
            raise Exception(f"getUsersList Error: {e}")
    
    def delUsers(self, reqDTO: usersDTO):
        try:
            self.DAO.delUsers(reqDTO)
        except Exception as e:
            raise Exception(f"delUsers Error: {e}")
