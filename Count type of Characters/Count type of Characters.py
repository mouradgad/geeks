s="AZDVAIHsoasaiocha1231314)!@#!"
upper=0
lower=0
numbers=0
special=0
for i in s:
    if i.isupper():
        upper+=1
    elif i.islower():
        lower+=1
    elif i.isnumeric():
        numbers+=1
    else:
        special+=1
print(upper,lower,numbers,special)