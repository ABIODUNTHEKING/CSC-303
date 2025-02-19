"""
This module defines the Course class and a grading format used to determine
grade points based on course scores.
"""

# Grading format specifying the grading scale for courses.
gradingFormat = [
    {"grade": "A", "grade_point": 5, "minimum_score": 70, "maximum_score": 100},
    {"grade": "B", "grade_point": 4, "minimum_score": 60, "maximum_score": 69},
    {"grade": "C", "grade_point": 3, "minimum_score": 50, "maximum_score": 59},
    {"grade": "D", "grade_point": 2, "minimum_score": 45, "maximum_score": 49},
    {"grade": "E", "grade_point": 1, "minimum_score": 40, "maximum_score": 44},
    {"grade": "F", "grade_point": 0, "minimum_score": 0,  "maximum_score": 39},
]

class Course:
    """
    Represents a course taken by a student.

    Attributes:
        name (str): The name of the course.
        code (str): The unique code identifier for the course.
        score (float): The score achieved in the course.
        unit (float): The credit unit associated with the course.
    """

    def __init__(self, name, code, score, unit):
        self.name = name
        self.code = code
        self.score = score
        self.unit = unit

    def get_grade_point(self, score):
        """
        Calculate the grade point corresponding to the provided score using the grading format.

        Returns the grade point from the gradingFormat. Returns 0 if the score doesn't fall within any specified range.
        """
        for format in gradingFormat:
            # Check if the score is within the range specified by the current grading format.
            if format["minimum_score"] <= score <= format["maximum_score"]:
                return format["grade_point"]
        return 0

    def get_course_details(self):
        """
        Retrieve all details of the course as a dictionary.
        """
        return {
            "name": self.name,
            "code": self.code,
            "unit": self.unit,
            "score": self.score,
            "grade_point": self.get_grade_point(self.score)
        }
