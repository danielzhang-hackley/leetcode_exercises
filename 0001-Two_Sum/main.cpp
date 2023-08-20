#include <iostream>
#include <string>
#include <vector>

using namespace std;


void printArray(vector<int> & arr){
    for(int i = 0; i < arr.size(); i++){
        cout << arr[i] << " ";
    }
    cout << "\n";
}


vector<int> merge(vector<int>& arr1, vector<int>& arr2){
    vector<int> out;

    int i = 0;
    int j = 0;

    int k = 0;
    while(i < arr1.size() && j < arr2.size()){
        if(arr1[i] < arr2[j]){
            out.push_back(arr1[i]);
            i++;
        }
        else{
            out.push_back(arr2[j]);
            j++;
        }
    }

    if(i >= arr1.size())
        out.insert(out.end(), arr2.begin() + j, arr2.end());

    if(j >= arr2.size())
        out.insert(out.end(), arr1.begin() + i, arr1.end());

    return out;
}


vector<int> mergeSort(vector<int>& arr){
    if(arr.size() == 1)
        return arr;

    vector<int> arr1 = vector<int>(arr.begin(), arr.begin() + arr.size() / 2);
    vector<int> arr2 = vector<int>(arr.begin() + arr.size() / 2, arr.end());

    arr1 = mergeSort(arr1);
    arr2 = mergeSort(arr2);

    return merge(arr1, arr2);
}


class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target){
        vector<int> nums_s = mergeSort(nums);
        int i = 0;
        int j = nums_s.size() - 1;

        while(i < j){
            if(nums_s[i] + nums_s[j] < target)
                i++;
            else if(nums_s[i] + nums_s[j] > target)
                j--;
            else{
                vector<int> sum_idx_s = vector<int> {i, j};
                vector<int> sum_idx;

                bool checked0 = false;
                bool checked1 = false;
                for(int i = 0; i < nums.size(); i++){
                    if((nums[i] == nums_s[sum_idx_s[0]]) && !checked0){
                        sum_idx.push_back(i);
                        checked0 = true;
                    }
                    else if((nums[i] == nums_s[sum_idx_s[1]]) && !checked1){
                        sum_idx.push_back(i);
                        checked1 = true;
                    }
                }

                return sum_idx;
            }
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