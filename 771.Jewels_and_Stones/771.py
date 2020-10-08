https://leetcode.com/problems/jewels-and-stones/

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        ans = 0
        for i in range(len(J)):
            for j in range(len(S)):
                if J[i] == S[j]:
                    ans += 1
        return ans


def numJewelsInStones(self, J, S):
    return sum(map(J.count, S))