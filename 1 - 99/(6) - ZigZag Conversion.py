# 44 ms
class Solution:
    def convert(self, s:str, numRows: int) -> str:

        n = len(s)
        
        if numRows == 1:
            return s
        else:
            rows = ["" for i in range(numRows)]
            count = 0
            row = 0
            while count<n:
                if row == numRows-1:
                    while row > 0 and count<n:
                        rows[row] += s[count]
                        count += 1
                        row -= 1
                else:
                    rows[row] += s[count]
                    count += 1
                    row += 1

            ans = ""
            for row in rows:
                ans += row
            return ans

    def convert2(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        n = len(s)
        ans = ""
        maxDiffBetweenChars = (numRows-1)*2

        for i in range(numRows):

            positionsOffset = (maxDiffBetweenChars - i*2, i*2)
            if positionsOffset[0] == 0:
                positionsOffset = (positionsOffset[1],positionsOffset[1])
            elif positionsOffset[1] == 0:
                positionsOffset = (positionsOffset[0],positionsOffset[0])

            currentPosition = i
            switch = False

            while currentPosition < n:
                if switch == False:
                    if currentPosition < n:
                        ans += s[currentPosition]
                        currentPosition += positionsOffset[0]
                        switch = True
                else: # switch == True
                    if currentPosition < n:
                        ans += s[currentPosition]
                        currentPosition += positionsOffset[1]
                        switch = False
        return ans

print(Solution.convert(Solution, "PAYPALISHIRING", 3))
print(Solution.convert(Solution, "PAYPALISHIRING", 4))
print(Solution.convert(Solution, "A", 1))

print(Solution.convert2(Solution, "PAYPALISHIRING", 3))
print(Solution.convert2(Solution, "PAYPALISHIRING", 4))
print(Solution.convert2(Solution, "A", 1))
