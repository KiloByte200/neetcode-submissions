class Solution:

    def encode(self, strs: List[str]) -> str:
        parts = [] 
        for word in strs:
            parts.append(str(len(word)) + "#" + word)
        return ''.join(parts)

    def decode(self, s: str) -> List[str]:
        i = 0
        result = []

        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1

            length = int(s[i:j])
            i = j + 1

            result.append(s[i:i + length])
            i+= length
        return result