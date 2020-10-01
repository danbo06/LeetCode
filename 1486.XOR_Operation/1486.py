https://leetcode.com/problems/xor-operation-in-an-array/

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = []
        ans = 0
        for n in range(n):
            nums.append(start + n * 2)
        for n in nums:
            ans = ans ^ n
        return ans 

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        
        ans = 0
        nums = [start + n * 2 for n in range(n)]
        
        for n in nums:
            ans = ans ^ n
        return ans 