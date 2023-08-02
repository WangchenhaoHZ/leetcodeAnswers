from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        for i in range(1, len(s)):
            for j in range(i+1, len(s)):
                for k in range (j+1, len(s)):
                    a = s[:i]
                    b = s[i:j]
                    c = s[j:k]
                    d = s[k:]
                    if (len(a)>1) and (a[0] == '0') or\
                        (len(b)>1) and (b[0] == '0') or\
                        (len(c)>1) and (c[0] == '0') or\
                        (len(d)>1) and (d[0] == '0'):
                        continue
                    if  ((0 <= int(a)) and (int(a) <= 255) and\
                        (0 <= int(b)) and (int(b) <= 255) and\
                        (0 <= int(c)) and (int(c) <= 255) and\
                        (0 <= int(d)) and (int(d) <= 255)):
                        ans.append("{}.{}.{}.{}".format(a,b,c,d))
        return ans

print(
    Solution().restoreIpAddresses(
        "101023"
    )
)