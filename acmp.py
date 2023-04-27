# find next around number in a chessboard from 1 to 64

num = int(input())
if num == 1:
    print(2, 9)
elif num == 64:
    print(56, 63)
else: # print next numbers if they are positive and less than 64
    a = num - 8
    b = num - 1 if num % 8 != 1 else 0
    c = num + 1 if num % 8 != 0 else 0
    d = num + 8
    if 0 < a < 65:
        print(a, end=' ')
    if 0 < b < 65:
        print(b, end=' ')
    if 65 > c > 0:
        print(c, end=' ')
    if 65 > d > 0:
        print(d, end=' ')
        