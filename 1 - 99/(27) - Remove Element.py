class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        p2 = 0
        k = 0
        n = len(nums)
        
        for p1, number in enumerate(nums, start=0):
            if number == val:
                p2 = p1
                while p2 < n and nums[p2] == val:
                    p2 += 1
                else:
                    if p2 == n:
                        break
                    nums[p1] = nums[p2]
                    nums[p2] = val
                    k += 1
            else: 
                k += 1

        return k

print(Solution.removeElement(Solution, nums = [0,1,2,2,3,0,4,2], val = 2))