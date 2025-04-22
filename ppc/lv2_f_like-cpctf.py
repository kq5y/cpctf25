n = int(input())
s = input()
ans = 0
for i0 in range(n):
    for i1 in range(i0 + 1, n):
        for i2 in range(i1 + 1, n):
            for i3 in range(i2 + 1, n):
                for i4 in range(i3 + 1, n):
                    if (
                        len(set([s[i0], s[i1], s[i2], s[i3], s[i4]])) == 4
                        and s[i0] == s[i2]
                    ):
                        ans += 1
print(ans)
