from charpy.matrix import Matrix


e = Matrix([
    [1, 2,],
    [6, 3,],
    [5, 4,],
])

e_rotated = e.rotated()
print(e_rotated)
quit()

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

