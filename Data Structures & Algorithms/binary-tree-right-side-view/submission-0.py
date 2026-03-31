# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        sol = []
        seen = [False for i in range(100)]

        def dfs(node: Optional[TreeNode], depth: int) -> None:
            if node == None:
                return
            if seen[depth] is False:
                sol.append(node.val)
                seen[depth] = True
            
            dfs(node.right, depth+1)
            dfs(node.left, depth+1)
        
        dfs(root, 0)
        return sol