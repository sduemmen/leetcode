# 524 ms
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        temp = 0
        substring = ""

        length = len(s)
        for i in range(length):
            for j in range(i, length):
                if s[j] not in substring:
                    substring += s[j]
                    temp += 1
                else:
                    substring = ""
                    temp = 0
                    break
                if temp > result:
                    result = temp

        return result

print(Solution.lengthOfLongestSubstring(Solution, "abcabcbb"))
print(Solution.lengthOfLongestSubstring(Solution, "bbbbb"))
print(Solution.lengthOfLongestSubstring(Solution, "pwwkew"))
print(Solution.lengthOfLongestSubstring(Solution, ""))
