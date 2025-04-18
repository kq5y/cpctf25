n, k = list(map(int, input().split()))
s = [input() for _ in range(n)]
t = [input() for _ in range(n)]

ans = True

if k == 0:
    ans = s == t
for i in range(k):
    a = []
    b = []
    for j in range(i, n, k):
        a.append(s[j])
        b.append(t[j])
    a.sort()
    b.sort()
    if a != b:
        ans = False
        break

if ans:
    print("Yes")
else:
    print("No")
