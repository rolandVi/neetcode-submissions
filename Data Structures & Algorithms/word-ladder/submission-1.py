class SolutionMine:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        def differsByOne(a: str, b: str) -> bool:
            diff = 0
            for i in range(len(a)):
                if a[i] != b[i]:
                    diff += 1

                if diff >= 2:
                    return False
            return True

        wordList.append(beginWord)
        n = len(wordList)
        adj_map = defaultdict(list)
            
        for i in range(n):
            for j in range(i+1, n):
                w1 = wordList[i]
                w2 = wordList[j]
                if differsByOne(w1, w2):
                    adj_map[w1].append(w2)
                    adj_map[w2].append(w1)
        
        q = deque()
        q.append([beginWord, 1])
        seen = set()

        while q:
            word, dis = q.popleft()
            if word == endWord:
                return dis
            if word in seen:
                continue

            seen.add(word)

            for nei in adj_map[word]:
                if nei not in seen:
                    q.append([nei, dis+1])
        
        return 0


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0

        # Build wildcard pattern adjacency map: O(N * L^2)
        L = len(beginWord)
        pattern_map = defaultdict(list)
        for word in word_set:
            for i in range(L):
                pattern = word[:i] + "*" + word[i + 1:]
                pattern_map[pattern].append(word)

        # Standard BFS marking seen on enqueue
        q = deque([(beginWord, 1)])
        seen = {beginWord}

        while q:
            word, dist = q.popleft()
            if word == endWord:
                return dist

            for i in range(L):
                pattern = word[:i] + "*" + word[i + 1:]
                for nei in pattern_map[pattern]:
                    if nei not in seen:
                        seen.add(nei)
                        q.append((nei, dist + 1))
                # Optional: clear list so we never re-scan this pattern
                pattern_map[pattern].clear()

        return 0