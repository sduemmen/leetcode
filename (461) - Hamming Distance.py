class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ans = 0
        while x > 0 and y > 0:
            if x % 2 != y % 2:
                ans += 1
            x = x >> 1
            y = y >> 1
        else:
            if x == 0:
                while y > 0:
                    if y % 2 == 1:
                        ans += 1
                    y = y >> 1
            else:
                while x > 0:
                    if x % 2 == 1:
                        ans += 1 
                    x = x >> 1
                    
        return ans

print(Solution.hammingDistance(Solution, 1, 4))
print(Solution.hammingDistance(Solution, 3, 1))