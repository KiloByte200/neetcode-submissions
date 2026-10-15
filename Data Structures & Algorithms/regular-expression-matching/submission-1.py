from functools import cache
class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        ns = len(s)
        np = len(p)

        @cache
        def matching(index_s: int, index_p: int) -> bool:      
            if np == index_p:
                return ns == index_s

            # if p at index_p contains a *, compare index_p-1 to index_s 
            # true : try two paths
            #     1. increment index_s
            #     2. decrement index_p

            first_match = (
                index_s < ns
                and (s[index_s] == p[index_p] or p[index_p] == ".")
            )

            if index_p+1 < np and p[index_p+1] == "*":
                # using 0 or 1+ of p[index_p]
                return (matching(index_s, index_p+2) or
                        (first_match and matching(index_s+1, index_p))
                )


            # if index_s and index_p at s and p match or p is a ., increment both indexes one forward
            return (first_match and matching(index_s+1, index_p+1))
        
        return matching(0,0)
        