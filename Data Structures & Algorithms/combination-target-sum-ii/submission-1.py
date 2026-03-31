class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)

        combos = set()

        def rec(arr: List[int], i: int, suma: int) -> None:
            if suma == target:
                combos.add(tuple(arr))
                return
            if suma > target or i >= n:
                return

            arr.append(candidates[i])
            suma += candidates[i]

            rec(arr, i+1, suma)

            arr.pop()
            suma -= candidates[i]

            cur = candidates[i]
            while i < n and candidates[i] == cur:
                i += 1
            rec(arr, i, suma)

        rec([], 0, 0)
        
        sol = list(map(lambda x: list(x), combos))
        return sol
