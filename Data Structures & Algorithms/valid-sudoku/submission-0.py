class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for m in range(3):
            skip_row = m * 3
            for n in range(3):
                skip_column = n * 3
                sub_board = set([])
                for i in range(3):
                    for j in range(3):
                        item = board[skip_row+i][skip_column+j]
                        if not item in sub_board and not item == '.':
                            sub_board.add(item)
                        elif item in sub_board:
                            return False
        for i in range(9):
            sub_board = set([])
            for j in range(9):
                item = board[i][j]
                if not item in sub_board and not item == '.':
                    sub_board.add(item)
                elif item in sub_board:
                    return False
        for i in range(9):
            sub_board = set([])
            for j in range(9):
                item = board[j][i]
                if not item in sub_board and not item == '.':
                    sub_board.add(item)
                elif item in sub_board:
                    return False
        return True
                        