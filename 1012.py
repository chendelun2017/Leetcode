class Solution(object):
    def bitwiseComplement(self, N):
        """
        :type N: int
        :rtype: int
        """
        b = bin(N)[2:]
        ob = ''.join('0' if i == '1' else '1' for i in b)
        return int(ob, 2)


s = Solution()
print(s.bitwiseComplement(10))

