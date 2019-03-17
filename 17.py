class Solution:
    def letterCombinations_1(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        import itertools
        if not digits:
            return []

        l_map = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', 
                 '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}

        chars = [l_map.get(d) for d in digits]
        return [''.join(x) for x in itertools.product(*chars)]

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        result = []
        if not digits:
            return []
        l_map = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', 
                 '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        chars = [l_map.get(d) for d in digits]

        tmp = [[]]
        for pool in chars:
            tmp = [x + [y] for x in tmp for y in pool]
        for prod in tmp:
            result.append(''.join(prod))
        return result

s = Solution()
print(s.letterCombinations('23'))