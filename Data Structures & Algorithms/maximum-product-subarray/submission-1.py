class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        sol = nums[0]
        product = 1
        smallest_negative = 1

        for i in nums:
            if i == 0:
                product = 1
                smallest_negative = 1
                sol = max(0, sol)
                continue

            product *= i
            sol = max(sol, product, product // smallest_negative)

            if product < 0:
                if smallest_negative == 1 or abs(product) < abs(smallest_negative):
                    smallest_negative = product
    
        return sol