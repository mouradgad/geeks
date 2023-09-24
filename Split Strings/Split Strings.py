S="b1397cg1xjzm90j0j!!!@3"
S1=S2=S3=""
for i in S:
    if i.isdigit():
        S2+=i
    elif i.isalpha():
        S1+=i
    else:
        S3+=i
print (S1,S2,S3)