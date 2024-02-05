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
    
    max_name_length = max(len(name) for name, _ in students)  
    for i in range(min(5, len(students))):
        name, gpa = students[i]
        print(f"\033[32m{f'{name}:':<{max_name_length + 2}}{format(gpa, '.2f')}\033[0m")

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


number_of_records = int(input("Enter the number of records: "))
records = []
for i in range(number_of_records):
    record_input = input(f"Enter record {i+1}: ")
    records.append(record_input)

calculate_gpa(number_of_records, records)
