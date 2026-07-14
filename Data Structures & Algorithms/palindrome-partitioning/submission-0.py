class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        
        def isPalidrome(a: str) -> bool:
            m = len(a)
            for i in range(m//2):
                if a[i] != a[m-1-i]:
                    return False
            return True
        
        memo: Dict[int, List[List[str]]] = {}
        
        def divide(i: int) -> List[List[str]]:
            if i == n:
                return []
            if memo.get(i) is not None:
                return memo.get(i)

            res = []
            for j in range(i+1, n+1):
                current_string = s[i:j]
                if isPalidrome(current_string):
                    recursion_result = divide(j)
                    if not recursion_result:
                        res.append([current_string])
                    for division in recursion_result:
                        res.append([current_string] + division)

            memo[i] = res
            return res

        return divide(0)

