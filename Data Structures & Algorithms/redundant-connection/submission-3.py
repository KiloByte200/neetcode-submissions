class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        connections = {}

        def find(node) -> int:
            if node not in connections:
                connections[node] = node

            while node != connections[node]:
                connections[node] = connections[connections[node]]
                node = connections[node]
            return node


        for edge1, edge2 in edges:
            if (find(edge1) == find(edge2)):
                return [edge1, edge2]

            connections[find(edge2)] = find(edge1)
        
        return [0, 0]