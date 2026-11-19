from DAO.StudentDao import StudentDao
from Model.Student import student

class StudentService:
    def __init__(self):
        self.dao = StudentDao()

    def save_std(self,student):
        if student.name.strip() == "":
            print("Name can not be empty")
            return
        if student.roll_no < 0:
            print("Roll no must be positive")
            return
        if student.age < 0:
            print("Student age must be positive")
            return
        if student.age > 100:
            print("Invalid Student age")
            return
        if student.marks > 100 or student.marks < 0:
            print("Invalid Student marks")
            return
        self.dao.add_std(student)

    def display(self):
        std = self.dao.get_std()
        if len(std) == 0:
            print("No student found")
            return
        for student in std:
            print("Student Roll no: ",student.roll_no)
            print("Student Name: ",student.name)
            print("Student Age: ",student.age)
            print("Student Marks: ",student.marks)
            print("================================")

    def dis_name(self,name):
        if name.strip() == "":
            print("Name can not be empty")
            return
        student = self.dao.std_name(name)
        if student is not None:
            print("Student Roll no: ",student.roll_no)
            print("Student Name: ",student.name)
            print("Student Age: ",student.age)
            print("Student Marks: ",student.marks)
        else:
            print("Student Not found")

    def delete_std(self,name):
        affectedrows = self.dao.delete_std(name)
        if affectedrows > 0:
            print("Student record deleted successfully")
        else:
            print("Student not found")

    def update(self,student):
        affectedrows = self.dao.update(student)
        if affectedrows > 0:
            print("Student record updated successfully")
        else:
            print("Student not found")
    
