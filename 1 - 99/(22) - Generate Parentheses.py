class Solution:
    def generateParentheses(self, n: int) -> list[str]:
        if n == 0:
            return [""]
        ans = []
        for c in range(n):
            for left in self.generateParentheses(self, c):
                for right in self.generateParentheses(self, n-c-1):
                    ans.append("({}){}".format(left, right))
        return ans

print(Solution.generateParentheses(Solution, 3))
