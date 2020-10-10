https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/

class Solution:
    def numberOfSteps (self, num: int) -> int:
        cnt = 0
        while num != 0:
            if num % 2 == 0:
                num //= 2
            else:
                num -= 1
            cnt += 1
        return cnt

    def numberOfSteps (self, num: int) -> int:
        cnt = 0
        while num > 0:
            cnt += 1 if num % 2 == 0 or num == 1 else 2
            num //= 2
        return cnt

    def numberOfSteps (self, num: int) -> int:
        s = bin(num)[2 :]
        return s.count('1') + len(s) - 1

