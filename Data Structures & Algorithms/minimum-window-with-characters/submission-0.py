from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        nt = len(t)
        ns = len(s)

        have = 0
        need = 0

        t_freq = defaultdict(int)
        for c in t:
            t_freq[c] += 1
            if t_freq[c] == 1:
                need += 1
        
        s_freq = defaultdict(int)
        for c in s[:nt]:
            s_freq[c] += 1
            if s_freq[c] == t_freq[c]:
                have += 1
        
        if have == need:
            return s[:nt]

        start, end = 0, nt
        candidate = None

        while end < ns:
            c = s[end]
            s_freq[c] += 1

            if c in t_freq and s_freq[c] == t_freq[c]:
                have += 1

            if have == need:
                while have == need:
                    rem_char = s[start]

                    s_freq[rem_char] -= 1

                    if rem_char in t_freq and s_freq[rem_char] < t_freq[rem_char]:
                        have -= 1

                    start += 1

                if not candidate or len(candidate) > len(s[start-1:end+1]):
                    candidate = s[start-1:end+1]
            end += 1

        return candidate or ""

