# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.sol = -1

        def num_of_nodes(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            
            return 1 + num_of_nodes(node.left) + num_of_nodes(node.right)
        
        def dfs(node: Optional[TreeNode], smaller: int) -> None:
            if node is None or self.sol != -1:
                return
            
            smaller_total = smaller + num_of_nodes(node.left)
            larger = num_of_nodes(node.right)

            if k == smaller_total + 1:
                self.sol = node.val
                return
            
            if k <= smaller_total:
                dfs(node.left, smaller)
            else:
                dfs(node.right, smaller_total + 1)
        
        dfs(root, 0)
        return self.sol