class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        sol = []

        def recursion(i: int, subset: List[int]) -> None:
            if i == n:
                sol.append(subset[:])
                return
            
            r = i
            while r < n-1 and nums[r+1] == nums[r]:
                r += 1
            num_same = r - i + 1
            
            recursion(i + num_same, subset)
            for j in range(num_same):
                subset.append(nums[i + j])
                recursion(i + num_same, subset)
            
            for _ in range(num_same):
                subset.pop()

        recursion(0, [])
        return sol
