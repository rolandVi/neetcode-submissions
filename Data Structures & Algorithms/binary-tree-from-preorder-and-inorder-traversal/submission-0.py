# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def build(pre_l: int, pre_r: int, in_l: int, in_r: int) -> TreeNode:
            top_node = preorder[pre_l]

            in_top = -1
            for i in range(in_l, in_r + 1):
                if inorder[i] == top_node:
                    in_top = i
                    break

            left_size = in_top - in_l
            right_size = in_r - in_top
            
            left_child = build(pre_l+1, pre_l+left_size, in_l, in_top - 1) if left_size > 0 else None
            right_child = build(pre_l+left_size+1, pre_r, in_top + 1, in_r) if right_size > 0 else None
            return TreeNode(top_node, left_child, right_child)

        return build(0, len(preorder)-1, 0, len(inorder) - 1)
