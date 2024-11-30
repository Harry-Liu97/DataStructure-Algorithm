# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
# You must do it in place.

# Example 1:
# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]

# Example 2:
# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

# Constraints:
# m == matrix.length
# n == matrix[0].length
# 1 <= m, n <= 200
# -231 <= matrix[i][j] <= 231 - 1

class Solution:
    def setZeroes(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        '''
            Hash Array
        '''
        hash_list = []
        row_length = len(matrix)
        column_length = len(matrix[0])

        # Traverse all integers in the matrix and store the coordinates of 0s in the hash array
        for row in range(row_length):
            for column in range(column_length):
                if matrix[row][column] == 0:
                    hash_list.append((row, column))

        # Traverse the coordinates in the hash array
        for pos in hash_list:
            # Set all elements in the current row to 0
            cur_row = pos[0]
            cur_column = pos[1]
            while cur_row + 1 < row_length:
                cur_row += 1
                matrix[cur_row][cur_column] = 0

            # Set all elements in the current row to 0
            cur_row = pos[0]
            cur_column = pos[1]
            while cur_row - 1 >= 0:
                cur_row -= 1
                matrix[cur_row][cur_column] = 0

            # Set all elements in the current column to 0
            cur_row = pos[0]
            cur_column = pos[1]
            while cur_column + 1 < column_length:
                cur_column += 1
                matrix[cur_row][cur_column] = 0

            # Set all elements in the current column to 0
            cur_row = pos[0]
            cur_column = pos[1]
            while cur_column - 1 >= 0:
                cur_column -= 1
                matrix[cur_row][cur_column] = 0
            
        # Return the updated matrix
        return matrix

res = Solution()
print(res.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))