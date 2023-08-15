class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        column = collections.defaultdict(set)
        row = collections.defaultdict(set)
        square = collections.defaultdict(set)
        
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue

                if board[i][j] in row[i]:
                    print(row[i])
                    print("row")
                    return False

                if board[i][j] in column[j]:
                    print("col")
                    return False

                if board[i][j] in square[(i // 3, j // 3)]:
                    print("square")
                    return False

                column[j].add(board[i][j])
                row[i].add(board[i][j])
                square[(i // 3, j // 3)].add(board[i][j])

        return True
                
