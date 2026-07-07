class Solution:
    def reverse(self, x: int) -> int:
        max_num = (1 << 31) - 1
        min_num = - (1 << 31)
        print(max_num, min_num)
        sign = 1 if x > 0 else -1
        x = abs(x)

        sol = 0
        while x > 0:
            if sol > max_num/10 or sol < min_num/10:
                return 0
            sol *= 10

            digit = x % 10
            x //= 10
            if sol > max_num - digit * sign or sol < min_num - digit * sign:
                return 0
            sol += digit * sign

        return sol