# 144 ms
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        n = len(s)

        if n == 1:
            return s
        else:
            stack.append([s[0], 1])

        for i in range(1, n):
            if len(stack) > 0 and s[i] == stack[-1][0]:
                stack[-1][1] += 1
            else:
                stack.append([s[i], 1])

            if stack[-1][1] == k:
                stack.pop()
        
        ans = ""
        for i in range(len(stack)):
            ans = stack[-1][0] * stack[-1][1] + ans
            stack.pop()
        
        return ans

print(Solution.removeDuplicates(Solution, "aaabbcccbcdec", k = 3))
print(Solution.removeDuplicates(Solution, "nnwssswwnvbnnnbbqhhbbbhmmmlllm", 3))
print(Solution.removeDuplicates(Solution, "yfttttfbbbbnnnnffbgffffgbbbbgssssgthyyyy", 4))
