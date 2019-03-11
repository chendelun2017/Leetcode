class Solution(object):
    def threeSumClosest_1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums_len = len(nums)
        nums.sort()
        best_sum, best_dist = 0, float('inf')

        for i in range(nums_len - 2):
            l, r = i + 1, nums_len - 1
            while l < r:
                tmp_sum = nums[i] + nums[l] + nums[r]
                if abs(tmp_sum - target) < best_dist:
                    best_sum, best_dist = tmp_sum, abs(tmp_sum - target)
                if tmp_sum - target >= 0:
                    r -= 1
                else:
                    l += 1
        return best_sum

    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        result = []
        nums_len = len(nums)
        nums.sort()

        for i, num in enumerate(nums[0:-2]):
            l, r = i + 1, nums_len - 1
            if num + nums[l] + nums[l+1] > target:
                result.append(num + nums[l] + nums[l+1])
            elif num + nums[r] + nums[r-1] < target:
                result.append(num + nums[r] + nums[r-1])
            else:
                while l < r:
                    result.append(num + nums[l] + nums[r])
                    if num + nums[l] + nums[r] > target:
                        r -= 1
                    elif num + nums[l] + nums[r] < target:
                        l += 1
                    else:
                        return target
        result.sort(key = lambda x: abs(x - target))
        return result[0]



s = Solution()
print(s.threeSumClosest([1,1,1,0], -100), 'True: 2')
print(s.threeSumClosest([-1,2,1,-4], 1), 'True: 2')