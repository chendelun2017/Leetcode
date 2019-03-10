class Solution(object):
    # zip法
    def longestCommonPrefix_1(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ''
        for i in zip(*strs):
            if len(set(i)) != 1:
                break
            res += i[0]
        return res

    # 两两比较法    
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        res = strs[0]
        for i in range(1,len(strs)):
            tmp = res
            res = ''
            for j in range(min(len(tmp), len(strs[i]))):
                if tmp[j] == strs[i][j]:
                    res += tmp[j]
                else:
                    break
        return res

nums = ['flower','flight','flow']
s = Solution()
print(s.longestCommonPrefix(nums),'true:\'fl\'')
print(s.longestCommonPrefix(['aca','cba']),'true:')
print(s.longestCommonPrefix(''),'true:')

# for i in zip(*nums):
#     print(i)
#     print(len(set(i)))

# for i in zip(nums):
#     print(i)