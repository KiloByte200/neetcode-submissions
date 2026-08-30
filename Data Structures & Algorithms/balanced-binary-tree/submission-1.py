# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def depth(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            
            left_height = depth(node.left)
            right_height = depth(node.right)

            if left_height == -1 or right_height == -1:
                return -1
            
            if abs(left_height-right_height) > 1:
                return -1

            return 1 + max(left_height, right_height)
    
        return depth(root) != -1