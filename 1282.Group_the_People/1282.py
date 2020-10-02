https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        cnt, ans = collections.defaultdict(list), []
        for i, n in enumerate(groupSizes):
            cnt[n] += [i]
            if len(cnt[n]) == n:
                ans += [cnt[n]]
                cnt[n] = []
        return ans
