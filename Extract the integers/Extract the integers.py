s="ncionc1jd129e12312ionason1oc2"
result = ""
for char in s:
    if char.isdigit():
        result += char 
    else:
        result += " "
num_list = result.split()
print(num_list)