class Solution(object):
    def threeSum_1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums_hash = {}
        ans = []
        for num in nums:
            nums_hash[num] = nums_hash.get(num, 0) + 1
        if  0 in nums_hash and nums_hash[0] >= 3:
            ans.append([0,0,0])

        pos = list(filter(lambda x: x >= 0, nums_hash))
        neg = list(filter(lambda x: x < 0, nums_hash))
                    
        for i in neg:
            for j in pos:
                dif = 0 - i - j
                if dif in nums_hash:
                    if dif in (i, j) and nums_hash[dif] >=2:  # 因为与i,j重复，所以判定nums_hash中 i 或 j 是否出现两次以上是否
                        ans.append([i, j, dif])
                    if dif < i or dif > j:
                        ans.append([i, j, dif])
        return ans

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        N = len(nums)
        if N < 3:
            return ans
        l, r = 0, 0
        nums.sort()
        N = len(nums)
        for i in range(N - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i - 1] == nums[i]:
                continue

            l = i + 1
            r = N - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    ans.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    l +=1
        return ans



    

nums = [-1,0,1,2,-1,4]
s = Solution()
print(s.threeSum(nums))
print(s.threeSum([-2,0,0,2,2]),'true:[[-2,0,2]]')
# nums.sort()
# print(nums)
# nums = sorted(nums)
# print(nums)
# num = set(nums)
# print(list(sorted(set(nums))))

