'''
Find the total area covered by two rectilinear rectangles in a 2D plane. Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

Assume that the total area is never beyond the maximum possible value of int.
https://github.com/xuelangZF/LeetCode/tree/master/Math
'''

class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        size_1 = (C-A) * (D-B)
        size_2 = (G-E) * (H-F)
        left = max(A, E)
        bottom = max(B, F)
        right = min(C, G)
        top = min(D, H)

        # There is an area coverd by both the two rectangle
        if left < right and bottom < top:
            return size_1 + size_2 - (top - bottom) * (right - left)
        else:
            return size_1 + size_2