"""
Module: Grade
This module defines the Grades class, which extends the Student class to provide
methods for calculating and displaying the student's GPA (Grade Point Average).
"""

from Student import Student

class Grades(Student):
    def __init__(self, name, id, department):
        super().__init__(name, id, department)
    
    def calculate_gpa(self):
        """
        Calculate the student's GPA based on the courses added.
        
        The GPA is computed as the sum of (grade point × course unit) for each course,
        divided by the total number of units. If no courses are available, a message is returned.
        
        """
        if not self._courses:
            return "No courses available to calculate GPA"
        
        total_student_point = 0
        total_course_unit = 0
        
        
        for course in self._courses:
            total_course_unit += course["unit"]
            total_student_point += course["grade_point"] * course["unit"]
        
        
        if total_course_unit > 0:
            return total_student_point / total_course_unit
        
        return 0
    
    def display_gpa(self):
        return f'{self.get_name()} with matric number {self.get_id()} has a CGPA of {self.calculate_gpa()}'
