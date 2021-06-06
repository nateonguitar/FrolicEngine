from charpy import Vector2
import colorama

GREEN = colorama.Fore.GREEN
RED = colorama.Fore.RED
BRIGHT = colorama.Style.BRIGHT
RESET_ALL = colorama.Style.RESET_ALL

print('\nVector2 Test\n')
try:
    v1 = Vector2(2, 4)
    v2 = Vector2(x=3, y=5)
    v3 = Vector2(y=4, x=6)
    test = 'v1.x == 2'
    assert(eval(test))
    test = 'v1.y == 4'
    assert(eval(test))
    test = 'v2.x == 3'
    assert(eval(test))
    test = 'v2.y == 5'
    assert(eval(test))
    test = 'v3.x == 6'
    assert(eval(test))
    test = 'v3.y == 4'
    assert(eval(test))
    print(f'{GREEN}{BRIGHT}PASSED:{RESET_ALL} assignment')
except:
    print(f'{RED}{BRIGHT}FAILED:{RESET_ALL} assignment "{test}"')


try:
    v1 = Vector2(x=3, y=4)
    v2 = v1.add(Vector2(x=2, y=3))
    test = 'v2.x == 5'
    assert(eval(test))
    test = 'v2.y == 7'
    assert(eval(test))
    print(f'{GREEN}{BRIGHT}PASSED:{RESET_ALL} add')
except:
    print(f'{RED}{BRIGHT}FAILED:{RESET_ALL} add "{test}"')


try:
    v1 = Vector2(x=3, y=4)
    v2 = v1.subtract(Vector2(x=2, y=1))
    test = 'v2.x == 1'
    assert(eval(test))
    test = 'v2.y == 3'
    assert(eval(test))
    print(f'{GREEN}{BRIGHT}PASSED:{RESET_ALL} subtract')
except:
    print(f'{RED}{BRIGHT}FAILED:{RESET_ALL} subtract "{test}"')


try:
    v1 = Vector2(x=3, y=4).scale(3)
    test = 'v1.x == 9'
    assert(eval(test))
    test = 'v1.y == 12'
    assert(eval(test))
    print(f'{GREEN}{BRIGHT}PASSED:{RESET_ALL} scale')
except:
    print(f'{RED}{BRIGHT}FAILED:{RESET_ALL} scale "{test}"')


try:
    v1 = Vector2(x=5, y=10).dot(Vector2(x=3, y=2))
    v2 = Vector2(x=2, y=3).dot(Vector2(x=-3, y=-5))
    v3 = Vector2(x=4, y=4).dot(Vector2(x=-1, y=1))
    test = 'v1 == 35'
    assert(eval(test))
    test = 'v2 == -21'
    assert(eval(test))
    test = 'v3 == 0'
    assert(eval(test))
    print(f'{GREEN}{BRIGHT}PASSED:{RESET_ALL} dot')
except:
    print(f'{RED}{BRIGHT}FAILED:{RESET_ALL} dot "{test}"')


try:
    v1 = Vector2(x=3, y=4).magnitude()
    test = 'v1 == 5'
    assert(eval(test))
    print(f'{GREEN}{BRIGHT}PASSED:{RESET_ALL} magnitude')
except:
    print(f'{RED}{BRIGHT}FAILED:{RESET_ALL} magnitude "{test}"')


try:
    equality1 = Vector2(x=5, y=10)
    equality2 = Vector2(x=5, y=10)
    test = 'equality1 == equality2'
    assert(eval(test))
    test = 'equality1 is not equality2'
    assert(eval(test))
    print(f'{GREEN}{BRIGHT}PASSED:{RESET_ALL} equality check')
except:
    print(f'{RED}{BRIGHT}FAILED:{RESET_ALL} equality check "{test}"')


try:
    clone1 = Vector2(x=5, y=10)
    clone2 = clone1.clone()
    test = 'clone1 == clone2'
    assert(eval(test))
    test = 'clone1 is not clone2'
    assert(eval(test))
    print(f'{GREEN}{BRIGHT}PASSED:{RESET_ALL} clone')
except:
    print(f'{RED}{BRIGHT}FAILED:{RESET_ALL} clone "{test}"')

print('')
