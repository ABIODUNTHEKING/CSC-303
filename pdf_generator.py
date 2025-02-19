"""
Module: pdf_generator
This module generates an A4 PDF report displaying each student's results in a tabular format.
Each student's details (name, ID, department, GPA) and a table of courses (with course name,
code, score, unit, and grade point) are printed on separate pages.
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, PageBreak, Spacer

def generate_pdf_for_all_students(students, output_file):
    """
    Generate a PDF report in tabular form for all students.
    
    """
    # Build a list of student detail dictionaries by calling each student's getter methods.
    students_details_list = []
    for student in students:
        details = student.get_student_details()
        # If the student has GPA calculation capability, add it to the details.
        if hasattr(student, 'calculate_gpa'):
            details["GPA"] = student.calculate_gpa()
        else:
            details["GPA"] = "N/A"
        students_details_list.append(details)

    # Create the PDF document with A4 page size.
    doc = SimpleDocTemplate(output_file, pagesize=A4)
    elements = []
    styles = getSampleStyleSheet()

    # Loop over each student's details.
    for idx, student in enumerate(students_details_list):
        # Add a title for the student.
        title = Paragraph("Student Result", styles["Title"])
        elements.append(title)
        elements.append(Spacer(1, 12))  # Add space after the title

        # Create paragraphs for basic student information.
        student_name = Paragraph(f"Name: {student.get('name', '')}", styles["Normal"])
        student_id = Paragraph(f"ID: {student.get('id', '')}", styles["Normal"])
        student_department = Paragraph(f"Department: {student.get('department', '')}", styles["Normal"])
        
        # Format GPA: if GPA is a string, print as is, otherwise format to 2 decimal places.
        gpa_value = student.get('GPA', 'N/A')
        if not isinstance(gpa_value, str):
            gpa_value = f"{gpa_value:.2f}"
        student_gpa = Paragraph(f"GPA: {gpa_value}", styles["Normal"])

        # Add details to the document
        elements.extend([student_name, student_id, student_department, student_gpa])
        elements.append(Spacer(1, 20))  # Add space before the table

        # Build a table for course details.
        courses = student.get("courses", [])
        if courses:
            # Header row for courses table.
            table_data = [["Course Name", "Course Code", "Score", "Unit", "Grade Point"]]
            for course in courses:
                row = [
                    course.get("name", ""),
                    course.get("code", ""),
                    str(course.get("score", "")),
                    str(course.get("unit", "")),
                    str(course.get("grade_point", ""))
                ]
                table_data.append(row)
            courses_table = Table(table_data, colWidths=[150, 100, 50, 50, 80])
            courses_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.gray),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ]))
            elements.append(courses_table)
        else:
            elements.append(Paragraph("No courses available.", styles["Normal"]))

        # Add space after the table
        elements.append(Spacer(1, 30))

        # Add a page break after each student except the last one.
        if idx < len(students_details_list) - 1:
            elements.append(PageBreak())

    # Build the PDF document.
    doc.build(elements)
  

