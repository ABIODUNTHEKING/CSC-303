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
