'''
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example, 
Given s = "Hello World",
return 5.

Runtime: 40 ms
'''
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = ''; 
        for i in s.split(' '):
          if(i != ''):
             count = i;
        return len(count);
    def lengthOfLastWord1(self, s):
        return len(s.split(' ')[-1])
            
if __name__=="__main__":
    s = "Hello World Puppy Wang"
    print Solution().lengthOfLastWord1(s)             
