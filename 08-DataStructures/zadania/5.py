class matrix():

    @staticmethod
    def create(x,y):
        w, h = y, x
        return [[0 for x in range(w)] for y in range(h)]

    @staticmethod
    def print(matrix):
        for row in matrix:
            print(row)

m = matrix.create(4,3)
matrix.print(m)
