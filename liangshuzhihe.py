
def twoSum(nums, target):
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return i,j
        dict = {}
        for index, num in enumerate(nums):
            another_num = target - num
            if another_num in dict:
                return (dict[another_num], index)
            dict[num] = index


[i,j] = twoSum([3,2,4], 6)
print(i,j)

