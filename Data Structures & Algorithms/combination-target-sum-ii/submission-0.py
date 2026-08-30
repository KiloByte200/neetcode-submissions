class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()
        result = []
        current = []

        def backtracking(start: int, remaining: int) -> None:
            
            if remaining == 0:
                result.append(current.copy())
                return


            for index in range(start, len(candidates)):
                candidate = candidates[index]

                # skip duplicates
                if index > start and candidate == candidates[index-1]:
                    continue
                
                if candidate > remaining:
                    break
                
                current.append(candidate)

                backtracking(index + 1, remaining - candidate)

                current.pop()


        backtracking(0, target)
        return result
        