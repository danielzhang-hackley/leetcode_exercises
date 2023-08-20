from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sums = {}  # key is sums, values is list of pairs of indices
        ans = []
        for i, num1 in enumerate(nums[:-1]):
            if -num1 in sums:
                for pair in sums[-num1]:
                    ans.append(pair + [(num1, i)])
            for j, num2 in enumerate(nums[i+1:], start=i+1):
                if num1 + num2 in sums:
                    sums[num1 + num2].append([(num1, i), (num2, j)])
                else:
                    sums[num1 + num2] = [[(num1, i), (num2, j)]]

        print(sums)
        print()
        return list(ans)
    

print('\033c')
solution = Solution()
print(solution.threeSum([-1,0,1,2,-1,-4]))
print('\n\n')
print(solution.threeSum([-2, 0, 2]))