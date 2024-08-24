class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        number=0
        for i in nums:
            counter=0
            for j in nums:
                if j==i:
                    counter+=1
            if counter <=1  :
                number = i
        return number
            
