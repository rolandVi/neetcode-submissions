from functools import lru_cache
class Solution:
    @lru_cache(None)
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n == 0:
            return 1
        if n == 1:
            return x

        x_2 = x * x
        res = self.myPow(x_2, n // 2)
        if n % 2:
            return res * x
        return res