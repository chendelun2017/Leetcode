class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        a = [0] * 60
        ans = 0
        for i in time:
            a[i%60] += 1
        for j in range(1,30):
            ans += a[j] * a[60 - j]
        ans += a[0] * (a[0] - 1)//2 + a[30] * (a[30] - 1)//2
        return ans


s = Solution()
print(s.numPairsDivisibleBy60([30,20,150,100,40]))

