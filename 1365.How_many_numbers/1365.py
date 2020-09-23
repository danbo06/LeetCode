https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution:
    # Brute force
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans_list = []
        for i in range(len(nums)):
            ans = 0
            for j in range(len(nums)):
                if nums[i] != nums[j] and nums[j] < nums[i]:
                    ans += 1
            ans_list.append(ans)
        return ans_list
    
    # Sort
    # Time: O(NlogN)
    # Space: O(N) for output list
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
    dct = {}
    for i, n in enumerate(sorted(nums)):
        if n not in dct:
            dct[n] = i
    return [dct[n] for n in nums]

    # Time: O(N)
    # Space: O(N) for output list
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = [0] * 102
        for num in nums:
            count[num+1] += 1
        for i in range(1, 102):
            count[i] += count[i-1]
        return [count[num] for num in nums]

    