class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        connections = {}

        def find(node: int) -> int:
            if node not in connections:
                connections[node] = node

            while node != connections[node]:
                connections[node] = connections[connections[node]]
                node = connections[node]
            return node


        for edge1, edge2 in edges:
            root1 = find(edge1)
            root2 = find(edge2)

            if root1 == root2:
                return [edge1, edge2]

            connections[root2] = root1
        
        return [0, 0]