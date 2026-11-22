from functools import lru_cache

class SolutionRec:
    def canPartition(self, nums: List[int]) -> bool:
        suma = sum(nums)
        if suma % 2 == 1:
            return False
        
        goal = suma // 2

        @lru_cache(None)
        def rec(weigth: int, i: int) -> bool:
            if weigth == 0:
                return True
            if i <= -1:
                return False
            
            return rec(weigth, i-1) or rec(weigth - nums[i], i-1)
        
        return rec(goal, len(nums)-1)

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        suma = sum(nums)
        n = len(nums)
        if suma % 2 == 1:
            return False
        
        goal = suma // 2
        dp = [[False] * (goal+1) for _ in range(n)]
        for i in range(n):
            dp[i][0] = True
        
        for i in range(n):
            for w in range(goal+1):
                weight = nums[i]
                if weight <= w:
                    dp[i][w] = dp[i-1][w] or dp[i-1][w - weight]
                else:
                    dp[i][w] = dp[i-1][w]
        
        return dp[n-1][goal]


        