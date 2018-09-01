'''
Given an array of integers, every element appears three times except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Runtime: 44 ms 
'''
class Solution(object):
    def singleNumber(self, nums):
        dic = {};
        for i in nums:
            if i not in dic:
               dic[i] = 1;            
            else:  
               dic[i] += 1;
        for i in dic:
            if dic[i] == 1:
               return i;
               
    def singleNumber1(self, nums):
        if len(nums) == 1:
            return nums[0]
        s = sum(set(nums)) * 3
        for n in nums:
            s = s - n
        return s / 2
            
if __name__=="__main__":
    nums = [1,2,1,2,3,3,4,3,1,2]
    print Solution().singleNumber1(nums)             
