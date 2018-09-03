"""
Write a program to find the n-th ugly number.
Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12
is the sequence of the first 10 ugly numbers.
Note that 1 is typically treated as an ugly number.
"""

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n + 1)
        dp[1] = 1
        i2 = i3 = i5 = 1
        for i in xrange(2, n + 1):
            dp[i] = min(dp[i2] * 2, dp[i3] * 3, dp[i5] * 5)
            if dp[i] == dp[i2] * 2:
                i2 += 1
            if dp[i] == dp[i3] * 3:
                i3 += 1
            if dp[i] == dp[i5] * 5:
                i5 += 1
        return dp[-1]