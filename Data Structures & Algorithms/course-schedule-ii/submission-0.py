from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        requirements = defaultdict(list)
        # requirements dict to map class to requirement []

        for course, prereq in prerequisites:
            requirements[course].append(prereq)


        result = []

        # visiting, and visited sets -> visiting makes sure there's no duplicate, visited to cut on going down same path
        visiting = set()
        visited = set()

        # DFS loop
        # if class already in visiting -> return []
        # if class in visited -> continue
        # prereq = [[1, 0]] -> class 0 req before class 1

        def dfs(course: int) -> bool:
            if course in visiting:
                return False
            if course in visited:
                return True

            visiting.add(course)

            for new_course in requirements[course]:
                if not dfs(new_course):
                    return False
            
            visiting.remove(course)
            visited.add(course)

            result.append(course)
            return True
        
        
        for course in range(numCourses):
            if not dfs(course):
                return []
        return result


        