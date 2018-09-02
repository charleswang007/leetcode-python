# -*- coding:utf-8 -*-


# Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.
#
# Example 1:
#
#
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# Output: true
#
#
# Example 2:
#
#
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
# Output: false
#
#

class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        
        r, c, l = len(s1), len(s2), len(s3)
        if r + c != l:
            return False
        stack, visited = [(0, 0)], set((0, 0))
        while stack:
            x, y = stack.pop()
            print "x: ", x
            print "y: ", y
            if x + y == l:
                print "CONDITION 1"
                return True
            if x + 1 <= r and s1[x] == s3[x+y] and (x + 1, y) not in visited:
                stack.append((x + 1, y)); visited.add((x + 1, y))
                print "CONDITION 2"
            if y + 1 <= c and s2[y] == s3[x+y] and (x, y + 1) not in visited:
                stack.append((x, y + 1)); visited.add((x, y + 1))
                print "CONDITION 3"
            print "stack: ", stack
            print "visited: ", visited
        return False
        
if __name__ == "__main__":
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    print(Solution().isInterleave(s1, s2, s3))