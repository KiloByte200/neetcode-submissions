# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        # BFS
        # use while loop with internal for loop to skip queue to show each layer of the tree
        # push node.right on the queue first then node.left to get right most elements
        # first element in the queue on each level is the rightmost
        # Add that to list and return list at the end

        if not root:
            return []

        results = []
        queue = deque([root])

        while queue:
            results.append(queue[0].val)

            for _ in range(len(queue)):
                node = queue.popleft()
                
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
            
        
        return results


        