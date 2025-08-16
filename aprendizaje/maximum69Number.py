class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        num_str = str(num)
        
        for i in range(4):
            if num == 9:
                return num
            else:
                if '6' in num_str[i:]:
                    num = int(num_str.replace('6', '9', 1))
        return num
print(Solution().maximum69Number(9669))  # Output: 9969