from typing import List

"""
1 2 3 4

2 1 3 4

3 1 2 4
3 2 1 4
1 3 2 4
2 3 1 4

4 1 2 3
4 2 1 3
4 3 1 2
4 3 2 1
4 1 3 2
4 2 3 1


"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [nums]
        # i is the idx of the element we will move around
        for i in range(len(nums)):
            perms_new = []
            for perm in perms:
                perm_temp = perm[:i] + perm[i+1:]
                for j in range(i):
                    perms_new.append(perm_temp[:j] + [nums[i]] + perm_temp[j:])
            perms.extend(perms_new)
        return perms
    
print('\033c')
print(Solution().permute([1, 2, 3]))