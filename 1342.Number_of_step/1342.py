https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/

class Solution:
    def numberOfSteps (self, num: int) -> int:
        cnt = 0
        while num != 0:
            cnt += 1
            if num % 2 == 0:
                num = num // 2
            elif num % 2 != 0:
                num -= 1
        return cnt