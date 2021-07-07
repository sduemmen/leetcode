class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False

        pdict = {"}": "{", ")": "(", "]": "["}
        stack = []
        for char in s:
            if char in ["{", "(", "["]:
                stack.append(char)
            else:
                if len(stack) > 0 and stack[-1] == pdict[char]:
                    stack.pop()
                else:
                    return False

        if len(stack) == 0:
            return True

print(Solution.isValid(Solution, ")"))
print(Solution.isValid(Solution, "()[]{}"))
print(Solution.isValid(Solution, "(]"))
print(Solution.isValid(Solution, "([)]"))
print(Solution.isValid(Solution, "{[]}"))
