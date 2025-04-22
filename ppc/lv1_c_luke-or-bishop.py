gx, gy = list(map(int, input().split()))
if gx == 0 and gy == 0:
    print(0)
elif gx == 0 or gy == 0:
    print(1)
elif gx == gy or gx == -gy:
    print(1)
else:
    print(2)
