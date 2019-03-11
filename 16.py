class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ans = []
        l, r, dif, temp, ans_1 = 0, 0, 0, 65536, 65536
        N = len(nums)
        if N <= 3:
            return sum(nums)
        nums.sort()

        for i in range(N - 2):
            l = i + 1
            r = N - 1

            while l < r:
                dif = target - nums[i] - nums[l] - nums[r]
                if dif < temp:
                    temp = dif
                    ans = nums[i]+nums[l]+nums[r]
                if dif > 0:
                    l += 1
                elif dif < 0:
                    r -= 1
                    dif = -dif
                else:
                    return target
            if ans_1 >= ans:
                ans_1 = ans
        return ans_1


s = Solution()
print(s.threeSumClosest([1,1,1,0], -100), 'True: 2')