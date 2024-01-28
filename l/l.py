def transform_records(no_of_records, *records):
    new_list = {}

    for record in records:
        parts = record.split(',,')
        name = parts[0]
        course = parts[1]
        grades = parts[2]

        if name in new_list:
            new_list[name][1].append(course)
            new_list[name][2].append(grades)
        else:
            new_list[name] = [name, [course], [grades]]

    for i in new_list:
        print(new_list[i])


number_of_records = int(input("Enter the number of records: "))

records = []
for i in range(number_of_records):
    record_input = input(f"Enter record {i+1}: ")
    records.append(record_input)

transform_records(number_of_records, *records)