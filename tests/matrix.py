from frolic.matrix import Matrix, Vector2


e = Matrix([
    [1, 2,],
    [6, 3,],
    [5, 4,],
])

e_rotated = e.rotated()
print(e_rotated)

a = Matrix([
    [1, 2, 3],
    [8, 0, 4],
    [7, 6, 5],
])
print(a)
assert a[0][0] == 1
assert a[0][1] == 2
assert a[0][2] == 3
assert a[1][0] == 8
assert a[1][1] == 0
assert a[1][2] == 4
assert a[2][0] == 7
assert a[2][1] == 6
assert a[2][2] == 5


print('')
a_rotated = a.rotated()
print('clockwize turn')
print(a_rotated)
assert a_rotated[0][0] == 7
assert a_rotated[0][1] == 8
assert a_rotated[0][2] == 1
assert a_rotated[1][0] == 6
assert a_rotated[1][1] == 0
assert a_rotated[1][2] == 2
assert a_rotated[2][0] == 5
assert a_rotated[2][1] == 4
assert a_rotated[2][2] == 3


print('')
a_rotated = a_rotated.rotated(clockwize=False)
print('counter clockwize turn')
print(a_rotated)
assert a_rotated[0][0] == 1
assert a_rotated[0][1] == 2
assert a_rotated[0][2] == 3
assert a_rotated[1][0] == 8
assert a_rotated[1][1] == 0
assert a_rotated[1][2] == 4
assert a_rotated[2][0] == 7
assert a_rotated[2][1] == 6
assert a_rotated[2][2] == 5

print('')
print('counter clockwize turn')
a_rotated = a_rotated.rotated(clockwize=False)
print(a_rotated)
assert a_rotated[0][0] == 3
assert a_rotated[0][1] == 4
assert a_rotated[0][2] == 5
assert a_rotated[1][0] == 2
assert a_rotated[1][1] == 0
assert a_rotated[1][2] == 6
assert a_rotated[2][0] == 1
assert a_rotated[2][1] == 8
assert a_rotated[2][2] == 7


print('')
b = Matrix.empty_sized()
print(b)
assert len(b) == 0


print('')
c = Matrix.empty_sized(rows=2, columns=1, value='X')
print(c)

print('')
d = Matrix.empty_sized(rows=3, columns=4, value='Dog')
print(d)

_e = [

]
for i in range(0, 10):
    row = []
    for j in range(10):
        row.append(str(i*10 + j).rjust(4, ' '))
    _e.append(row)

e = Matrix([
    ['a','b','c','d','e',],
    ['f','g','h','i','j',],
    ['k','l','m','n','o',],
    ['p','q','r','s','t',],
    ['u','v','w','x','y',],
])

print('1')
e_section1 = e.section(top_left=Vector2(y=1, x=1), bottom_right=Vector2(y=2, x=2))
print(e)
print(e_section1)
assert e_section1[0][0] == 'g'
assert e_section1[0][1] == 'h'
assert e_section1[1][0] == 'l'
assert e_section1[1][1] == 'm'

print('2')
e_section2 = e.section(top_left=Vector2(y=0, x=0), bottom_right=Vector2(y=1, x=4))
print(e_section2)
assert e_section2[0][0] == 'a'
assert e_section2[0][3] == 'd'
assert e_section2[1][3] == 'i'

print('3')
# going past the edges of the matrix should return Nones in those places
e_section3 = e.section(top_left=Vector2(-1, -1), bottom_right=Vector2(1, 1))
print(e_section3)
assert e_section3[0][0] == None
assert e_section3[0][1] == None
assert e_section3[0][2] == None
assert e_section3[1][0] == None
assert e_section3[1][1] == 'a'
assert e_section3[1][2] == 'b'
assert e_section3[2][0] == None
assert e_section3[2][1] == 'f'
assert e_section3[2][2] == 'g'


print('4')
# this should be all nones
e_section4 = e.section(top_left=Vector2(8, 8), bottom_right=Vector2(10, 10))
print(e_section4)
assert e_section4[0][0] == None
assert e_section4[0][1] == None
assert e_section4[0][2] == None
assert e_section4[1][0] == None
assert e_section4[1][1] == None
assert e_section4[1][2] == None
assert e_section4[2][0] == None
assert e_section4[2][1] == None
assert e_section4[2][2] == None

print('5')
# bordered by Nones since this goes of bounds on all sides
e_section5 = e.section(top_left=Vector2(-1, -1), bottom_right=Vector2(5, 5))
print(e_section5)
assert e_section5[0][0] == None
assert e_section5[0][1] == None
assert e_section5[0][2] == None
assert e_section5[0][3] == None
assert e_section5[0][4] == None
assert e_section5[0][5] == None
assert e_section5[0][6] == None

assert e_section5[1][0] == None
assert e_section5[1][1] == 'a'
assert e_section5[1][2] == 'b'
assert e_section5[1][3] == 'c'
assert e_section5[1][4] == 'd'
assert e_section5[1][5] == 'e'
assert e_section5[1][6] == None

assert e_section5[6][0] == None
assert e_section5[6][1] == None
assert e_section5[6][2] == None
assert e_section5[6][3] == None
assert e_section5[6][4] == None
assert e_section5[6][5] == None
assert e_section5[6][6] == None

print('6')
# go out of bounds on all sides but don't allow overflow, should get the original matrix back
e_section6 = e.section(top_left=Vector2(-1, -1), bottom_right=Vector2(5, 5), allow_overflow=False)
print(e_section6)

assert e_section6[0][0] == 'a'
assert e_section6[0][1] == 'b'
assert e_section6[0][2] == 'c'
assert e_section6[0][3] == 'd'
assert e_section6[0][4] == 'e'
assert e_section6[4][0] == 'u'
assert e_section6[4][1] == 'v'
assert e_section6[4][2] == 'w'
assert e_section6[4][3] == 'x'
assert e_section6[4][4] == 'y'

print('7')
# should be just the character at e[0][0] in the bottom right corner with the other 3 cells as None
e_section7 = e.section(top_left=Vector2(-1, -1), bottom_right=Vector2(0, 0),)
print(e_section7)
assert e_section7[0][0] == None
assert e_section7[0][1] == None
assert e_section7[1][0] == None
assert e_section7[1][1] == 'a'

print('8')
# should be just the character at e[0][0] since we don't allow out of bounds
e_section8 = e.section(top_left=Vector2(-1, -1), bottom_right=Vector2(0, 0), allow_overflow=False)
print(e_section8)
assert e_section8[0][0] == 'a'

A = Matrix([
    ['.', '.', '.', '.',],
    ['.', '.', '.', '.',],
    ['.', '.', '.', '.',],
    ['.', '.', '.', '.',],
])
X = Matrix([
    ['X', 'X',],
    ['X', 'X',],
])

print('9')
e_section9A = A.apply(X, Vector2(1, 1))
e_section9B = A.apply(X, Vector2(2, 2))
e_section9C = A.apply(X, Vector2(3, 3))
print(e_section9A)
assert e_section9A[0][0] == '.'
assert e_section9A[1][1] == 'X'
assert e_section9A[2][2] == 'X'
assert e_section9A[3][3] == '.'
print(e_section9B)
assert e_section9B[0][0] == '.'
assert e_section9B[1][1] == '.'
assert e_section9B[2][2] == 'X'
assert e_section9B[3][3] == 'X'
print(e_section9C)
assert e_section9C[0][0] == '.'
assert e_section9C[1][1] == '.'
assert e_section9C[2][2] == '.'
assert e_section9C[3][3] == 'X'

X = Matrix([
    [None, 'X',  'X',],
    [None, 'X',  'X',],
    [None, None, None],
])

print('10')
# A will pass no matter what, we've already done this in a prevous step.
# This is just showing a juxtaposition between apply_nones=False/True.
e_section10A = A.apply(X, Vector2(x=0, y=1), apply_nones=False)
e_section10B = A.apply(X, Vector2(x=0, y=1), apply_nones=True)
print('X', X)
print(e_section10A)
print(e_section10B)
assert e_section10B[0][0] == '.'
assert e_section10B[0][1] == '.'
assert e_section10B[0][2] == '.'
assert e_section10B[0][3] == '.'
assert e_section10B[1][0] == None
assert e_section10B[1][1] == 'X'
assert e_section10B[1][2] == 'X'
assert e_section10B[1][3] == '.'
assert e_section10B[2][0] == None
assert e_section10B[2][1] == 'X'
assert e_section10B[2][2] == 'X'
assert e_section10B[2][3] == '.'
assert e_section10B[3][0] == None
assert e_section10B[3][1] == None
assert e_section10B[3][2] == None
assert e_section10B[3][3] == '.'
