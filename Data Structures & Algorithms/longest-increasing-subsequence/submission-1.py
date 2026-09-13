class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        lengths = [0 for i in range(n)]
        for i, num in enumerate(nums):
            j = i -1
            len_before = 0
            for j in range(i-1, -1, -1):
                if nums[j] < num:
                    len_before = max(len_before, lengths[j])
            
            lengths[i] = len_before + 1
        
        sol = 0
        for length in lengths:
            sol = max(sol, length)
        
        return sol