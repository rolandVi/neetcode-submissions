from sortedcontainers import SortedDict

class Solution:
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