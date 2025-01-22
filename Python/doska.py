# Ввод координат первой и второй клетки
x1 = int(input(''))
y1 = int(input(''))
x2 = int(input(''))
y2 = int(input(''))

# Проверяем четность суммы координат обеих клеток
if (x1 + y1) % 2 == (x2 + y2) % 2:
    print("YES")
else:
    print("NO")

#-------slon--------

# Ввод координат первой и второй клетки
x1 = int(input(''))
y1 = int(input(''))
x2 = int(input(''))
y2 = int(input(''))

if abs(x1 - x2) == abs(y1 - y2):
    print("YES")
else:
    print("NO")

#-------kon6--------

# Ввод данных
a = int(input())
b = int(input())
c = int(input())
d = int(input())

# Условие, что клетки находятся в пределах доски (1-8)
if 1 <= a <= 8 and 1 <= b <= 8 and 1 <= c <= 8 and 1 <= d <= 8:
   
    if (abs(a-c)==2 and abs(b-d)==1) or (abs(a-c)==1 and abs(b-d)==2):
        print("YES")
    else:
        print("NO")
else:
    print("NO")

#-------fers6--------

# Ввод координат первой и второй клетки
x1 = int(input(''))
y1 = int(input(''))
x2 = int(input(''))
y2 = int(input(''))

# Проверяем, может ли ферзь попасть с первой клетки на вторую
if x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
    print("YES")
else:
    print("NO")

#-------korol6--------

a = int(input())
b = int(input())
c = int(input())
d = int(input())
if 1 <= a <= 8 and 1 <= b <= 8 and 1 <= c <= 8 and 1 <= d <= 8:
    if -1 <= c - a <= 1 and -1 <= d - b <= 1:
        print('YES')
    else:
        print('NO')
else:
    print('NO')

#-------lad6ya--------

# Ввод данных
a = int(input())
b = int(input())
c = int(input())
d = int(input())

# Условие, что клетки находятся в пределах доски (1-8)
if 1 <= a <= 8 and 1 <= b <= 8 and 1 <= c <= 8 and 1 <= d <= 8:
    # Ладья может ходить, если либо столбцы совпадают, либо строки
    if a == c or b == d:
        print("YES")
    else:
        print("NO")
else:
    print("NO")