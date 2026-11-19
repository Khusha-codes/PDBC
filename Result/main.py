from Service.StudentService import StudentService
from Model.Student import student
call = StudentService()

while True:
    print("""
i will complete it later""")

    n = int(input("\nEnter your choice: "))
    print()

    match n:
        case 1:
            roll_no = int(input("Enter Student Roll No.: "))
            name = input("Enter Student Name: ")
            Age = int(input("Enter Student Name: "))
            Marks = int(input("Enter marks: "))
            std = student(roll_no,name,Age,Marks)
            call.save_std(std)

        case 2:
            call.display()

        case 3:
            name = input("Enter Student Name: ")
            call.dis_name(name)

        case 4:
            name = input("Enter Student Name: ")
            call.delete_std(name)

        case 5:
            roll_no = int(input("Enter Student Roll no.: "))
            name = input("Enter Student Name: ")
            marks = int(input("Enter Student Marks: "))
            Age = int(input("Enter Student Age: "))
            std = student(roll_no,name,Age,marks)
            call.update(std)

        case 6:
            print("\nThank-You")
            break

        case __:
            print("\nTry Again")