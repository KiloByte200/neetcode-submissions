# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        answer = None

        def dfs(node: TreeNode) -> None:
            nonlocal count, answer

            if answer is not None or not node:
                return

            dfs(node.left)

            count += 1
            if count == k:
                answer = node
                return
            
            dfs(node.right)

        dfs(root)
        return answer.val
            
