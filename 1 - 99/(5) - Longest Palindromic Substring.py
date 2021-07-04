# 540 ms
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res=""
        size=0
        center = 0
        n=len(s)
        while center<n:
            left = center-1
            right= center+1
            while right<n and s[right]==s[center]:
                right+=1
            while left>=0 and right<n and s[left]==s[right]:
                left-=1
                right+=1
            if right-left-1>size:
                size=right-left-1
                res = s[left+1:right]
            center+=1
        return res
        
print(Solution.longestPalindrome(Solution, "babad"))
print(Solution.longestPalindrome(Solution, "cbbd"))
print(Solution.longestPalindrome(Solution, "a"))
print(Solution.longestPalindrome(Solution, "ac"))
