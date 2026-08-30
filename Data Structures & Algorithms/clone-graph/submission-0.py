"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
                return None
        old_to_new = {}

        def dfs(current):
            # Already cloned?
            if current in old_to_new:
                return old_to_new[current]

            # Create and store clone
            old_to_new[current] = Node(current.val)

            # Clone every neighbor
            for neighbor in current.neighbors:
                old_to_new[current].neighbors.append(dfs(neighbor))

            # Return clone
            return old_to_new[current]
        
        return dfs(node)