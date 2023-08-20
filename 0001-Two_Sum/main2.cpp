#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>

using namespace std;


void printArray(vector<int> & arr){
    for(int i = 0; i < arr.size(); i++){
        cout << arr[i] << " ";
    }
    cout << "\n";
}


class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target){
        unordered_map<int, int> val_to_idx;

        for(int i = 0; i < nums.size(); i++){
            if(val_to_idx.find(target - nums[i]) == val_to_idx.end())
                val_to_idx[nums[i]] = i;
            else
                return vector<int> {val_to_idx[target - nums[i]], i};
        }

        return vector<int> {-1};
    }

};


int main(){
    Solution solution = Solution();

    vector<int> x = {-1,-2,-3,-4,-5};
    int target = -8;

    vector<int> result = solution.twoSum(x, target);

    printArray(result);

    return 0;
}