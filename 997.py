class Solution(object):
    def findJudge_1(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict
        if not trust:
            return 1
        trust_map = defaultdict(set)
        trust_set = set()
        for it in trust:
            trust_map[it[1]].add(it[0])
            trust_set.add(it[0])
        for key, val in trust_map.items():
            if len(val) == N-1 and key not in trust_set:
                return key
        return -1

    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        count = [0] * (N + 1)
        for i, j in trust:
            count[i] -= 1
            count[j] += 1
        for i in range(1, N+1):
            if count[i] == N-1:
                return i
        return -1


s = Solution()
# print(s.findJudge(4,[[1,3],[1,4],[2,3],[2,4],[4,3]]))
print(s.findJudge(1,[]))