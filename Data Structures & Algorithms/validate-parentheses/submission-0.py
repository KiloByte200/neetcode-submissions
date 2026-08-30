class Solution:
    def isValid(self, s: str) -> bool:
        counter = {"(" : ")",
                    "{" : "}",
                    "[" : "]"}
        st = []

        for c in s:
            if c in counter:
                st.append(c)
            else:
                if not st or counter[st[-1]] != c:
                    return False
                st.pop()

        
        return not st
            
            

        