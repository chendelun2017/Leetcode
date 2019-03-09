class Solution(object):
    def isPalindrome_1(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        l = []
        while x > 0:
            temp = x % 10
            l.append(temp)
            x = int(x / 10)
        N = len(l)
        for i in range(int(N/2)):
            j = N - 1 - i
            if l[i] != l[j]:
                return False
        return True

    def isPalindrome_2(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        y = x
        num = 0
        while y > 0:
            temp = y % 10
            num = num * 10 + temp
            y = int(y/10)
        return True if x == num else False

    def isPalindrome_3(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        y = str(x)
        return True if y == str(x)[::-1] else False