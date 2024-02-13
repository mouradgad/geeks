def apply_grading_criteria():
    student_name = input("Enter the student's name: ")
    num_courses = int(input("Enter the number of courses: "))
    
    for _ in range(num_courses):
        course_name = input("Enter the course's name: ")
        coursework_grade = int(input("Enter the coursework grade: "))
        exam_grade = int(input("Enter the exam grade: "))
        
        coursework_percentage = (coursework_grade / 60) * 100
        exam_percentage = (exam_grade / 40) * 100
        
        final_grade = -1
        letter_grade = "INC"
        
        if exam_grade == -1:
            print(f"{course_name}: {letter_grade}, {final_grade}")
            continue
        
        if coursework_percentage < 50 or exam_percentage < 50:
            final_grade = min(45, coursework_grade + exam_grade)
        elif coursework_percentage < 60 or exam_percentage < 60:
            final_grade = min(58, coursework_grade + exam_grade)
        else:
            final_grade = coursework_grade + exam_grade
        
        if final_grade >= 90:
            letter_grade = "A+"
        elif final_grade >= 80:
            letter_grade = "A"
        elif final_grade >= 70:
            letter_grade = "B"
        elif final_grade >= 60:
            letter_grade = "C"
        elif final_grade >= 50:
            letter_grade = "D"
        else:
            letter_grade = "F"
        
        print(f"{course_name}: {letter_grade}, {final_grade}")

apply_grading_criteria()
