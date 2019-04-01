#
# @lc app=leetcode.cn id=283 lang=python
#
# [283] 移动零
#
# https://leetcode-cn.com/problems/move-zeroes/description/
#
# algorithms
# Easy (53.14%)
# Total Accepted:    39.7K
# Total Submissions: 74.6K
# Testcase Example:  '[0,1,0,3,12]'
#
# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
# 
# 示例:
# 
# 输入: [0,1,0,3,12]
# 输出: [1,3,12,0,0]
# 
# 说明:
# 
# 
# 必须在原数组上操作，不能拷贝额外的数组。
# 尽量减少操作次数。
# 
# 
#
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        total = len(nums)
        none_zero = 0
        for i in nums:
            if i == 0:
                continue
            nums[none_zero] = i
            none_zero += 1
        
        for i in range(none_zero, total, 1):
            nums[i] = 0

# s = Solution()
# print(s.moveZeroes([0,1,2,2,3,0,4,2]))


