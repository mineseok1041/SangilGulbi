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
                    user_info = self.usersDAO.getUsersInfo(reqDTO)
                    if user_info.identity in [0, 1] and not self.usersDAO.isVerified(reqDTO):   # 선생님(1) 또는 관리자(0)일 때 승인 여부 체크
                        raise Exception("관리자의 승인이 필요합니다.")
                    self.usersDAO.updateLastLogin(reqDTO)
                    return True
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
            raise Exception(f"getStudentsList Error: {e}")

    def getTeachersList(self, page: int) -> list[usersDTO]: # type: ignore
        try:
            return self.usersDAO.getTeachersList(page)
        except Exception as e:
            raise Exception(f"getTeachersList Error: {e}")

    def delUsers(self, reqDTO: usersDTO):
        try:
            self.usersDAO.delUsers(reqDTO)
        except Exception as e:
            raise Exception(f"delUsers Error: {e}")
        
    def getUnverifiedTeachers(self) -> list[usersDTO]: # type: ignore
        try:
            return self.usersDAO.getUnverifiedTeachers()
        except Exception as e:
            raise Exception(f"getUnverifiedTeachers Error: {e}")
    
    def searchStudentsByKeyword(self, keyword: str) -> list[usersDTO]:  # type: ignore
        try:
            return self.usersDAO.searchStudentsByKeyword(keyword)
        except Exception as e:
            raise Exception(f"searchStudentsByKeyword Error: {e}")

    def searchTeachersByKeyword(self, keyword: str) -> list[usersDTO]:  # type: ignore
        try:
            return self.usersDAO.searchTeachersByKeyword(keyword)
        except Exception as e:
            raise Exception(f"searchTeachersByKeyword Error: {e}")
        
    def changePassword(self, beforeDTO: usersDTO, newPassword: str, newPasswordCheck: str):
        try:
            if newPassword != newPasswordCheck:
                raise Exception("새 비밀번호와 확인 비밀번호가 일치하지 않습니다.")
            
            if not self.usersDAO.isPWDCorrect(beforeDTO):
                raise Exception("현재 비밀번호가 일치하지 않습니다.")
            
            self.usersDAO.updatePassword(beforeDTO.id, newPassword)
        except Exception as e:
            raise Exception(f"{e}")

