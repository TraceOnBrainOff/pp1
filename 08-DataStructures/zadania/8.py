import random

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
    def fill_random(matrix, m, n):
        for row in matrix:
            for i in range(len(row)):
                row[i] = random.randrange(m,n+1)

    @staticmethod
    def transpose(matrix):
        transposedMatrix = []
        for column in range(len(matrix[0])):
            newRow = []
            for row in matrix:
                newRow.append(row[column])
            transposedMatrix.append(newRow)
        return transposedMatrix

    @staticmethod
    def print(matrix):
        for row in matrix:
            print(row)

m = matrix.create(3,5)
matrix.fill_random(m, 1,9)
matrix.print(m)
print()
m = matrix.transpose(m)
matrix.print(m)
