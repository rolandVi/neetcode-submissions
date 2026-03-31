class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counts_upper = [0] * 26
        counts_lower = [0] * 26
        for c in t:
            if ord(c) >= 97:
                counts_lower[ord(c) - ord("a")] += 1
            else:
                counts_upper[ord(c) - ord("A")] += 1
        n, m = len(s), len(t)
        if n < m:
            return ""

        window_lower = [0] * 26
        window_upper = [0] * 26
        
        sol = ""
        length = n + 1
        
        r = -1
        for l in range(n):
            if l != 0:
                if ord(s[l-1]) >= 97:
                    window_lower[ord(s[l-1]) - ord("a")] -= 1
                else:
                    window_upper[ord(s[l-1]) - ord("A")] -= 1
            
            while not self.valid(counts_lower, counts_upper, window_lower, window_upper):
                r += 1
                if r >= n:
                    break
                if ord(s[r]) >= 97:
                    window_lower[ord(s[r]) - ord("a")] += 1
                else:
                    window_upper[ord(s[r]) - ord("A")] += 1
            if not self.valid(counts_lower, counts_upper, window_lower, window_upper):
                break
            if r - l + 1 < length:
                sol = s[l:r+1]
                length = r - l + 1

        return sol

    def valid(self, counts_lower: List, counts_upper: List, window_lower: List, window_upper: List) -> bool:
        for i in range(26):
            if counts_lower[i] > window_lower[i]:
                return False
            if counts_upper[i] > window_upper[i]:
                return False
        return True