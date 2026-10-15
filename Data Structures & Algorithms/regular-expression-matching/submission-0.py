class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        ns = len(s)
        np = len(p)

        memo = {}

        def matching(index_s: int, index_p: int) -> bool:
            if ns == index_s and np == index_p:
                return True
            
            if np == index_p:
                return False
            
            if (index_s, index_p) in memo:
                return memo[(index_s, index_p)]
            
            result = False

            # if p at index_p contains a *, compare index_p-1 to index_s 
            # true : try two paths
            #     1. increment index_s
            #     2. decrement index_p

            first_match = (
                index_s < ns
                and (s[index_s] == p[index_p] or p[index_p] == ".")
            )

            if index_p+1 < np and p[index_p+1] == "*":

                # using 0 of p[index_p]
                result = result or matching(index_s, index_p+2)

                # using 1+ of p[index_p]
                if first_match:
                    result = result or matching(index_s+1, index_p)

            elif first_match:
                # if index_s and index_p at s and p match or p is a ., increment both indexes one forward
                result = result or matching(index_s+1, index_p+1)
            
            # return tru if any of these paths return true
            memo[(index_s, index_p)] = result
            return memo[(index_s, index_p)]
        
        return matching(0,0)
        