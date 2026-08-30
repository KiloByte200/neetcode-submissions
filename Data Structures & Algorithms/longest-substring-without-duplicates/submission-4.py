class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        longestSubStr = 1
        last = {s[0]: 0}

        left = 0
        right = 1

        while right < len(s):

            c = s[right]

            if c in last:
                left = max(left, last[c] + 1)

            last[c] = right
            right +=1

            longestSubStr = max(longestSubStr, right - left)
        return longestSubStr