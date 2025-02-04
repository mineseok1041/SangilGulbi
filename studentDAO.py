from studentDTO import studentDTO
import cx_Oracle

class studentDAO:
    def __init__(self):
        self.dsn = cx_Oracle.makedsn('localhost', 1521, service_name='xe')
        self.db_user = 'sangil'
        self.db_password = '1234'

    def get_connection(self):
        return cx_Oracle.connect(self.db_user, self.db_password, self.dsn)

    def getStudentInfo(self, reqDTO: studentDTO) -> studentDTO:
        query = "SELECT * FROM student WHERE id = :1"
        
        conn = None
        cursor = None
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            cursor.execute(query, [reqDTO.id])
            row = cursor.fetchone()
            
            if row:
                return studentDTO(*row)
            else:
                raise ValueError(f"ID {reqDTO.id} not found")
        except cx_Oracle.DatabaseError as e:
            raise Exception(f"DB Error: {e}")
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def getStudentList(self) -> list[studentDTO]:
        query = "SELECT * FROM student"
        
        conn = None
        cursor = None
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            cursor.execute(query)
            rows = cursor.fetchall()
            
            result = []
            for row in rows:
                result.append(studentDTO(*row))
            
            return result
        except cx_Oracle.DatabaseError as e:
            raise Exception(f"DB Error: {e}")
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def isIDExist(self, reqDTO: studentDTO) -> bool:
        query = "SELECT COUNT(*) FROM student WHERE id = :1"
        
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute(query, [reqDTO.id])
        count = cursor.fetchone()[0]
        
        cursor.close()
        conn.close()
        
        return count > 0

    def isPWDCorrect(self, reqDTO: studentDTO) -> bool:
        query = "SELECT COUNT(*) FROM student WHERE id = :1 AND password = :2"
        
        conn = None
        cursor = None
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            cursor.execute(query, [reqDTO.id, reqDTO.password])
            count = cursor.fetchone()[0]
            
            return count > 0
        except cx_Oracle.DatabaseError as e:
            raise Exception(f"DB Error: {e}")
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def addStudent(self, reqDTO: studentDTO):
        query = "INSERT INTO student(id, password, name, email, birth) VALUES(:1, :2, :3, :4, :5)"
        
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

    def delStudent(self, reqDTO: studentDTO):
        query = "DELETE FROM student WHERE id = :1"
        
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

    def altStdNum(self, reqDTO: studentDTO):
        if reqDTO.currentgrade not in [1, 2, 3]:
            raise ValueError(f"Invalid grade: {reqDTO.currentgrade}. Must be 1, 2, or 3.")

        query = "UPDATE student SET currentgrade = :1, currentclass = :2, currentnum = :3 WHERE id = :4"
        
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

    def addPoint(self, reqDTO: studentDTO, point: int):
        query = "UPDATE student SET point = point + :1 WHERE id = :2"
        
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
