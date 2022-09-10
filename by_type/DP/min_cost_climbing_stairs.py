from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def inner(i):
            if i == 0:
                return cost[0]
            elif i == 1:
                return cost[1]
            if i == len(cost):
                return min(inner(i - 1), inner(i - 2))
            res = memo.get(i)
            if res is not None:
                return res
            memo[i] = min(inner(i - 1), inner(i - 2)) + cost[i]
            return memo[i]
        memo = {}
        return inner(len(cost))


sol = Solution()
print(sol.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))


"""
[10,15,20]

min()

"""
