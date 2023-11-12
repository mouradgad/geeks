class Solution:
	def timeToWord(self, h, m):
		# code here
		nums = ["zero", "one", "two", "three", "four",
           "five", "six", "seven", "eight", "nine",
           "ten", "eleven", "twelve", "thirteen",
           "fourteen", "fifteen", "sixteen",
           "seventeen", "eighteen", "nineteen",
           "twenty", "twenty one", "twenty two",
           "twenty three", "twenty four",
           "twenty five", "twenty six", "twenty seven",
           "twenty eight", "twenty nine"]
       
        if (m == 0):
           return "".join(map(str,(nums[h], " o' clock")))

        elif (m == 1):
           return " ".join(map(str,("one minute past", nums[h])))

        elif (m == 59):
           return " ".join(map(str,("one minute to", nums[(h % 12) + 1])))
    
        elif (m == 15):
           return " ".join(map(str,("quarter past", nums[h])))
    
        elif (m == 30):
           return " ".join(map(str,("half past", nums[h])))
    
        elif (m == 45):
           return " ".join(map(str,("quarter to", (nums[(h % 12) + 1]))))
    
        elif (m < 30):
           return " ".join(map(str,(nums[m],"minutes past", nums[h])))
    
        elif (m > 30):
           return " ".join(map(str,(nums[60 - m], "minutes to",nums[(h % 12) + 1])))