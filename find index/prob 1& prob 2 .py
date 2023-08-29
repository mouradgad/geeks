'''
Example 1:

Input: n = 555
Output: Yes

Example 2:

Input: n = 123
Output: No

Example 1:

Input:
N = 8, K = 3
Arr[] = {1, 2, 3, 4, 5, 6, 7, 8}
Output: 1 2 6 4 5 3 7 8
Explanation: Kth element from beginning is
3 and from end is 6.
Example 2:

Input:
N = 5, K = 2
Arr[] = {5, 3, 6, 1, 2}
Output: 5 1 6 3 2
Explanation: Kth element from beginning is
3 and from end is 1.
Your Task:
'''

def prob1(num):
    f=str(num)
    g=f[::-1]
    if g==f:
        return "Yes"
    else:
        return "No"
      

        
    
    

def prob2(arr,num1,num2):
    n1 = num1 - 1
    n2= num2-num1-1
    arr[n1],arr[n2] = arr[n2],arr[n1]
    return arr

f=[1,2,3,4,5,6,7,8]
g=prob2(f,2,8)
print (g)