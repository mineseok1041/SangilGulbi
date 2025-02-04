import studentDAO
import studentDTO

class studentSVC:
    def __init__(self):
        self.DAO = studentDAO.studentDAO()
        
    def getStudentInfo(self, reqDTO:studentDTO) -> studentDTO:
        try:
            return self.DAO.getStudentInfo(reqDTO)
        except Exception as e:
            raise Exception(f"getStudentInfo Error: {e}")
    
    def signup(self, reqDTO:studentDTO):
        if not self.DAO.isIDExist(reqDTO):
            try:
                self.DAO.addStudent(reqDTO)
            except Exception as e:
                raise Exception(e)
        else:
            raise Exception("ID already exists")
        
    def login(self, reqDTO:studentDTO) -> bool:
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