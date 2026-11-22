from functools import lru_cache

class Solution:
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