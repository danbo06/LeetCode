https://leetcode.com/problems/decompress-run-length-encoded-list/

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(0, len(nums), 2):
            freq = nums[i]
            val = nums[i+1]
            for j in range(freq):
                ans.append(val)
        return ans