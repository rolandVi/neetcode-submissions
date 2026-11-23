# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        sol = -1000

        def rec(node: Optional[TreeNode]) -> int:
            nonlocal sol
            if not node:
                return 0

            left = max(rec(node.left), 0)
            right = max(rec(node.right), 0)

            together = left + node.val + right

            sol = max(sol, together)

            return max(left, right) + node.val

        rec(root)

        return sol