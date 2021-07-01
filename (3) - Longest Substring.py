# 524 ms	14.4 MB
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
