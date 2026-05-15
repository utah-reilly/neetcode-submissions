class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> theMap;

        for(int j = 0; j < nums.size(); j++){
            int diff = target - nums[j];
            if(theMap.find(diff) != theMap.end()){
                return {theMap[diff], j};
            }
            theMap.insert({nums[j], j});
        }
        return {};
    }
};
