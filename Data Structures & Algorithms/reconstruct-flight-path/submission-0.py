from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Create adjacency list that is easily popable:
        # "JFK": maybe a heap that is sortable by lexicographical values
        #
        # dfs where ticket values from the adjacency list are popped when used and put back if the dfs path is not fit
        # the base condition would be if there are no more values in the adj list which means we used all tickets for our path
        # wondering if before we go one level of recursion deep we add the popped airline path to a results array and if the path doesn't work out we pop it, wonder how efficient that would be
        
        adj_list = defaultdict(list)
        for edge1, edge2 in tickets:
            adj_list[edge1].append(edge2)
        
        for key in adj_list.keys():
            adj_list[key].sort(reverse=True)

        result = []

        def eulerian(ticket: str) -> None:
            while adj_list[ticket]:
                path = adj_list[ticket].pop()
                eulerian(path)
            
            result.append(ticket)
        
        eulerian("JFK")

        return result[::-1]

