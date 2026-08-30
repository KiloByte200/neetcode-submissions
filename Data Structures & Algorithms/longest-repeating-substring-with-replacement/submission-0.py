from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int)
        max_freq = 0
        start, end = 0, 0
        n = len(s)

        while end < n:
            counts[s[end]] += 1
            if k < (end-start+1) - max(counts.values()):
                counts[s[start]] -= 1
                start += 1
            else:
                max_freq = max(max_freq, end - start + 1)
            end += 1
        return max_freq
        