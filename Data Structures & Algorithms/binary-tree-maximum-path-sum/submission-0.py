# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        candidate = float("-inf")
        def dfs(node: TreeNode) -> int:
            if node is None:
                return 0

            nonlocal candidate

            left_gain = max(0, dfs(node.left))
            right_gain = max(0, dfs(node.right))

            candidate = max(candidate, node.val + left_gain + right_gain)

            return node.val + max(left_gain, right_gain)

        dfs(root)
        return candidate

