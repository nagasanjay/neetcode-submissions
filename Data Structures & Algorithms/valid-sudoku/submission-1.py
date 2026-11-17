class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        columns = [0] * 9
        squares = [0] * 9

        for rowIndex in range(9):
            for colIndex in range(9):
                value = board[rowIndex][colIndex]

                if value == ".":
                    continue
                bitValue = 1 << int(value)

                if (rows[rowIndex] & bitValue) or (columns[colIndex] & bitValue):
                    return False
                
                if (squares[((rowIndex // 3) * 3 ) + (colIndex // 3)] & bitValue):
                    return False

                rows[rowIndex] |= bitValue
                columns[colIndex] |= bitValue
                squares[((rowIndex // 3) * 3 ) + (colIndex // 3)] |= bitValue

        return True


                