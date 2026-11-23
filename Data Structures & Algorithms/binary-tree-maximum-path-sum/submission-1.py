# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.sol = -1000

        def rec(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            left = max(rec(node.left), 0) + node.val
            right = max(rec(node.right), 0) + node.val

            together = left - node.val + right

            self.sol = max(self.sol, left, right, together)

            return max(left, right)

        rec(root)

        return self.sol