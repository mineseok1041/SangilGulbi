import usersDAO
import usersDTO
import pointLogDTO

class usersSVC:
    def __init__(self):
        self.DAO = usersDAO.usersDAO()
        
    def getUsersInfo(self, reqDTO:usersDTO) -> usersDTO:
        try:
            return self.DAO.getUsersInfo(reqDTO)
        except Exception as e:
            raise Exception(f"getUsersInfo Error: {e}")
    
    def signup(self, reqDTO:usersDTO):
        if not self.DAO.isIDExist(reqDTO):
            try:
                self.DAO.addUsers(reqDTO)
            except Exception as e:
                raise Exception(e)
        else:
            raise Exception("ID already exists")
        
    def login(self, reqDTO:usersDTO) -> bool:
        try:
            if self.DAO.isIDExist(reqDTO):
                if self.DAO.isPWDCorrect(reqDTO):
                    return True
                else:
                    raise Exception("비밀번호가 일치하지 않습니다.")
            else:
                raise Exception("존재하지 않는 ID입니다.")
        except Exception as e:
            raise Exception(f"Login Error: {e}")
        
    def isIDExist(self, reqDTO:usersDTO) -> bool:
        try:
            if self.DAO.isIDExist(reqDTO):
                return True
            else:
                return False
        except Exception as e:
            raise Exception(f"isIDExist Error: {e}")

    # 프로필 사진 업데이트 함수
    def updateProfilePic(self, reqDTO:usersDTO):
        try:
            # 프로필 사진 업데이트
            self.DAO.updateProfilePic(reqDTO)
        except Exception as e:
            raise Exception(f"updateProfilePic Error: {e}")

    # 사용자 정보 업데이트 함수
    def updateUserInfo(self, reqDTO:usersDTO):
        try:
            # 사용자 정보 업데이트
            self.DAO.updateUserInfo(reqDTO)
        except Exception as e:
            raise Exception(f"updateUserInfo Error: {e}")
        
    def getStudentsList(self, page:int) -> list[usersDTO]:
        try:
            return self.DAO.getStudentsList(page)
        except Exception as e:
            raise Exception(f"getUsersList Error: {e}")
        
    def addPoint(self, stdDTO:usersDTO, managerDTO:usersDTO, point:int, reason: int):
        try:
            self.DAO.addPoint(stdDTO, point)
            self.DAO.addPointLog(stdDTO, managerDTO, point, reason)
            print("SVC success")
        except Exception as e:
            raise Exception(f"addPoint Error: {e}")
        
    def getManagersList(self, page:int):
        try:
            return self.DAO.getManagersList(page)
        except Exception as e:
            raise Exception(f"getManagersList Error: {e}")
        
    def delUsers(self, reqDTO: usersDTO):
        try:
            self.DAO.delUsers(reqDTO)
        except Exception as e:
            raise Exception(f"delUsers Error: {e}")
        
    def getPointLogByStdID(self, reqDTO: usersDTO):
        try:
            return self.DAO.getPointLogByStdID(reqDTO)
        except Exception as e:
            raise Exception(f"getPointLogByStdID Error: {e}")
