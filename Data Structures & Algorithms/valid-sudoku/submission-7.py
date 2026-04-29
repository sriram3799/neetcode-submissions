class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        boxes = collections.defaultdict(set)
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    continue
                g = boxes[r//3,c//3]
                if val in row[r] or val in col[c] or val in g:
                    return False
                row[r].add(val)
                col[c].add(val)
                boxes[r//3,c//3].add(val)
        return True