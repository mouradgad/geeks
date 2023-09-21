ans = []
S="hello"
n = len(S)
for i in range(n):
    ans.append(S[:n-i])
print (ans)