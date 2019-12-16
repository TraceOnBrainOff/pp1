class matrix():

    @staticmethod
    def create(x,y):
        w, h = y, x
        return [[0 for x in range(w)] for y in range(h)]

    @staticmethod
    def create_unit(x): #num of rows/columns
        matrix = []
        currIndex = 0
        for i in range(x):
            row = []
            for j in range(x):
                if j == currIndex:
                    row.append(1)
                else:
                    row.append(0)
            currIndex += 1
            matrix.append(row)    
        return matrix

    @staticmethod
    def print(matrix):
        for row in matrix:
            print(row)

m = matrix.create_unit(4)
matrix.print(m)
