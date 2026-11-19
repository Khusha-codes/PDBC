from Database.connection import database
from Model.Student import student

db = database()
connection = db.connect()
cursor = connection.cursor()

class StudentDao():
    def __init__(self):
        db = database()
        self.connection = db.connect()
        self.cursor = self.connection.cursor()

    def add_std(self,student):
        query = "insert into student2(roll_no,name,age,marks) values(%s,%s,%s,%s)"
        value = (student.roll_no,student.name,student.age,student.marks)
        self.cursor.execute(query,value)
        self.connection.commit()
        print("Student Details Add Successfully")
        self.end()

    def get_std(self):
        query = "Select * from student2"
        self.cursor.execute(query)
        students = []
        self.end()
        for row in self.cursor:
            std = student(row[0],row[1],row[2],row[3])
            students.append(std)
        return students


    def std_name(self,name):
        query = "Select * from student2 where name = %s"
        self.cursor.execute(query,(name,))
        row = self.cursor.fetchone()
        self.end()
        if row is not None:
            std = student(row[0],row[1],row[2],row[3])
            return std
        return None

    def delete_std(self,name):
        query = "delete from student2 where name = %s"
        self.cursor.execute(query,(name,))
        self.connection.commit()
        self.end()
        affectedrow = self.cursor.rowcount
        return affectedrow

    def update(self,student):
        query = "update student2 set marks = %s where roll_no = %s"
        values = (student.marks,student.roll_no)
        self.cursor.execute(query,values)
        self.connection.commit()
        self.end()
        affectedrow = self.cursor.rowcount
        return affectedrow

    def end(self):
        self.cursor.close()
        self.connection.close()

