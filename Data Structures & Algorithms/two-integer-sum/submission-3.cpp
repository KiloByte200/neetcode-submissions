#include <unordered_map>

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        // hashset with value : index relationship
        std::unordered_map<int, int> mem;

        for (int i = 0; i < nums.size(); i++){
            int cand = target - nums[i];
            if (mem.contains(cand)){
                return {mem[cand], i};
            }
            mem[nums[i]] = i;
        }

    }
};
