from typing import List
from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        def binary_search(arr, x):
            l = 0
            r = len(arr) - 1

            while l <= r:
                m = (l + r + 1) // 2
                if arr[m] == x:
                    return m, True
                if arr[m] > x:
                    r = m-1
                else:
                    l = m+1

            return l, False
        
        graphs = [i for i in range(len(accounts))]
        names = defaultdict(list)  # keys are account names, values are lists of graph values (also idx in accounts)
        subsets = defaultdict(list)  # keys are graph values (also idx in accounts), values are lists of emails
        n_subsets = 0

        for account in accounts:
            any_overlap = False
            # check all the subsets associated with the account name
            for group in names[account[0]]:
                temp = subsets[group][:]
                need_merge = False
                # for each subset, check if any of the account's emails are in the subset
                for email in account[1:]:
                    idx, isin = binary_search(subsets[group], email)
                    if isin:
                        need_merge = True
                        any_overlap = True
                    else:
                        temp.insert(idx, email)
                # merge and modify account to look for others that overlap
                # both with original and merged account
                if need_merge:
                    subsets[group] = temp
                    account = subsets[group][:]
                    del subsets[group]
            # if no emails associated with previous subsets of same name
            if not any_overlap:
                subsets[n_subsets] = sorted([account[1:]])
                names[n_subsets]
                n_subsets += 1

        
        return []