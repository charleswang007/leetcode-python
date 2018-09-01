"""
Given a non-empty array of integers, return the k most frequent elements.
For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].
Note:
You may assume k is always valid, 1 <= k <= number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""

from collections import defaultdict
import heapq

class Counter(object):
    def __init__(self, val, cnt):
        self.val = val
        self.cnt = cnt

    def __cmp__(self, other):
        return self.cnt - other.cnt


class Solution(object):
    def topKFrequent1(self, nums, K):
        """
        Count and Maintain a heap with size k -> O(n lg k)
        Since python heapq does not support cmp, need to wrap data in a struct
        Need to use min heap instead of max heap, since we need to pop the minimal one
        :type nums: List[int]
        :type K: int
        :rtype: List[int]
        """
        cnt = defaultdict(int)
        for e in nums:
            cnt[e] += 1

        lst = []
        for k, v in cnt.items():
            lst.append(Counter(k, v))

        ret = []
        for elt in lst:
            if len(ret) < K:
                heapq.heappush(ret, elt)
            else:
                heapq.heappushpop(ret, elt)

        return map(lambda x: x.val, ret)
        
    def topKFrequent2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = {} # or d = defaultdict(int)
        res = []
        ans = []
        buckets = [[] for _ in range(len(nums) + 1)]
        
        #print "nums: ", nums
        #print "buckets (empty): ", buckets
        
        for num in nums:
            d[num] = d.get(num, 0) + 1
            
        #print "d: ", d
        
        for key in d:
            res.append((d[key], key))
            
        #print "res: ", res
        
        for t in res:
            freq, key = t
            buckets[freq].append(key)
            
        #print "buckets (inserted): ", buckets

        buckets.reverse()
        
        #print "buckets (reversed): ", buckets
        
        for item in buckets:
            if item and k > 0:
                while item and k > 0:
                    #print "item pop: ", item
                    ans.append(item.pop())
                    k -= 1
                    #print "buckets (now): ", buckets
                if k == 0:
                    return ans
                    
        return ans
        
if __name__ == "__main__":
    nums = [1,1,1,2,2,3]
    K = 2
    print(Solution().topKFrequent2(nums, K))