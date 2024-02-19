class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        row, col, group1 = 0, 0, 0
        # for group in range(9):
        #     i = 0
        #     mat = {}

        # for row in range(row, row + 3):
        #     for col in range(col, col + 3):
        #         print(board[row][col])
        #         if board[row][col] not in mat:
        #             mat[i] = 1

        #         else:

        #             return False

        #         i += 1
        # print(row, col)

        while group1 < 3:
            mat = {}
            i = 0
            if row >= 8:
                rtemp = 0
            else:
                rtemp = row
            while row < rtemp + 3 and row < 9:
                if col >= 8:
                    ctemp = 0
                else:
                    ctemp = col
                while col < ctemp + 3 and col < 9:
                    if board[row][col] not in mat:
                        mat[i] = 1
                    else:
                        return False
                    i += 1
                    col += 1
                row += 1

        mat = {}
        for i in range(9):
            mat = {}
            for j in range(9):
                if board[i][j] not in mat:
                    mat[j] = 1
                else:
                    return False
        print(mat)

        for i in range(9):
            mat = {}
            for j in range(9):
                if board[j][i] not in mat:
                    mat[j] = 1
                else:
                    return False
        print(mat)

        return True


def main():
    board = [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    sol = Solution()

    sol.isValidSudoku(board)


if __name__ == "__main__":
    main()
