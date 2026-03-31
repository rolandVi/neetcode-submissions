class Solution:
    def countSubstrings(self, s: str) -> int:
        sol = 0

        n = len(s)

        for i in range(n):
            # odd
            r, l = i, i
            while r >= 0 and l < n and s[r] == s[l]: 
                sol += 1
                r -= 1
                l += 1

            # even
            r, l = i, i+1
            while r >= 0 and l < n and s[r] == s[l]: 
                sol += 1
                r -= 1
                l += 1
        
        return sol