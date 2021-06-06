from charpy.matrix import Matrix, Vector2


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
e_section1 = e.section(top_left=Vector2(y=1, x=1), bottom_right=Vector2(y=2, x=2))
print(e)
print(e_section1)
assert e_section1[0][0] == 'g'
assert e_section1[0][1] == 'h'
assert e_section1[1][0] == 'l'
assert e_section1[1][1] == 'm'
e_section2 = e.section(top_left=Vector2(y=0, x=0), bottom_right=Vector2(y=1, x=4))
print(e_section2)
assert e_section2[0][0] == 'a'
assert e_section2[0][3] == 'd'
assert e_section2[1][3] == 'i'

# going past the edges of the matrix should return Nones in those places
e_section3 = e.section(top_left=Vector2(-1, -1), bottom_right=Vector2(1, 1))
print(e_section3)

# this should be all nones
e_section4 = e.section(top_left=Vector2(8, 8), bottom_right=Vector2(10, 10))
print(e_section4)

# bordered by Nones since this goes of bounds on all sides
e_section5 = e.section(top_left=Vector2(-1, -1), bottom_right=Vector2(5, 5))
print(e_section5)

# go out of bounds on all sides but don't allow overflow, should get the original matrix back
e_section6 = e.section(top_left=Vector2(-1, -1), bottom_right=Vector2(5, 5), allow_overflow=False)
print(e_section6)

# should be just the character at e[0][0] in the bottom right corner with the other 3 cells as None
e_section8 = e.section(top_left=Vector2(-1, -1), bottom_right=Vector2(0, 0),)
print(e_section8)

# should be just the character at e[0][0] since we don't allow out of bounds
e_section7 = e.section(top_left=Vector2(-1, -1), bottom_right=Vector2(0, 0), allow_overflow=False)
print(e_section7)

A = Matrix([
    [' ', ' ', ' ', ' ',],
    [' ', ' ', ' ', ' ',],
    [' ', ' ', ' ', ' ',],
    [' ', ' ', ' ', ' ',],
])
X = Matrix([
    ['X', 'X',],
    ['X', 'X',],
])
B = A.apply(X, Vector2(1, 1))
C = A.apply(X, Vector2(2, 2))
D = A.apply(X, Vector2(3, 3))

print(B)
print(C)
print(D)