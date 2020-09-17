from sys import stdin


class Matrix:

    def __init__(self, lst):
        self.lst = [line.copy() for line in lst]
        self.lines = len(lst)
        self.columns = len(lst[0])

    def __str__(self):
        # output = ""
        # for line in self.lst:
        #     x = ["".join(str(x) + "\t" for x in line)]
        #     output += x.rstrip() + '\n'
        # output = output.rstrip()

        return '\n'.join(['\t'.join(map(str, line)) for line in self.lst])

    def size(self):
        return (self.lines, self.columns)


# m = Matrix([[1, 0], [0, 1]])
# print(m)
# m = Matrix([[2, 0, 0], [0, 1, 10000]])
# print(m)
# m = Matrix([[-10, 20, 50, 2443], [-5235, 12, 4324, 4234]])
# print(m)
exec(stdin.read())
