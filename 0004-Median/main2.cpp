#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2){
        bool isEven = (nums1.size() + nums2.size()) % 2 == 0;
        vector<int> arr;

        int idx1 = 0;
        int idx2 = 0;

        auto iter1 = nums1.begin();
        auto iter2 = nums2.begin();

        bool added = false;

        printf("here\n");

        for (iter1; iter1 != nums1.end(); ++iter1){
            printf("here for 1\n");
            for (iter2; iter2 != nums2.end(); ++iter2){
                printf("here for 2\n");
                if (*iter2 < *iter1){
                    printf("here if\n");
                    arr.push_back(*iter2);
                    added = true;
                }
                else{
                    printf("here else\n");
                    arr.push_back(*iter1);
                    added = true;
                    break;
                }
            }
            if (!added)
                arr.push_back(*iter1);
            added = false;
        }


        return arr[arr.size()-1];
    }
};

int main(){
    cout << "\033[H\033[J";
    Solution solution = Solution();
    vector<int> nums1 = {1, 3};
    vector<int> nums2 = {2};
    double x = solution.findMedianSortedArrays(nums1, nums2);

    cout << x;
}