def count_courses():
    noOfRecords = int(input("Enter the number of records: "))
    records = {}
    
    for i in range(noOfRecords):
        student_name = input("Enter the student's name: ")
        course_name = input("Enter the course's name: ")
        
        if student_name in records:
            records[student_name] += 1
        else:
            records[student_name] = 1
    
    for x,y  in records.items():
        print(f"Student {x} is taking {y} courses")

count_courses()