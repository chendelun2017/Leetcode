class Solution:
    def longestPalindrome_1(self, s):
        """
        :type s: str
        :rtype: str
        """
        k = len(s)
        olist = [0] * k     # 申请长度为n的列表，并初始化
        nList = [0] * k     # 同上
        logestSubStr = ""
        logestLen = 0
 
        for j in range(0, k):
            for i in range(0, j + 1):
                if j - i <= 1:
                    if s[i] == s[j]:
                        nList[i] = 1                # 当 j 时，第 i 个子串为回文子串
                        len_t = j - i + 1
                        if logestLen < len_t:       # 判断长度
                            logestSubStr = s[i:j + 1]
                            logestLen = len_t
                else:
                    if s[i] == s[j] and olist[i+1]:     # 当j-i>1时，判断s[i]是否等于s[j]，并判断当j-1时，第i+1个子串是否为回文子串
                        nList[i] = 1                    # 当 j 时，第 i 个子串为回文子串
                        len_t = j - i + 1
                        if logestLen < len_t:
                            logestSubStr = s[i:j + 1]
                            logestLen = len_t
            olist = nList                   # 覆盖旧的列表
            nList = [0] * k                 # 新的列表清空
        return logestSubStr

    def longestPalindrome(self, s):
    #动态规划：基本思路是对任意字符串，如果头和尾相同，那么它的最长回文子串一定是去头去尾之后的部分的最长回文子串加上头和尾。如果头和尾不同，那么它的最长回文子串是去头的部分的最长回文子串和去尾的部分的最长回文子串的较长的那一个。 
        n = len(s)
        maxl = 0
        start = 0
        for i in range(n):
            if i - maxl >= 1 and s[i-maxl-1: i+1] == s[i-maxl-1: i+1][::-1]:
                start = i - maxl - 1
                maxl += 2
                continue
            if i - maxl >= 0 and s[i-maxl: i+1] == s[i-maxl: i+1][::-1]:
                start = i - maxl
                maxl += 1
        return s[start: start + maxl]

s = Solution()
print(s.longestPalindrome('cbabc'), 'true = cbabc')
print(s.longestPalindrome(''),'true = ')
print(s.longestPalindrome('a'),'true = a')
print(s.longestPalindrome('ac'),'true = a')
print(s.longestPalindrome('abcdea'),'true = a')
print(s.longestPalindrome('bbbb'),'true = bbbb')
