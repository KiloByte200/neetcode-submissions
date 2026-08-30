class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adj_list = [[] for _ in range(n)]
        for node1, node2 in edges:
            adj_list[node1].append(node2)
            adj_list[node2].append(node1)

        visited = set()


        def dfs(parent: int, node:int) -> None:
            if node in visited:
                return
            
            visited.add(node)

            for new_node in adj_list[node]:
                if parent != new_node:
                    dfs(node, new_node)
        
        count = 0
        
        for i in range(len(adj_list)):
            if i not in visited:
                dfs(-1, i)
                count += 1
        
        return count
        