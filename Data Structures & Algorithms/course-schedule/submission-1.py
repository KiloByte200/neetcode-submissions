class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj_list = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            adj_list[course].append(prereq)

        
        visiting = set()
        visited = set()

        def dfs(course: int) -> bool:
            if course in visiting:
                return False

            if course in visited:
                return True 

            visiting.add(course)   

            for prereq in adj_list[course]:
                if not dfs(prereq):
                    return False

            visited.add(course)
            visiting.remove(course) 

            return True
            
            
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True





        