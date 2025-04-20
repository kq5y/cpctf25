from collections import defaultdict

n = int(input())
graph = defaultdict(list)
for _ in range(n - 1):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

parent = [0] * (n + 1)
order = []
stack = [1]
parent[1] = -1
while stack:
    u = stack.pop()
    order.append(u)
    for v, w in graph[u]:
        if parent[v] == 0:
            parent[v] = u
            stack.append(v)

best_down = [0] * (n + 1)
answer = 0

for u in reversed(order):
    first = 0
    second = 0
    for v, w in graph[u]:
        if v == parent[u]:
            continue
        c = best_down[v] + w
        if c > first:
            second = first
            first = c
        elif c > second:
            second = c
    if first < 0:
        first = 0
    if second < 0:
        second = 0
    answer = max(answer, first + second)
    best_down[u] = first

print(answer)
