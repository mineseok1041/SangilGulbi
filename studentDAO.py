from studentDTO import studentDTO

class studentDAO:
    def __init__:
        conn = cx_Oracle.connect('sangil/1234@localhost:1521/xe')
        cursor = conn.cursor()
        
    def getStudentInfo(studentDTO: studentDTO):
        query = "select * from student where id = :0"
        cursor.execute(query, [studentDTO.id])
        row = cursor.fetchone()
        result = studentDTO(*row)
        return result
        
    def addStudent(studentDTO: studentDTO):
        query = "insert into student(id, password, name) values(:0, :1, :2)"
        cursor.execute(query, [studentDTO.id, studentDTO.password, studentDTO.name])
        conn.commit()
    
    def delStudent(studentDTO: studentDTO):
        query = "delete from student where id = :0"
        cursor.execute(query, [studentDTO.id])
        conn.commit()
    
    def altStdNum(studentDTO: studentDTO):
        query = "update student set (currentgrade, currentclass, currentnum) = (:0, :1, :2) where id = :3"
        cursor.execute(query, [studentDTO.currentgrade, studentDTO.currentclass, studentDTO.currentnum, studentDTO.id])
        conn.commit()
    
    def addPoint(studentDTO: studentDTO, point: int):
        query = "update student set point = point + :0 where id = :1"
        cursor.execute(query, [point, studentDTO.id])
        conn.commit()
        
    def __del__:
        cursor.close()
        conn.close()