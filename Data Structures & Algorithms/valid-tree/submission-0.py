class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_list = [[] for _ in range(n)]

        for node1, node2, in edges:
            adj_list[node1].append(node2)
            adj_list[node2].append(node1)

        visited = set()

        def dfs(parent: int, node: int) -> bool:
            if node in visited:
                return False

            visited.add(node)
            
            for new_node in adj_list[node]:
                if new_node == parent:
                    continue
                
                if not dfs(node, new_node):
                    return False
                
            return True
        
        if not dfs(-1, 0):
            return False
        
        return len(visited) == n
        