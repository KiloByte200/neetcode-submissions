class Solution:
    def countSubstrings(self, s: str) -> int:

        n = len(s)
        count = 0

        for i in range(n):

            left = right = i

            while left >= 0 and right < n:
                if s[right] != s[left]:
                    break

                count += 1
                left -= 1
                right += 1

            left = i - 1
            right = i

            while left >= 0 and right < n:
                if s[right] != s[left]:
                    break

                count += 1
                left -= 1
                right += 1

        return count

        