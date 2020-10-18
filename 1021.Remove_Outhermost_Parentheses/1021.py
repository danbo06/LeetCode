https://leetcode.com/problems/remove-outermost-parentheses/

class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        ans = []
        cnt = 0
        i = 0
        for j in range(len(S)):
            if S[j] == "(":
                cnt += 1
            else:
                cnt -= 1
            if cnt == 0:
                ans.append(S[i + 1 :j])
                i = j + 1
        return "".join(ans)