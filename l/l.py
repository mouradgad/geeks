from ast import literal_eval

def calculate_gpa(noOfRecords, records):
    students = []
    
    for record in records:
        parts = record.split(',,')
        name = parts[0]
        courses = literal_eval(parts[1])
        grades = literal_eval(parts[2])
        
      
        total_gp = 0
        for i in range(len(courses)):
            final_grade = sum(grades[i])
            gp = calculate_gp(final_grade)
            total_gp += gp
        
        overall_gpa = round(total_gp / len(courses), 5)
        students.append((name, overall_gpa))
    
    
    students = sort_students(students)
    
    
    for i in range(min(5, len(students))):
        print(f"{students[i][0]},{students[i][1]}")

def calculate_gp(final_grade):
    
    if final_grade >= 95:
        return 4.0
    elif final_grade >= 90:
        return 3.9
    elif final_grade >= 85:
        return 3.8
    elif final_grade >= 80:
        return 3.7
    elif final_grade >= 77:
        return 3.3
    elif final_grade >= 73:
        return 3.0
    elif final_grade >= 70:
        return 2.7
    elif final_grade >= 67:
        return 2.3
    elif final_grade >= 63:
        return 2.0
    elif final_grade >= 60:
        return 1.7
    elif final_grade >= 57:
        return 1.3
    elif final_grade >= 53:
        return 1.0
    elif final_grade >= 50:
        return 0.7
    else:
        return 0.0

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


number_of_records = int(input("Enter the number of records: "))
records = []
for i in range(number_of_records):
    record_input = input(f"Enter record {i+1}: ")
    records.append(record_input)

calculate_gpa(number_of_records, records)
