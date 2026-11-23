# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class SolutionMine:
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

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')

        def max_gain(node: Optional[TreeNode]) -> int:
            nonlocal max_sum
            if not node:
                return 0

            # Max gain we can get from left and right subtrees (ignore if negative)
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)

            # Price of a path that splits at this node
            current_path_sum = node.val + left_gain + right_gain
            max_sum = max(max_sum, current_path_sum)

            # Return the max gain if continuing the same path upward
            return node.val + max(left_gain, right_gain)

        max_gain(root)
        return max_sum