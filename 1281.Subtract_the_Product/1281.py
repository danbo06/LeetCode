https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod, sum = 1, 0
        n_str = str(n)
        for i in range(len(n_str)):
            prod *= int(n_str[i])
            sum += int(n_str[i])
        return prod - sum