https://leetcode.com/problems/maximum-69-number/

class Solution:
    def maximum69Number (self, num: int) -> int:
        ans = 0
        list_num = str(num)
        list_num = [s for s in list_num]

        for i in range(len(list_num)):
            if list_num[i] == '6':
                list_num[i] = '9'
                break
        
        return "".join(list_num)

    def maximum69Number(self, num):
        return int(str(num).replace('6', '9', 1))
        