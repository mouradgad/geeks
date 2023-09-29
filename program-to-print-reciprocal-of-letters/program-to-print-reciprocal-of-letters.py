S="adoiw"
a = ""
for i in S:
    if i.isalpha():
        if i.isupper():
            sub = ord(i) - 65
            char = chr(90 - sub)
            a += char
        elif i.islower():
            sub = ord(i) - 97
            char = chr(122 - sub)
            a += char
    else:
        a+=i
print(a)