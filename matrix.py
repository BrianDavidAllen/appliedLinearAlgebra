import random

class Matrix:

    def __init__ (self, name, row, col):
        self.row = row
        self.col = col
        self.name = name
        self.matrix = [[0 for x in range(0, col)] for y in range(0, row)]
    
    def print(self):
        print("Name: " + self.name)
        print("Number of rows: " + str(self.row) + "\nNumber of cols: " + str(self.col))
        for i in range(0, self.row):
            for j in range(0, self.col):
                print(self.matrix[i][j], end= ' ')
            print()

    def randomize(self, start, end):
        for i in range(0, self.row):
            for j in range(0, self.col):
                self.matrix[i][j] = random.randint(start, end)

    def multiply(self, matrixB):
        if self.col != matrixB.row:
            print("Matrices cannot be multipled. Matrix " + self.name + "'s number of columns do not match " + matrixB.name + "'s number of rows")
        
        resultMatrix = Matrix("result", self.row, matrixB.col)

        for i in range(0, self.row):
            for j in range(0, self.col):
                sum = 0
                for k in range(0, matrixB.col):
                    sum += self.matrix[i][k] * matrixB.matrix[j][k] 
                resultMatrix.matrix[i][j] = sum
        
        return resultMatrix

        
    
def main():
    matrixA = Matrix("A",5,5)
    matrixA.randomize(0,1)
    matrixA.print()
    result = matrixA.multiply(matrixA)
    result.print()
    


if __name__ == "__main__":
    main()
