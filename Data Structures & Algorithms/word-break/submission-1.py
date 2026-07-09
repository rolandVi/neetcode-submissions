class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        mem = [-1 for _ in range(n)]

        def rec(i: int) -> bool:
            if i == n:
                return True
            if mem[i] != -1:
                return True if mem[i] == 1 else False
            
            res = False
            for word in wordDict:
                if word[0] == s[i]:
                    m = len(word)
                    if i + m > n:
                        continue

                    idx = i
                    valid = True
                    for j in range(m):
                        if s[idx] != word[j]:
                            valid = False
                            break
                        idx += 1

                    if valid:
                        res |= rec(i + m)
            # print(i, res)
            
            mem[i] = 1 if res else 0
            return res

        return rec(0)