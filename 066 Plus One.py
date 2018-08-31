'''
Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.

Runtime: 44 ms 
'''
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in reversed(xrange(len(digits))):
            print "i: ", i
            print "digit: ", digits[i]
            if digits[i] < 9:
                digits[i] += 1;
                return digits; # return here
            else:
                digits[i] = 0;
        digits.insert(0, 1);
        return digits;
            
if __name__=="__main__":
    digits = [0,1,2,7,9,9,9]
    #digits = [9]
    print Solution().plusOne(digits)
