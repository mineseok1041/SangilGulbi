from usersDTO import usersDTO
import cx_Oracle

class usersDAO:
    def __init__(self):
        self.dsn = cx_Oracle.makedsn('localhost', 1521, service_name='xe')
        self.db_user = 'sangil'
        self.db_password = '1234'

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
        except cx_Oracle.DatabaseError as e:
            raise Exception(f"DB Error: {e}")
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def getUsersList(self) -> list[usersDTO]:
        query = "SELECT * FROM users"
        
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

    def altStdNum(self, reqDTO: usersDTO):
        if reqDTO.currentgrade not in [1, 2, 3]:
            raise ValueError(f"Invalid grade: {reqDTO.currentgrade}. Must be 1, 2, or 3.")

        query = "UPDATE users SET currentgrade = :1, currentclass = :2, currentnum = :3 WHERE id = :4"
        
        conn = None
        cursor = None
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            cursor.execute(query, [reqDTO.currentgrade, reqDTO.currentclass, reqDTO.currentnum, reqDTO.id])
            
            conn.commit()
        except cx_Oracle.DatabaseError as e:
            raise Exception(f"DB Error: {e}")
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def addPoint(self, reqDTO: usersDTO, point: int):
        query = "UPDATE users SET point = point + :1 WHERE id = :2"
        
        conn = None
        cursor = None
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            cursor.execute(query, [point, reqDTO.id])
            
            conn.commit()
        except cx_Oracle.DatabaseError as e:
            raise Exception(f"DB Error: {e}")
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def updateProfilePic(self, reqDTO: usersDTO):
        query = "UPDATE users SET profile_pic = :1 WHERE id = :2"
        
        conn = None
        cursor = None
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            cursor.execute(query, [reqDTO.profile_pic, reqDTO.id])
            
            conn.commit()
        except cx_Oracle.DatabaseError as e:
            raise Exception(f"DB Error: {e}")
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def updateUserInfo(self, reqDTO: usersDTO):
        query = "UPDATE users SET currentgrade = :1, currentclass = :2, currentnum = :3, name = :4, phone = :5, email = :6 WHERE id = :7"
        
        conn = None
        cursor = None
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            cursor.execute(query, [reqDTO.currentgrade, reqDTO.currentclass, reqDTO.currentnum, reqDTO.name, reqDTO.phone, reqDTO.email, reqDTO.id])
            
            conn.commit()
        except cx_Oracle.DatabaseError as e:
            raise Exception(f"DB Error: {e}")
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()