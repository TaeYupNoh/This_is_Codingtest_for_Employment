# 1로 만들기 p.217 (다이나믹 프로그래밍 연습) - 탑다운 방식
n = int(input())

cache = [0]*30001


def make(x):
    if x == 1:
        return 0
    if cache[x] > 0:
        return cache[x]

    cache[x] = make(x-1) + 1

    if x % 2 == 0:
        temp = make(x//2) + 1
        if cache[x] > temp:
            cache[x] = temp
    if x % 3 == 0:
        temp = make(x//3) + 1
        if cache[x] > temp:
            cache[x] = temp
    if x % 5 == 0:
        temp = make(x//5) + 1
        if cache[x] > temp:
            cache[x] = temp
    return cache[x]


print(make(n))
