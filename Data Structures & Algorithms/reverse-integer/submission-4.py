class Solution:
    def reverse(self, x: int) -> int:
        MAX_INT = (1 << 31) - 1
        MIN_INT = -(1 << 31)
        
        sign = -1 if x < 0 else 1
        x = abs(x)
        res = 0
        
        while x > 0:
            if res > MAX_INT // 10:
                return 0
                
            res = res * 10 + (x % 10)
            x //= 10
            
        res *= sign
        return res