class Solution(object):
    def reverse_1(self, x):
        """
        :type x: int
        :rtype: int
        """
        num = 0
        reverse = False
        if x < 0:
            reverse = True
            x = -x
        while x >= 10:
            remain = x % 10
            x = x // 10
            num = num * 10 + remain
        num = num * 10 + x
        if num >= 2**31:
            return 0
        if reverse:
            num = -num
        return num

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        output = 0
        flag = -1 if x < 0 else 1
        x = abs(x)
        while x != 0:
            res = x % 10
            x = int(x/10)
            output = output * 10 + res
        if -2**31 < flag * output < 2**31-1:
            return flag * output
        else:
            return 0


s = Solution()
print(s.reverse(12345))
print(s.reverse(-1258774589))