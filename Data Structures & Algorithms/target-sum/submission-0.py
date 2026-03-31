class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        def rec(i: int, suma: int) -> int:
            if i == n:
                if suma == target:
                    return 1
                return 0

            return rec(i+1, suma+ nums[i]) + rec(i+1, suma-nums[i])
        
        return rec(0, 0)