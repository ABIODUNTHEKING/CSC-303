"""
This module provides utility functions for saving and reading student data in JSON format.

Functions:
    save_students(students): Saves a list of student objects to a JSON file.
    read_students_data(): Reads student data from a JSON file and returns it as a list of dictionaries.
"""

import json
import os

from pdf_generator import generate_pdf_for_all_students

output_file = "StudentResults.pdf"

def save_students(students):
    """
    Save the details of a list of student objects to a JSON file.
    
    """
    with open("./students.json", "w") as file:
        # Create a list of dictionaries from the student objects.
        data = [student.get_student_details() for student in students]


        generate_pdf_for_all_students(students, output_file)
        json.dump(data, file, indent=4)  # Write JSON data with indentation for readability.

def read_students_data():
    """
    Read student data from a JSON file.
    
    This function checks if the file 'students.json' exists in the current working directory.
    If the file exists, it reads the file, parses the JSON content, and returns a list of 
    student data dictionaries. If the file does not exist, it returns an empty list.
    """
    if not os.path.exists("./students.json"):
        # Return an empty list if the JSON file does not exist.
        return []
    with open("./students.json", "r") as file:
        # Load and return the JSON data as a list of dictionaries.
        return json.load(file)
