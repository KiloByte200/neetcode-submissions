class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for word in strs:
            result += str(len(word)) + "#" + word
        return result

    def decode(self, s: str) -> List[str]:
        i = 0
        result = []
        print(s)
        while i < len(s):
            print(s[i])
            length = int(s[i:i+s[i:].find("#")])
            print(length)
            i += len(str(length)) + 1
            result.append(s[i: i + length])
            i+= + length
        return result