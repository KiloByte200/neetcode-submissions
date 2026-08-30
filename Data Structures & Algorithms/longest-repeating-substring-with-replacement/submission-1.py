from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int)
        max_len = 0
        highest_count = 0
        start, end = 0, 0
        n = len(s)

        while end < n:
            counts[s[end]] += 1
            highest_count = max(highest_count, counts[s[end]])

            if (end - start + 1) - highest_count > k:
                counts[s[start]] -= 1
                start += 1

            max_len = max(max_len, end - start + 1)
            end += 1

        return max_len