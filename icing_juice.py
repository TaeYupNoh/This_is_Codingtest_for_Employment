# 음료수 얼려 먹기 p.149
# n, m = map(int, input().split())
n, m = 4, 5
# 얼음틀 0,1 문자로 입력받음
case = [list(map(int, input())) for _ in range(n)]


def dfs(a, b):
    if a < 0 or a > n-1 or b < 0 or b > m-1:
        return False

    if case[a][b] == 0:
        case[a][b] = 1
        dfs(a-1, b)
        dfs(a+1, b)
        dfs(a, b-1)
        dfs(a, b+1)
        return True
    return False


result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)
