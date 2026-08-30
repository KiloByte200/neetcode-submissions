# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pre_index = 0

        def dfs(in_left: int, in_right: int) -> Optional[TreeNode]:
            nonlocal pre_index

            if in_left >= in_right:
                return None
            
            split_val = preorder[pre_index]
            pre_index+=1

            val_found = inorder.index(split_val)

            left_node = dfs(in_left, val_found)
            right_node = dfs(val_found+1, in_right)

            node = TreeNode(split_val, left_node, right_node)
            return node

        return dfs(0, len(inorder))