class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == '':
            return ''
        N = len(s)
        if N == 1:
            return s
        for i in range(N):
            j = N - 2
            while j > i:
                if s[j] == s[i]:
                    return s[i:j+1]
                j -= 1
        return s[0]

s = Solution()
print(s.longestPalindrome(''),'true = ')
print(s.longestPalindrome('a'),'true = a')
print(s.longestPalindrome('ac'),'true = a')
print(s.longestPalindrome('abcdea'),'true = a')
print(s.longestPalindrome('bbbb'),'true = b')