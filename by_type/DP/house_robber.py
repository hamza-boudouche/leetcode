"""
[1, 2, 3, 1]
[0, 0, 0, 0]

def rob(robbed = []):
	if len(robbed) == 0:
		return max(rob([0]), rob([1]))
	if robbed[len(robbed) - 1] == 0:
		return max(rob(robbed.append(0)), rob(robbed.append(1)))
	return rob(robbed.append(0))

"""

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        def inner(i):
            res = memo.get(i)
            if res is not None:
                return res
            if i == 0:
                return nums[0]
            elif i == 1:
                return max(nums[0], nums[1])
            memo[i] = max(inner(i - 1), inner(i - 2) + nums[i])
            return memo[i]
        memo = {}
        return inner(len(nums) - 1)


sol = Solution()
print(sol.rob([2, 7, 9, 3, 1]))
