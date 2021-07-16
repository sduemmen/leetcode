class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        l = len(s)

        if l >= 2:
            i = 0
            while i < l / 2:
                if s[i] == s[-(i+1)]:
                    i += 1
                else:
                    return False
            return True
        else:
            return True

print(Solution.isPalindrome(Solution, 121))
