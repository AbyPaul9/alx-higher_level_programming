#!/usr/bin/python3


class Chess():
    __size = 0
    __matrix = []

    def __init__(self, prmSize=0):
        self.size = prmSize
        self.__matrix = self.__initMatrix(self.size)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, prmValue):
        if isinstance(prmValue, str) and prmValue.isnumeric():
            prmValue = int(prmValue)
        if not isinstance(prmValue, int):
            raise TypeError("N must be a number")
        if prmValue < 4:
            raise ValueError("N must be least 4")

        self.__size = prmValue

    def __generateNQueenSolution(self, prmMatrix, prmX, prmY=0):
        if prmX >= self.size:
            return True

        limit = self.size if prmY == 0 else prmY - self.size

        print("{}: {}".format(prmY, limit))
        for y in range(prmY, limit):
            if self.__isQueenSafe(prmMatrix, prmX, y):
                prmMatrix[y][prmX] = 1

                if self.__generateNQueenSolution(prmMatrix, prmX + 1) is True:
                    return True

                prmMatrix[y][prmX] = 0
        return False

    def __initMatrix(self, prmNumber=0):
        return [
            [0 for x in range(prmNumber)] for y in range(prmNumber)
        ]

    def __solveNQueen(self, prmMatrix=[], prmX=0, prmY=0):
        matrix = prmMatrix if len(prmMatrix) > 0 else self.__matrix.copy()
        result = []

        self.__generateNQueenSolution(matrix, prmX, prmY)

        for y in range(len(matrix)):
            for x in range(len(matrix)):
                if matrix[y][x] != 0:
                    result.append([x, y])

        return result

    def __isQueenSafe(self, prmMatrix, prmX, prmY):
        if not isinstance(prmX, int):
            raise TypeError("X must be a number")
        if not isinstance(prmY, int):
            raise TypeError("Y must be a number")

        return (self.__checkDiagonal(prmMatrix, prmX, prmY) and
                self.__checkRow(prmMatrix, prmX) and
                self.__checkColumn(prmMatrix, prmY))

    def __checkRow(self, prmMatrix, prmX):
        for y in range(self.size):
            if prmMatrix[y][prmX] == 1:
                return False
        return True

    def __checkColumn(self, prmMatrix, prmY):
        for x in range(self.size):
            if prmMatrix[prmY][x] == 1:
                return False
        return True

    def __checkDiagonal(self, prmMatrix, prmX, prmY):
        for row, column in zip(range(prmY, -1, -1), range(prmX, -1, -1)):
            if prmMatrix[row][column] == 1:
                return False
        for row, column in zip(range(prmY, self.size, 1), range(prmX, -1, -1)):
            if prmMatrix[row][column] == 1:
                return False
        return True

    def printSolvedMatrix(self):
        x = 0
        y = 0
        matrix = []
        for i in range(self.size):
            result = self.__solveNQueen(matrix, x, y)
            self.__printEnableCoordinatesMatrix(result)
            x, y = list(result[i])
            matrix = self.__initMatrix(self.size)
            # matrix[x][y] = 1
            # self.__printEnableCoordinatesMatrix(result)

    def __printEnableCoordinatesMatrix(self, prmMatrix=[]):
        for coordinate in prmMatrix:
            x, y = coordinate
            print("[{:d}, {:d}]".format(x, y), end='')

        print()


if __name__ == "__main__":
    import sys

    size = len(sys.argv)
    if (size - 1 != 1):
        print("Usage: nqueens N")
        sys.exit(1)

    chess = Chess(sys.argv[1])
    chess.printSolvedMatrix()
