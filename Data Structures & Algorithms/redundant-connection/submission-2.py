class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        connections = {}

        def find(node) -> int:
            while node in connections and node != connections[node]:
                node = connections[node]
            return node



        result = [0,0]

        for edge1, edge2 in edges:
            if (edge1 in connections and edge2 in connections and
                find(edge1) == find(edge2)):
                result = [edge1, edge2]

            if edge1 not in connections:
                connections[edge1] = edge1
            connections[find(edge2)] = find(edge1)
        
        return result