
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        # check roots both exist
        # return if false

        # Create 2 queue/stack (1 for each tree)- choosing BFS or DFS doesn't change time complexity here 
        # since we search the whole tree worst case anyways

        # add roots to respective trees

        # while stack:
        # pop from stack
        # Check values are the same return if not
        # push left node and right node

        # if traversed the whole tree return true

        st_1 = [p]
        st_2 = [q]

        while st_1 and st_2:
            node_1 = st_1.pop()
            node_2 = st_2.pop()

            if not node_1 and not node_2:
                continue
            
            if not node_1 or not node_2:
                return False

            if node_1.val != node_2.val:
                return False
            
            st_1.append(node_1.left)
            st_1.append(node_1.right)

            st_2.append(node_2.left)
            st_2.append(node_2.right)

        return len(st_1) == len(st_2)




        
        