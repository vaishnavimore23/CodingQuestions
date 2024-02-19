class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead."""
        c = len(matrix[0]) - 1
        r = len(matrix) - 1

        zeroLocation = []
        for i in range(r + 1):
            for j in range(c + 1):
                if matrix[i][j] == 0:
                    zeroLocation.append((i, j))
        print(zeroLocation)
        for i in range(r + 1):
            for j in range(c + 1):
                if (i, j) in zeroLocation:
                    matrix[i][: c + 1] = [0] * (c + 1)
                    for k in range(r + 1):
                        print(matrix[k][j])
                        matrix[k][j] = 0
        print(matrix)


def main():
    obj = Solution()
    # matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    obj.setZeroes(matrix)


if __name__ == "__main__":
    main()
