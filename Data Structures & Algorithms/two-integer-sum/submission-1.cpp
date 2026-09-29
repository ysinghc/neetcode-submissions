class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> prevMap;

        for(int i = 0 ; i < nums.size() ; i++)
        {
            int complement = target - nums[i];
            if(prevMap.find(complement) != prevMap.end())
            {
                return {prevMap[complement], i};
            }
            prevMap.insert({nums[i], i});
        }

        return {};
    }
};
