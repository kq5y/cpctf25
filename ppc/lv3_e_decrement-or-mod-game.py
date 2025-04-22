a, b = map(int, input().split())
# a>=b+2 は a%bの後 に b>a%b && a%b>=2 だと負けるため
if a == 1 or b == 1 or a == b or a >= b + 2:
    print("Alice")
else:
    print("Bob")
