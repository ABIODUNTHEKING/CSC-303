import json

class Student:
    def __init__(self, name, id, department):
        self._name = name # Protected attribute name
        self._id = id # Protecte attribute id
        self._department = department # Protected attribute department

    def get_name(self):
        return self._name

    def get_id(self):
        return self._id
    
    def get_department(self):
        return self._department
    
class Grades(Student):
    def __init__(self, name, id, department):
        super().__init__(name, id, department)
        self._subject_scores = {}

    def add_score(self, subject, score, units):
        self._subject_scores[subject] = [score, units]

    def calculateGPA(self):
        if not _subject_scores:
            return 0 # Handle the case of no scores yet
        
        total_grade_points = 0
        num_subjects = len(self._subject_scores)

        for score in self._subject_scores.values(): #find a way to incorporate units into this
            if 70 <= score <= 100:
                grade_point = 5.0
            elif 60 <= score <=70:
                grade_point = 4.0
            elif 50 <= score <= 60:
                grade_point = 3.0
            elif 45 <= score <= 50:
                grade_point = 2.0
            elif 40 <= score <= 45:
                grade_point = 1.0
            else:
                grade_point = 0.0
            

    def displayGPA(self):
        return 

# this function allows us to save multiple students and add them to a file
def add_student(Student):
    return

victor = Grades("Victor", 2, "CSC")
print(victor.get_name())
