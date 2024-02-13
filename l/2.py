def calculate_gpa(course_grades):
    gp_table = {
        (95, 100): 4.0,
        (90, 94): 3.9,
        (85, 89): 3.8,
        (80, 84): 3.7,
        (77, 79): 3.3,
        (73, 76): 3.0,
        (70, 72): 2.7,
        (67, 69): 2.3,
        (63, 66): 2.0,
        (60, 62): 1.7,
        (57, 59): 1.3,
        (53, 56): 1.0,
        (50, 52): 0.7,
        (0, 49): 0.0
    }
    total_gp = 0
    total_courses = len(course_grades)

    for grade in course_grades:
        course_grade = grade[0] + grade[1]
        for score_range, gp_value in gp_table.items():
            if score_range[0] <= course_grade <= score_range[1]:
                total_gp += gp_value
                break

    return round(total_gp / total_courses, 5)


def sort_students(student_records):
    for i in range(len(student_records)):
        max_index = i
        for j in range(i + 1, len(student_records)):
            if student_records[j][1] > student_records[max_index][1]:
                max_index = j
        student_records[i], student_records[max_index] = student_records[max_index], student_records[i]


def main():
    no_of_records = int(input("Enter the number of records: "))
    student_records = []

    for _ in range(no_of_records):
        student_name = input("Enter the student's name: ")
        no_of_courses = int(input("Enter the number of courses: "))
        courses = []
        for _ in range(no_of_courses):
            course_name = input("Enter the course's name: ")
            coursework_grade = int(input("Enter the coursework grade: "))
            exam_grade = int(input("Enter the exam grade: "))
            courses.append((coursework_grade, exam_grade))
        gpa = calculate_gpa(courses)
        student_records.append((student_name, gpa))

    sort_students(student_records)

    top_students = min(5, len(student_records))
    for i in range(top_students):
        print(f"{student_records[i][0]},{student_records[i][1]:.2f}")



    main()
