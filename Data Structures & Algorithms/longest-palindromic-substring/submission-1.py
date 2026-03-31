class Solution:
    def longestPalindrome(self, s: str) -> str:
        sol = ''

        n = len(s)

        for i in range(n):
            # odd
            r, l = i, i
            while r >= 0 and l < n and s[r] == s[l]: 
                if l - r + 1 > len(sol):
                    sol = s[r:l+1]
                r -= 1
                l += 1

            # even
            r, l = i, i+1
            while r >= 0 and l < n and s[r] == s[l]: 
                if l - r + 1 > len(sol):
                    sol = s[r:l+1]
                r -= 1
                l += 1
        
        return sol