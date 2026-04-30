from functools import lru_cache

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)

        @lru_cache(None)
        def rec(i: int, j: int) -> int:
            if j == m:
                return n - i # delete the rest pf word1
            if i == n:
                return m - j # isnert the rest of word2
            
            if word1[i] == word2[j]:
                return rec(i+1, j+1)
            else:
                insert = rec(i, j+1) + 1
                delete = rec(i+1, j) + 1
                replace = rec(i+1, j+1) + 1
                return min(delete, replace, insert)

        return rec(0, 0)