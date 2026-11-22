from sortedcontainers import SortedDict

class Solution1:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        tree_map = SortedDict()
        sol = []
        n = len(nums)

        for i in range(k):
            if not tree_map.get(nums[i], None):
                tree_map[nums[i]] = 1
            else:
                tree_map[nums[i]] += 1
        
        for s in range(n-k):
            sol.append(tree_map.peekitem(-1)[0])

            tree_map[nums[s]] -= 1
            if tree_map[nums[s]] == 0:
                tree_map.pop(nums[s])
            
            if not tree_map.get(nums[s+k], None):
                tree_map[nums[s+k]] = 1
            else:
                tree_map[nums[s+k]] += 1

        sol.append(tree_map.peekitem(-1)[0])
        
        return sol

from sortedcontainers import SortedList

class Solution2:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = SortedList(nums[:k])
        sol = [window[-1]]

        for i in range(k, len(nums)):
            window.remove(nums[i - k])
            window.add(nums[i])
            sol.append(window[-1])

        return sol

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        sol = []

        def addToDeque(a: int) -> None:
            while dq and dq[-1] < a:
                dq.pop()
            dq.append(a)
        
        for i, a in enumerate(nums):
            addToDeque(a)

            if i >= k-1:
                sol.append(dq[0])

                if dq[0] == nums[i - k + 1]:
                    dq.popleft()
        
        return sol

