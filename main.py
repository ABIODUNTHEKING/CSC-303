"""
Module: main
This module implements a command-line interface (CLI) to manage student data.
Users can add new students (with courses), view the list of students, save data,
and generate a PDF report of all student results in tabular form.
"""

from json_handler import save_students, read_students_data
from Grade import Grades
from Student import Student
from pdf_generator import generate_pdf_for_all_students

def input_student():
    """
    Prompt the user to enter student details and courses.
    
    Returns:
        Grades: A new Grades instance with the entered student information and courses.
    """
    print("\n--- Enter Student Details ---")
    name = input("Enter student name: ").strip()
    student_id = input("Enter student ID: ").strip()
    department = input("Enter department: ").strip()
    
    # Using the Grades class (which extends Student) so we can calculate GPA later
    student = Grades(name, student_id, department)
    
    # Loop to allow entering multiple courses for the student
    while True:
        add_course = input("Add a course for this student? (Y/N): ").strip().lower()
        if add_course != 'y':
            break

        
        course_name = input("  Course Name: ").strip()
        course_code = input("  Course Code: ").strip()
        try:
            course_score = float(input("  Course Score: ").strip())
            course_unit = float(input("  Course Unit: ").strip())
        except ValueError:
            print("  Invalid score or unit. Please enter numeric values. Skipping this course.")
            continue
        student.add_course(course_name, course_code, course_score, course_unit)
        print(f"  Course '{course_name}' added successfully!")
      


        
    return student



def main():
    """
    Main function that runs the interactive CLI.
    It loads existing student data, allows the user to manage students,
    generates a PDF report, and saves data when requested.
    """
    # Load existing student data from JSON
    students = []
    existing_data = read_students_data()
    for student_data in existing_data:
        # Create a Grades instance for each stored student for GPA calculation support
        student = Grades(student_data["name"], student_data["id"], student_data["department"])
        for course in student_data["courses"]:
            student.add_course(course["name"], course["code"], course["score"], course["unit"])
        students.append(student)
    
    while True:
        print("\n--- Student Management CLI ---")
        print("1. Add New Student")
        print("2. Exit")
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            new_student = input_student()
            students.append(new_student)
            save_students(students)
            print("Students data saved successfully.")

           
       
        elif choice == '2':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
