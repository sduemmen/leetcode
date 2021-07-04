# 28 ms
class Solution:
    def reverse(self, x: int) -> int:
        # x has one digit
        if 0 <= x <= 9:
            return x
        else:
            negative = True if 0 > x else False
            x = abs(x)
            ans = 0
            nums = []
            # remove zeros at the end. ex: 901000 -> 901
            if x % 10 == 0 and x > 0:
                while x % 10 == 0:
                    x = x // 10

            # get each decimal place of x
            while x > 10:
                nums.append(x % 10)
                x = x // 10
            else:
                nums.append(x % 10)

            # build ans
            n = len(nums)
            decimalPlace = 1
            while n > 0:
                ans += nums[n-1]*decimalPlace
                decimalPlace *= 10
                n -=1

            # x is outside 32bit int range
            if ans > 2**31-1 or ans < -2**31:
                return 0
            else:
                return ans if not negative else -ans

print(Solution.reverse(Solution, 123))
print(Solution.reverse(Solution, -123))
print(Solution.reverse(Solution, 120))
print(Solution.reverse(Solution, 0))
