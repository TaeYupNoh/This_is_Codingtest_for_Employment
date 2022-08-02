# 미로 탈출 p.152
from collections import deque

n, m = map(int, input().split())
maze = [list(map(int, input())) for _ in range(n)]

da = [-1, 1, 0, 0]
db = [0, 0, -1, 1]


def bfs(a, b):
    queue = deque()
    queue.append((a, b))

    while queue:
        a, b = queue.popleft()
        for i in range(4):
            na = a+da[i]
            nb = b+db[i]

            if na < 0 or na > n-1 or nb < 0 or nb > m-1:
                continue
            if maze[na][nb] == 0:
                continue
            if maze[na][nb] == 1:
                maze[na][nb] = maze[a][b]+1
                queue.append((na, nb))

    return maze[n-1][m-1]


print(bfs(0, 0))
