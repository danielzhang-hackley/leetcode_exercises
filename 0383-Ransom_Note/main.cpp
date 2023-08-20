#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution{
    public:
        bool canConstruct(string ransomNote, string magazine){
            int magazineCounts[26] = {0};
            int ransomNoteCounts[26] = {0};

            for (char character: magazine){
                magazineCounts[(int) character - 97]++;
            }

            for (char character: ransomNote){
                int idx = (int) character - 97;
                ransomNoteCounts[idx]++;
                if (ransomNoteCounts[idx] > magazineCounts[idx]){
                    return false;
                }
            }

            return true;
        }
};



int main(){
    cout << "\033[H\033[J";
    // Solution solution = Solution();
    // bool x = solution.canConstruct("abbb", "aabbb");

    // cout << x;

    vector<int> x = {1, 2, 3, 4, 5};
    vector<int> v2 = vector<int>(x.begin() + 1, x.begin() + 3);

    for(int i = 0; i < v2.size(); i++){
        cout << v2[i] << " ";
    }

    return 0;
}