class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        # STARt on right side append -1
        # keep a max record
        # append max and check arr for new max

        result = []
        maxNum = arr[-1]
        result.append(-1)
        for i in range(len(arr)-2, -1, -1):
            result.append(maxNum)
            maxNum = max(maxNum, arr[i])

        return result[::-1]
        