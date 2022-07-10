import sys
input = sys.stdin.readline

m, n = map(int, input().split())
sor_lis = []

while m > 0:
    col_min = sorted(list(map(int, input().split())))[0]
    sor_lis.append(col_min)
    m -= 1

print(sorted(sor_lis)[-1])
