#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        vector<int> arr1;
        vector<int> arr2;

        if (nums1.empty())
            arr1 = nums2;
        else
            arr1 = nums1;
        if (nums2.empty())
            arr2 = nums1;
        else
            arr2 = nums2;

        int arrSize = arr1.size() + arr2.size();
        bool isOdd = arrSize % 2 != 0;
        int medIdx = arrSize / 2 + 1;

        bool nums1Complete = false;
        bool nums2Complete = false;

        vector<int> arr(medIdx);

        int arr1idx = 0;
        int arr2idx = 0;

        for (int i = 0; i < medIdx; i++){
            if (nums2Complete || (!nums1Complete && arr1[arr1idx] < arr2[arr2idx])){
                arr[i] = arr1[arr1idx];
                arr1idx++;
                if (arr1idx == arr1.size())
                    nums1Complete = true;
            }
            else{
                arr[i] = arr2[arr2idx];
                arr2idx++;
                if (arr2idx == arr2.size())
                    nums2Complete=true;
            }
        }

        if (isOdd)
            return arr[medIdx - 1];
        else
            return ((float) arr[medIdx - 1] + (float) arr[medIdx - 2]) / 2;
    }
};

int main(){
    cout << "\033[H\033[J";
    Solution solution = Solution();
    vector<int> nums1 = {};
    vector<int> nums2 = {1};
    double x = solution.findMedianSortedArrays(nums1, nums2);

    cout << x;
}