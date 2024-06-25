class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        max = 2**31 - 1
        min = -2**31
        reversed_num = int(str(abs(x))[::-1])
        reversed_num = reversed_num*sign
        if reversed_num > max or reversed_num <min :
            return 0
        return reversed_num