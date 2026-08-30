class MinStack:

    def __init__(self):
        self.__st = []
        

    def push(self, val: int) -> None:
        if self.__st:
            self.__st.append((val, min(val, self.__st[-1][1])))
        else:
            self.__st.append((val, val))
        

    def pop(self) -> None:
        self.__st.pop()
        

    def top(self) -> int:
        return self.__st[-1][0]
        

    def getMin(self) -> int:
        return self.__st[-1][1]
        
