from typing import List
from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        ans_dict = defaultdict(set)

        while accounts:
            account = accounts.pop()
            ans_dict[account[0]] = ans_dict[account[0]] | set(account[1:])


        return [[name] + sorted(list(ans_dict[name])) for name in ans_dict]