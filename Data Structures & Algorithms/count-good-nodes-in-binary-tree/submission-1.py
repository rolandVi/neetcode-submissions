# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        sol = 0

        def dfs(node: TreeNode, maxi: int) -> None:
            nonlocal sol
            if node == None:
                return
            if node.val >= maxi:
                sol += 1
            
            maxi = max(maxi, node.val)
            dfs(node.left, maxi)
            dfs(node.right, maxi)
        
        dfs(root, -101)
        return sol