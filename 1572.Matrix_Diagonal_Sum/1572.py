https://leetcode.com/problems/matrix-diagonal-sum/

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        ans = 0
        if n % 2 == 1:
            ans -= mat[n // 2][n // 2]
        else:
            ans = 0
        for i in range(n):
            ans += mat[i][i] + mat[i][n - 1 - i]
        return ans