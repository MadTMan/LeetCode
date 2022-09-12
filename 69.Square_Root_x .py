class Solution:
    def mySqrt(self, x: int) -> int:

        #Setting a counter as i to square
        i=1

        #result of squaring stored in result
        result = 0
        if (x == 0):
            return result

        #checking whether the square of a number matches with x
        #The number is the root if it matches
        while i<=x: 
            square = i*i
            if (square == x):
                result = i
                return result
            if (square > x):
                result = i-1
                return result
            else:
                i +=  1
                z

