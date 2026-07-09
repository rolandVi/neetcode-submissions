class SolutionMine:
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
            
            mem[i] = 1 if res else 0
            return res

        return rec(0)

class SolutionBasic:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break

        return dp[0]

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True

    def search(self, s, i, j):
        node = self.root
        for idx in range(i, j + 1):
            if s[idx] not in node.children:
                return False
            node = node.children[s[idx]]
        return node.is_word

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = Trie()
        for word in wordDict:
            trie.insert(word)

        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        t = 0
        for w in wordDict:
            t = max(t, len(w))

        for i in range(len(s), -1, -1):
            for j in range(i, min(len(s), i + t)):
                if trie.search(s, i, j):
                    dp[i] = dp[j + 1]
                    if dp[i]:
                        break

        return dp[0]