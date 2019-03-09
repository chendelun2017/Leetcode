class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = len(height)
        maxarea,temp = 0,0
        index_start, index_end = 0, l-1
        while index_start < index_end:       
            if height[index_start] < height[index_end]:
                temp = height[index_start]*(index_end - index_start)
                index_start += 1
            else:
                temp = height[index_end]*(index_end - index_start)
                index_end -= 1
            if temp > maxarea:
                maxarea = temp
        return maxarea

s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))