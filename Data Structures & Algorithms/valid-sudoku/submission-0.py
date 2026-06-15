class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Condition 1: Check rows
        for i in range(9):
            row = [x for x in board[i] if x != "."]
            if len(set(row)) != len(row):   # ✅ check all rows, return False if any fails
                return False

        # Condition 2: Check columns
        for i in range(9):
            col = [board[row][i] for row in range(9) if board[row][i] != "."]
            if len(set(col)) != len(col):
                return False

        # Condition 3: Check 3x3 sub-boxes
        for box_row in range(3):
            for box_col in range(3):
                box = [
                    board[r][c]
                    for r in range(box_row*3, box_row*3 + 3)
                    for c in range(box_col*3, box_col*3 + 3)
                    if board[r][c] != "."
                ]
                if len(set(box)) != len(box):
                    return False

        return True
        
            
        