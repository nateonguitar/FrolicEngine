from game.matrix import Matrix
from game.matrix_border import MatrixBorder

matrix1 = Matrix.empty_sized(rows=3, columns=4, value='.')
print(matrix1)
border = MatrixBorder()
print(border.apply(matrix1))


matrix2 = Matrix.empty_sized(rows=5, columns=5, value='°')
matrix2[2][2] = 'A'
border = MatrixBorder(sides=MatrixBorder.DOUBLE_LINE)
print(border.apply(matrix2))
print(matrix2)