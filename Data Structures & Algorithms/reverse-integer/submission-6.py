class Solution:
    def reverse(self, x: int) -> int:
        max_num = (1 << 31) - 1
        min_num = - (1 << 31)
        sign = 1 if x > 0 else -1
        x = abs(x)

        sol = 0
        while x > 0:
            if sol > max_num/10 or sol < min_num/10:
                return 0
            sol *= 10

            digit = x % 10
            x //= 10
            sol += digit * sign

        return sol