https://leetcode.com/problems/count-number-of-teams/

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        ans = 0
        for i in range(len(rating)):
            if i == len(rating) - 1:
                break
            for j in range(i+1, len(rating)):
                for k in range(i+2, len(rating)):
                    if rating[i] < rating[j] < rating[k] or rating[i] > rating[j] > rating[k]:
                        ans += 1
        return ans