https://leetcode.com/problems/count-number-of-teams/

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        return self.team_count(rating) + self.team_count(rating[::-1])

    def team_count(self, rating):
        ans = 0
        for i in range(len(rating) - 2):
            for j in range(i, len(rating) -1):
                if rating[j] > rating[i]:
                    for k in range(j, len(rating)):
                        if rating[k] > rating[j]:
                            ans += 1
        return ans


    def numTeams(self, rating: List[int]) -> int:
        res = 0
        for i in range(1, len(rating) - 1):
            less, greater = [0, 0], [0, 0]
            for j in range(i):
                if rating[j] < rating[i]:
                    less[0] += 1
                else:
                    greater[0] += 1
            
            for k in range(i+1, len(rating)):
                if rating[i] < rating[k]:
                    less[1] += 1
                else:
                    greater[1] += 1
            res += less[0] * less[1] + greater[0] * greater[1]
        return res