num1=12
num2=5

s=num1+num2
if s<12 :
    print(s)
elif s==12:
    print (0)
else:
    while s>=12:
        s-=12
        if s<12:
            print(s)
        elif s==12:
            print(0)