class Solution(object):
    """
    O(m+n)
    Check the top-right corner.
    If it's not the target, then remove the top row or rightmost column.
    """
    def searchMatrix(self, matrix, target):
        if not matrix or len(matrix[0]) < 1:
            return False
        
        m, n = len(matrix), len(matrix[0])

        # We start search the matrix from top right corner
        # Initialize the current position to top right corner.
        
        row, col = 0, n - 1
        while row < m and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1
        return False