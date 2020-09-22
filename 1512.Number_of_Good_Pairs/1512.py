https://leetcode.com/problems/number-of-good-pairs/

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # This solution is not good
        # ans = 0
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] == nums[j]:
        #             ans += 1
        # return ans

        # O(N) solution
        return sum(i * (i - 1) // 2 for i in collections.Counter(nums).values()) 