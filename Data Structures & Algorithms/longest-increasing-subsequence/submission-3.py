class Solution:
    def lengthOfLISslow(self, nums: List[int]) -> int:
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

    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = [nums[0]]

        def binaryAddition(tails: List[int], a: int) -> None:
            m = len(tails)
            if a > tails[-1]:
                tails.append(a)
                return
            
            idx = -1
            jump = m
            while jump > 0:
                while(idx + jump < m and tails[idx + jump] <= a):
                    idx += jump
                jump //= 2

            if idx == m-1 or tails[idx] == a:
                return
            tails[idx + 1] = a
            return

        for a in nums[1:]:
            binaryAddition(tails, a)
        
        return len(tails)
            
            
                