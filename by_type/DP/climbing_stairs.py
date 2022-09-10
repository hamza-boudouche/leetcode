class Solution:
    solutions = [0, 1, 2]

    def climbStairs(self, n: int) -> int:
        if len(self.solutions) < n + 1:
            self.solutions = [-1 for i in range(n + 1)]
            for i in range(3):
                self.solutions[i] = i
        if self.solutions[n] == -1:
            self.solutions[n] = self.climbStairs(
                n - 1) + self.climbStairs(n - 2)
            return self.solutions[n]
        return self.solutions[n]

# include everything in the function itself
# memoization
# use dict instead of list for more ease
# complexity analysis
# bottom up and top down solution


sol = Solution()
print(sol.climbStairs(50))


"""
in: 3
sol = [0, 1, 2, -1]
2 + 1 = 3

"""
