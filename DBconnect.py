import cx_Oracle
from studentDTO import studentDTO

conn = cx_Oracle.connect('sangil/1234@localhost:1521/xe')
cursor = conn.cursor()

oldone = studentDTO(id='test1')

query = "select * from student where id = :0"
cursor.execute(query, [oldone.id])
row = cursor.fetchone()
newone = studentDTO(*row)

print(row)
print(newone)

cursor.close()
conn.close()
