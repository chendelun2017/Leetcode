class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        dict = {}
        count = 0
        for index,string in enumerate(J):
            dict[index] = string
        for i in S:
            if i in dict:
                count += 1
                
        return count

if __
count = Solution.numJewelsInStones(["aA"], ["aAAbbb"])