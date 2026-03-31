# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        sol = []
        level = [root]
        if not root:
            return sol

        while len(level) != 0:
            level_values = []
            new_level = []
            for node in level:
                level_values.append(node.val)
                if node.left:
                    new_level.append(node.left)
                if node.right:
                    new_level.append(node.right)
            sol.append(level_values)
            level = new_level
        
        return sol
