from functools import lru_cache
from typing import List


class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        def inner(innums, i):
            if not i < len(multipliers):
                return 0
            if len(innums) == 1:
                return multipliers[i] * innums[0]
            if len(innums) == 2:
                if not i < len(multipliers) - 1:
                    return max(multipliers[i] * innums[0], multipliers[i] * innums[1])
                return max(multipliers[i] * innums[0] + multipliers[i + 1] * innums[1],
                           multipliers[i] * innums[1] + multipliers[i + 1] * innums[0])
            res = memo.get((tuple(innums), i))
            print("-----------------------------------------")
            print("the memo is : ", memo)
            print("i am looking for: ", (tuple(innums), i))
            print("i found it: ", res)
            if res is not None:
                return res
            last = multipliers[i] * innums[-1] + inner(innums[:-1], i + 1)
            first = multipliers[i] * innums[0] + inner(innums[1:], i + 1)
            if first > last:
                innums.pop(0)
                memo[(tuple(innums), i)] = first
                print("-----------------------------------------")
                print("i am inserting the value: ", (tuple(innums), i))
                print("after insertion: ", memo[(tuple(innums), i)])
                return first
            innums.pop(-1)
            memo[(tuple(innums), i)] = last
            print("-----------------------------------------")
            print("i am inserting the value: ", (tuple(innums), i))
            print("after insertion: ", memo[(tuple(innums), i)])
            return last
        memo = {}
        return inner(nums, 0)


sol = Solution()
print(sol.maximumScore([1, 1, 1, 1, 1, 1], [2, 2, 2, 2]))
