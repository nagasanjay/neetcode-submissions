class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict(set)
        squares = defaultdict(set)

        for rowIndex in range(9):
            for colIndex in range(9):
                value = board[rowIndex][colIndex]
                if value == ".":
                    continue
                
                if value in rows[rowIndex] or value in columns[colIndex] or value in squares[(rowIndex // 3, colIndex // 3)]:
                    return False

                rows[rowIndex].add(value)
                columns[colIndex].add(value)
                squares[(rowIndex // 3, colIndex // 3)].add(value)

        return True
