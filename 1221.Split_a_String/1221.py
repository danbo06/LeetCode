https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ans = 0
        cnt = 0
        for c in s:
            if c == 'L':
                cnt += 1
            else:
                cnt -= 1
            if cnt == 0:
                ans += 1
        return ans