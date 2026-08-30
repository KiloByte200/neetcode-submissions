class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for word in strs:
            result += str(len(word)) + "#" + word
        return result

    def decode(self, s: str) -> List[str]:
        i = 0
        result = []
        while i < len(s):
            cand = s[i:i+s[i:].find("#")]
            length = int(cand)
            i += len(cand) + 1
            
            result.append(s[i: i + length])
            i+= + length
        return result