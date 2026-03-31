from functools import lru_cache

class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        
        @lru_cache(None)
        def rec(i: int) -> int:
            if i == n:
                return 1
            if s[i] == "0":
                return 0
            
            one = rec(i+1)
            two = 0

            if i < n-1 and int(s[i:i+2]) <= 26:
                two = rec(i+2)
            
            return one + two

        return rec(0)