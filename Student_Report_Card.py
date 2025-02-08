import json


gradingFormat = [
    {"grade":"A","grade_point": 5, "minimum_score": 70,"maximum_score": 100},
    {"grade":"B","grade_point": 4,"minimum_score": 60,"maximum_score": 69},
    {"grade":"C","grade_point": 3,"minimum_score": 50,"maximum_score": 59},
    {"grade": "D","grade_point": 2,"minimum_score": 45,"maximum_score": 49},
    {"grade": "E","grade_point": 1,"minimum_score": 40,"maximum_score": 44},
    {"grade": "F","grade_point": 0,"minimum_score": 0,"maximum_score": 39},  
]


class Course: 
    def __init__(self, name, code, score,unit):
        self.name = name
        self.code = code
        self.score = score
        self.unit = unit

    def get_grade_point(self,score):
        for format in gradingFormat:
            if format["minimum_score"] <= score <= format["maximum_score"]:
                return format["grade_point"]
        return 0


    def get_course_details(self):
        return {"name": self.name, "code": self.code, "unit": self.unit, "score": self.score, "grade_point": self.get_grade_point(self.score) }
    
    

class Student:
    def __init__(self, name, id, department):
        self._name = name # Protected attribute name
        self._id = id # Protecte attribute id
        self._department = department # Protected attribute department
        self._courses = []

    def get_name(self):
        return self._name

    def get_id(self):
        return self._id
    
    def get_department(self):
        return self._department


    def get_student_details(self):
        return {
            "name": self._name,
            "id": self._id,
            "department": self._department,
            "courses": self._courses
        }

    def add_course(self, name, code, score, unit):
        course = Course(name, code, score, unit)
        self._courses.append(course.get_course_details())
    
    



class Grades(Student):
    def __init__(self, name, id, department):
        super().__init__(name, id, department)
        # self._subject_scores = {}

    # def add_score(self, subject, score, units):
    #     self._subject_scores[subject] = [score, units]

    # def calculateGPA(self):
    #     if not self._subject_scores:
    #         return 0 # Handle the case of no scores yet
        
    #     total_grade_points = 0
    #     num_subjects = len(self._subject_scores)

    #     for score in self._subject_scores.values(): #find a way to incorporate units into this
    #         if 70 <= score <= 100:
    #             grade_point = 5.0
    #         elif 60 <= score <=70:
    #             grade_point = 4.0
    #         elif 50 <= score <= 60:
    #             grade_point = 3.0
    #         elif 45 <= score <= 50:
    #             grade_point = 2.0
    #         elif 40 <= score <= 45:
    #             grade_point = 1.0
    #         else:
    #             grade_point = 0.0


    def calculateGPA(self):
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
    
    def calculateCGPA(self):
        pass

    def displayGPA(self):
        return f'{self.get_name()} with matric number {self.get_id()} has a CGPA of {self.calculateGPA()}'





"""
The accepted format for the Student is 

{
    name: "Student Name",
    id: "Student id",
    level: Student level,
    department: Student Department,
    courses: [
        {
            unit: Course Unit,
            code: "Course Code",
            name: "Course Name",
            score: Course Score, 
        },
        {
            unit: Course Unit,
            code: "Course Code",
            name: "Course Name",
            score: Course Score,
        }
    ]
}


Students will be Student[]
"""


# this function allows us to save multiple students and add them to a file
def add_student(Student):
    return

victor = Grades("Victor", "ABC12345", "CSC")
victor.add_course("Intoduction to MLS", "MLS 102", 75, 1)
victor.add_course("Cooking MLS", "MLS 104", 70, 4)


print(victor.displayGPA())

