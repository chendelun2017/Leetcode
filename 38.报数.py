#
# @lc app=leetcode.cn id=38 lang=python
#
# [38] 报数
#
# https://leetcode-cn.com/problems/count-and-say/description/
#
# algorithms
# Easy (48.65%)
# Total Accepted:    25.5K
# Total Submissions: 52.3K
# Testcase Example:  '1'
#
# 报数序列是一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。其前五项如下：
# 
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 
# 
# 1 被读作  "one 1"  ("一个一") , 即 11。
# 11 被读作 "two 1s" ("两个一"）, 即 21。
# 21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。
# 
# 给定一个正整数 n（1 ≤ n ≤ 30），输出报数序列的第 n 项。
# 
# 注意：整数顺序将表示为一个字符串。
# 
# 
# 
# 示例 1:
# 
# 输入: 1
# 输出: "1"
# 
# 
# 示例 2:
# 
# 输入: 4
# 输出: "1211"
# 
# 
#
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 0:
            return ''
        
        res = '1'
        while n != 1:
            res_len, i = len(res), 1
            tmp = ''
            while i <= res_len:
                count = 1
                while i < res_len and res[i] == res[i-1]:
                    count += 1
                    i += 1
                tmp += str(count) + str(res[i-1])
                i += 1
            res = tmp
            n -= 1
            
        return res     

# s = Solution()
# print(s.countAndSay(5))
# print(s.countAndSay(4))
# print(s.countAndSay(3))
# print(s.countAndSay(2))
# print(s.countAndSay(1))

