class Solution:
    def tribonacci(self, n: int) -> int:
        def inner(i):
            if i == 0:
                return 0
            res = memo[i]
            if res != 0:
                return res
            res = inner(i - 1) + inner(i - 2) + inner(i - 3)
            memo[i] = res
            return res
        memo = [0] * (n + 1)
        if n > 0:
            memo[1] = 1
        if n > 1:
            memo[2] = 1
        return inner(n)


sol = Solution()
print(sol.tribonacci(0))
