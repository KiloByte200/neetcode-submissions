# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def similar(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

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

        st = [root]

        while st:
            node = st.pop()

            if not node:
                continue

            if similar(node, subRoot):
                return True
            
            st.append(node.left)
            st.append(node.right)

        return False

        