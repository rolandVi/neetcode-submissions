# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        self.sol = True
        
        def min_max_of_children(node: TreeNode) -> List[int]:
            if not self.sol:
                return [0, 0]
            value = node.val
            min_l, max_l, min_r, max_r = value, value, value, value
            if node.left is not None:
                min_l, max_l = min_max_of_children(node.left)
                if max_l >= value:
                    self.sol = False
            
            if node.right is not None:
                min_r, max_r = min_max_of_children(node.right)
                if min_r <= value:
                    self.sol = False
            
            return [min_l, max_r]

        min_max_of_children(root)
        return self.sol
        
        



