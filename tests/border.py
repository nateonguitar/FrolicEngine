from charpy.matrix import Matrix
from charpy.matrix_border import MatrixBorder

matrix1 = Matrix.empty_sized(rows=3, columns=4, value='.')
print(matrix1)
border = MatrixBorder()
print(matrix1.with_border(border))


matrix2 = Matrix.empty_sized(rows=5, columns=5, value='°')
matrix2[2][2] = 'A'
border = MatrixBorder(sides=MatrixBorder.DOUBLE_LINE)
print(matrix2.with_border(border))
print(matrix2)