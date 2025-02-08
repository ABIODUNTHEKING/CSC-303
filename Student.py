from Course import Course

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
    
    def add_course(self, name, code, score, unit):
        course = Course(name, code, score, unit)
        self._courses.append(course.get_course_details())

    def get_student_details(self):
        return {
            "name": self._name,
            "id": self._id,
            "department": self._department,
            "courses": self._courses
        }

