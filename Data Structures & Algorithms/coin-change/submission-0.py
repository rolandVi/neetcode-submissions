class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
            
        counts = [-2 for _ in range(amount)]

        n = len(coins)

        def rec(value: int) -> int:
            if value == amount:
                return 0
            if value > amount:
                return -1
            
            if counts[value] != -2:
                return counts[value]

            minimun_coins = 10_001
            for c in coins:
                branch = rec(value + c)
                if branch != -1:
                    minimun_coins = min(minimun_coins, branch + 1)
            
            if minimun_coins == 10_001:
                minimun_coins = -1

            counts[value] = minimun_coins
            return minimun_coins

        rec(0)

        return counts[0]