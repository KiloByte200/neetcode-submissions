class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        curr = []

        def backtracking(open_count: int, close_count: int):
            if len(curr) >= n*2:
                result.append(''.join(curr.copy()))
                return
            
            if open_count < n:
                curr.append("(")
                backtracking(open_count+1, close_count)
                curr.pop()

            if close_count < open_count:
                curr.append(")")
                backtracking(open_count, close_count+1)
                curr.pop()

        backtracking(0, 0)
        return result