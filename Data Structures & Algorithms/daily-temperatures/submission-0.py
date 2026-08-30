class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):

            while st and temperatures[st[-1]] < temperatures[i]:
                cand = st.pop()
                res[cand] = i - cand
            
            st.append(i)
        
        return res
        