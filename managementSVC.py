import usersDAO
from usersDTO import usersDTO

class managementSVC():
    def __init__(self):
        self.DAO = usersDAO.usersDAO()

    def getUsersList(self, page:int) -> list[usersDTO]:
        try:
            return self.DAO.getUsersList(page)
        except Exception as e:
            raise Exception(f"getUsersList Error: {e}")