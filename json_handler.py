import json
import os



def save_students(students):
    with open("./students.json", "w") as file:
        json.dump([student.get_student_details() for student in students], file)


def read_students_data():
    if not os.path.exists("./students.json"):
        return []
    with open("./students.json", "r") as file:
        return json.load(file)
      