class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj_matrix = [[] for _ in range(numCourses)]
        for prereq in prerequisites:
            adj_matrix[prereq[0]].append(prereq[1])

        
        visiting = set()
        visited = set()

        def dfs(course: int) -> bool:
            if course in visiting:
                return False
            if course in visited:
                return True 

            visiting.add(course)   

            prereqs = adj_matrix[course]
            for prereq in prereqs:
                if not dfs(prereq):
                    return False

            visited.add(course)
            visiting.remove(course) 
            return True
            
            


        for lst in adj_matrix:
            for course in lst:
                if not dfs(course):
                    return False
        return True





        