input_str = "Sara,,English,,(60,40)\nSara,,French,,(35,38)"


lines = input_str.split('\n')

new_list = []


for line in lines:

    parts = line.split(',,')

    name = parts[0]
    language = [parts[1]]
    values = [parts[2]]

    line2 = [name, language, values]

    new_list.append(line2)

print(new_list)