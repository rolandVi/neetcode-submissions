class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        sol = []

        def rec(i: int, seen: set, arr: List[int]) -> None:
            if i == n:
                sol.append(arr[:])
                return

            for num in nums:
                if num not in seen:
                    arr.append(num)
                    seen.add(num)

                    rec(i+1, seen, arr)

                    arr.pop()
                    seen.remove(num)
        
        rec(0, set(), [])

        return sol