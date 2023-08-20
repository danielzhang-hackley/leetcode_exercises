from typing import List

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        def binary_search_lead(arr, x):
            l = 0
            r = len(arr) - 1

            while l <= r:
                m = (l + r + 1) // 2
                if arr[m][0] == x:
                    return m
                if arr[m][0] > x:
                    r = m-1
                else:
                    l = m+1

            return r
        
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

        ans = []
        while accounts:
            account = accounts.pop()
            print("account:", account)
            
            if not ans:
                print("ans:", ans)
                ans.append([account[0]] + sorted(account[1:]))
                print("next loop")
                continue

            print("ans:", ans)
            name_idx = binary_search_lead(ans, account[0])
            if ans[name_idx][0] == account[0]:
                one_match = False
                merged_emails = ans[name_idx][1:]
                for email in account[1:]:
                    email_idx, is_in = binary_search(merged_emails, email)
                    if is_in:
                        print(email, "is already in ans at", email_idx)
                        one_match = True
                    else:
                        print(email, "is not already in ans; adding to merged at", email_idx)
                        merged_emails.insert(email_idx, email)
                if one_match:
                    ans[name_idx] = [ans[name_idx][0]] + merged_emails
                # print(merged_emails)
            else:
                print("no emails")
                ans.insert(name_idx, [account[0]] + sorted(account[1:]))

            print('next loop')
        return ans
    
print('\033c')
print(Solution().accountsMerge([["John","johnsmith@mail.com","john_newyork@mail.com"],
                                ["John","johnsmith@mail.com","john00@mail.com"],
                                ["Mary","mary@mail.com"],
                                ["John","johnnybravo@mail.com"]]))