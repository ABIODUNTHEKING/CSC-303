from json_handler import save_students, read_students_data
from Grade import Grades
from Student import Student


students_data = read_students_data()
students = []


for student in students_data:
    existing_student = Student(student["name"], student["id"], student["department"])
    for course in student["courses"]:
        existing_student.add_course(course["name"], course["code"], course["score"], course["unit"])
    students.append(existing_student)


victor = Grades("Victor", "ABC12345", "CSC")
victor.add_course("Introduction to MLS", "MLS 102", 75, 1)
victor.add_course("Cooking MLS", "MLS 104", 70, 4)

students.append(victor)
save_students(students)