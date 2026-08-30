# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        def dps(node: TreeNode, max_so_far: int) -> int:
            if not node:
                return 0

            result = 0

            if node.val >= max_so_far:
                result += 1
                max_so_far = node.val
            
            return result + dps(node.left, max_so_far) + dps(node.right, max_so_far)

        return dps(root, root.val)