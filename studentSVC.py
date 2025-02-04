import studentDAO
import studentDTO

class studentSVC:
    def __init__(self):
        self.DAO = studentDAO.studentDAO()
    
    def signup(self, reqDTO:studentDTO):
        if not self.DAO.isIDExist(reqDTO):
            try:
                self.DAO.addStudent(reqDTO)
            except Exception as e:
                raise Exception(f"Signup Error: {e}")
        else:
            raise Exception("ID already exists")