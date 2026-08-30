class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []

        digits_comb = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }

        result = [""]
        curr = []

        for digit in digits:
                for entry in result:
                    for letter in digits_comb[digit]:
                        curr.append(entry+letter)
                result = curr.copy()
                curr = []
        
        return result
            

            




        