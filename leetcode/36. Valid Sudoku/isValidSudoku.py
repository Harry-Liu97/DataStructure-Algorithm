# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
# 1. Each row must contain the digits 1-9 without repetition.
# 2. Each column must contain the digits 1-9 without repetition.
# 3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

# Note:
# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.

# Example 1:
# Input: board = 
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true

# Example 2:
# Input: board = 
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

# Constraints:
# board.length == 9
# board[i].length == 9
# board[i][j] is a digit 1-9 or '.'.

class Solution:
    def isValidSudoku(self, board):
        '''
        Single traversal + hash arrays
        '''
        from math import floor
        # Create hash arrays for the three conditions
        hash_row = [[0] for _ in range(9)]
        hash_column = [[0] for _ in range(9)]
        hash_three = [[0] for _ in range(3)]

        # Traverse the elements in the board
        for row in range(9):
            for column in range(9):
                # Check the first condition
                # Numbers 1-9 must appear only once per row
                if board[row][column] not in hash_row[row]:
                    if board[row][column].isdigit():
                        hash_row[row].append(board[row][column])
                else:
                    return False

                # Check the second condition
                # Numbers 1-9 must appear only once per column
                if board[row][column] not in hash_column[column]:
                    if board[row][column].isdigit():
                        hash_column[column].append(board[row][column])
                else:
                    return False

                # Reset the hash array for the third condition to store new data
                if (row == 3 and column == 0) or (row == 6 and column == 0):
                    hash_three = [[0] for _ in range(3)]

                # Check the third condition
                # Numbers 1-9 must appear only once in each 3x3 sub-box
                if board[row][column] not in hash_three[floor(column / 3)]:
                    if board[row][column].isdigit():
                        hash_three[floor(column / 3)].append(board[row][column])
                else:
                    return False

        # If the loop completes, all conditions are satisfied
        return True

res = Solution()
print(res.isValidSudoku([["8","3",".",".","7",".",".",".","."]
                        ,["6",".",".","1","9","5",".",".","."]
                        ,[".","9","8",".",".",".",".","6","."]
                        ,["8",".",".",".","6",".",".",".","3"]
                        ,["4",".",".","8",".","3",".",".","1"]
                        ,["7",".",".",".","2",".",".",".","6"]
                        ,[".","6",".",".",".",".","2","8","."]
                        ,[".",".",".","4","1","9",".",".","5"]
                        ,[".",".",".",".","8",".",".","7","9"]]))
        