import math
N=13
g=[]
f=0
for i in (str(N)):
    g.append(math.factorial(int(i)))
for j in g:
    f+=j
if f == N:
    print(1)
else :
    print(0)