def addBinary(self, a: str, b: str) -> str:
        int1 = int(a, 2)
        int2 = int(b, 2)
        

        int_sum = int1 + int2

        bin_sum = bin(int_sum)[2:]  
        
        return bin_sum