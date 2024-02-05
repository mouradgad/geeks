from ast import literal_eval

def apply_grading_criteria(record):
    parts = record.split(',,')
    name = parts[0]
    courses = literal_eval(parts[1])
    grades = literal_eval(parts[2])

    for i in range(len(courses)):
        course_name = courses[i]
        coursework_grade = grades[i][0]
        exam_grade = grades[i][1]

        if exam_grade == -1:
            letter_grade = 'INC'
            final_grade = -1
        elif coursework_grade < 30 or exam_grade < 20:
            final_grade = min(45, coursework_grade + exam_grade)
            letter_grade = 'F'
        elif coursework_grade < 36 or exam_grade < 24:
            final_grade = min(58, coursework_grade + exam_grade)
            letter_grade = get_new_letter_grade(final_grade)
        else:
            final_grade = coursework_grade + exam_grade
            letter_grade = get_new_letter_grade(final_grade)

        print(f"{course_name}: {letter_grade}, {final_grade}")

def get_new_letter_grade(final_grade):
    if final_grade >= 90:
        return 'A+'
    elif final_grade >= 80:
        return 'A'
    elif final_grade >= 70:
        return 'B'
    elif final_grade >= 60:
        return 'C'
    elif final_grade >= 50:
        return 'D'
    else:
        return 'F'
def calculate_gp(final_grade):
    if final_grade >= 95:
        return 4.00
    elif final_grade >= 90:
        return 3.90
    elif final_grade >= 85:
        return 3.80
    elif final_grade >= 80:
        return 3.70
    elif final_grade >= 77:
        return 3.30
    elif final_grade >= 73:
        return 3.00
    elif final_grade >= 70:
        return 2.70
    elif final_grade >= 67:
        return 2.30
    elif final_grade >= 63:
        return 2.00
    elif final_grade >= 60:
        return 1.70
    elif final_grade >= 57:
        return 1.30
    elif final_grade >= 53:
        return 1.00
    elif final_grade >= 50:
        return 0.70
    else:
        return 0.00

def sort_students(students):
    sorted_students = []
    list_size = len(students)

    for _ in range(list_size):
        min_index = 0

        for i in range(1, len(students)):
            if students[i][1] > students[min_index][1]:
                min_index = i

        sorted_students.append(students.pop(min_index))

    return sorted_students


record = input("Enter the record: ")
apply_grading_criteria(record)