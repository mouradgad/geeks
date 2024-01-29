from ast import literal_eval

def transform_records(no_of_records, *records):
    new_list = []

    for record in records:
        parts = record.split(',,')
        name = parts[0]
        course = parts[1]
        grades_str = parts[2]
        grades = literal_eval(grades_str)

        existence = False
        for entry in new_list:
            if entry[0] == name:
                entry[1].append(course)
                entry[2].append(grades)
                existence = True
                break

        if not existence:
            new_list.append([name, [course], [grades]])

    for entry in new_list:
        total_calc = 0
        for i in entry[2].literal_eval():
            total_calc += sum(i)

        print(f"Total GPA for {entry[0]}: {total_calc / len(entry[2])}")

number_of_records = int(input("Enter the number of records: "))
records = []
for i in range(number_of_records):
    record_input = input(f"Enter record {i+1}: ")
    records.append(record_input)

transform_records(number_of_records, *records)
