from Student import Student

class Grades(Student):
    def __init__(self, name, id, department):
        super().__init__(name, id, department)
        

    def calculate_gpa(self):
        if not self._courses:
            return "No courses available to calculate GPA"

        total_student_point = 0
        total_course_unit = 0
       
        for course in self._courses:
            total_course_unit += course["unit"]
            total_student_point += course["grade_point"] * course["unit"]
                    

        if(total_course_unit > 0):
             return total_student_point / total_course_unit

        return 0
    

    def display_gpa(self):
        return f'{self.get_name()} with matric number {self.get_id()} has a CGPA of {self.calculate_gpa()}'
    