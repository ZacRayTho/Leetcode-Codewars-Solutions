class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        column = collections.defaultdict(set)
        row = collections.defaultdict(set)
        square = collections.defaultdict(set)
        
        for i in board:
            for j in i:
                print(j)
