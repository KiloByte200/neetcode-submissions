# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.invert(root) if root else root
    def invert(self, node: Optional[TreeNode]) -> Optional[TreeNode]:

        leftNode = self.invert(node.left) if node.left else None
        RightNode = self.invert(node.right) if node.right else None 

        node.left = RightNode
        node.right = leftNode
        return node
        