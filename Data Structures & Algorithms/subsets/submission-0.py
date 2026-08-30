class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def merge(curr_subset: List[List[int]], index: int):
            if index >= len(nums):
                return curr_subset
            
            new_subset = []
            for lst in curr_subset:
                temp = lst + [nums[index]]

                new_subset.append(temp)
            
            new_subset += curr_subset

            return merge(new_subset, index + 1)
            
        return merge([[]], 0)
        