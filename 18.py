class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = list()
        nums_len = len(nums)
        nums.sort()
        
        for i in range(nums_len - 3):
            if (nums[i] << 2) > target: # prune最小的数的 4 倍大于 target，剪枝操作
                break
            if i > 0 and nums[i - 1] == nums[i]:
                continue
                
            for j in range(nums_len-1, i+2, -1):
                if (nums[j] << 2) < target: # prune 最大的数的 4 倍小于 target，剪枝操作
                    break
                if j < nums_len-1 and nums[j] == nums[j + 1] :
                    continue
                    
                l, r = i+1, j-1                
                while l < r:
                    if nums[i] + nums[j] + nums[l] + nums[r] == target:
                        result.append([nums[i], nums[j], nums[l], nums[r]])
                        while l < r and nums[l] == nums[l + 1]:
                            l += 1
                        while l < r and nums[r] == nums[r - 1]:
                            r -= 1
                        l += 1
                        r -= 1
                    elif nums[i] + nums[j] + nums[l] + nums[r] < target:
                        l += 1
                    else:
                        r -= 1 
        return result
