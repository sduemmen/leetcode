class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        shortest = len(strs[0])
        for s in strs:
            l = len(s)
            if l < shortest:
                shortest = l

        for i in range(shortest):
            char = strs[0][i]
            for s in strs:
                if s[i] != char:
                    if i == 0:
                        return ""
                    else:
                        return strs[0][0:i]

        return strs[0][0:shortest]

print(Solution.longestCommonPrefix(Solution, ["flower","flow","flight"]))
print(Solution.longestCommonPrefix(Solution, ["ab", "a"]))
