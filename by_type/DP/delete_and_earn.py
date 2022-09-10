from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        nums.sort()
        nums_mult = []
        nums_dict = {}
        for i in nums:
            if nums_dict.get(i) is not None:
                nums_dict[i] += 1
            else:
                nums_mult.append(i)
                nums_dict[i] = 1

        def inner(i):
            if i == -1:
                return inner()
            num = nums_mult.pop()
        memo = {}
        return inner(-1)


sol = Solution()
print(sol.deleteAndEarn())
