from sys import stdin


class MatrixError(Exception):

    def __init__(self, matrix1, matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2


class Matrix:

    def __init__(self, lst):
        self.lst = [line.copy() for line in lst]
        self.lines = len(lst)
        self.columns = len(lst[0])

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, line)) for line in self.lst])

    def size(self):
        return (self.lines, self.columns)

    def __add__(self, other):
        if self.size() != other.size():
            raise MatrixError(self, other)
        else:
            temp1 = [line.copy() for line in self.lst]
            temp2 = [line.copy() for line in other.lst]
            output = []
            for i in range(len(temp1)):
                output.append([x + y for x, y in zip(temp1[i], temp2[i])])
            return Matrix(output)

    def __mul__(self, other):
        temp = [line.copy() for line in self.lst]
        output = []
        for i in range(len(temp)):
            output.append([x * other for x in temp[i]])
        return Matrix(output)

    __rmul__ = __mul__

    def transpose(self):
        self.lst = list(map(list, zip(*self.lst)))
        return self

    @staticmethod
    def transposed(matrix):
        return Matrix(list(map(list, zip(*matrix.lst))))

exec(stdin.read())
