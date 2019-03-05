# def lengthOfLongestSubstring(s):
#     # 第一种 滑动窗口法
#     ans = 0
#     tmp = 0
#     N = len(s)
#     if N == 0:      # 如果字符串为空  返回0
#         return 0
#     # if N == 1:      # 如果字符串长度为1  返回1
#     #     return 1
#     hashset = {}
#     for i in range(N):
#         for j in range(i, N):
#             if s[j] not in hashset:
#                 hashset[s[j]] = 1
#                 tmp = j - i + 1
#             else:
#                 tmp = j - i
#                 break
#         if tmp > ans:
#             ans = tmp
#         hashset = {}
#     # if ans == 0:    # 如果字符串无重复  则输出字符串原本长度
#     #     ans = N
#     return ans

#     # 第二种 优化的滑动窗口
#     N = len(s)
#     if N == 0:
#         return 0
#     if N == 1:
#         return 1
#     ans = 0
#     tmp = 0
#     hashmap = {}
#     temp = 0
#     for i in range(N):
#         temp = i
#         for j in range(i, N):
#             if s[j] not in hashmap:
#                 hashmap[s[j]] = 1
#                 tmp = j - temp + 1
#                 i = j
#             else:
#                 tmp = j - temp
#                 i = j + 1
#                 break
#         if tmp > ans:
#             ans = tmp
#         hashmap = {}
#     return ans

def lengthOfLongestSubstring(s):
    curr = []
    maxlen = 0
    for c in s:
        if c in curr:
            index = curr.index(c)
            curr = curr[index + 1:]
            curr.append(c)
        else:
            curr.append(c)
            currlen = len(curr)
            if currlen > maxlen:
                maxlen = currlen
    return maxlen  


num = lengthOfLongestSubstring('abcabcbb')
print(num, 'true: 3')

num = lengthOfLongestSubstring('pwwke')
print(num, 'true: 3')

num = lengthOfLongestSubstring('aabcd')
print(num, 'true: 4')

num = lengthOfLongestSubstring('')
print(num, 'true: 0')

num = lengthOfLongestSubstring(' ')
print(num, 'true: 1')