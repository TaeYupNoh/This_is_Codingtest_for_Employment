# 1이 될 때까지 p.99
n, k = map(int, input().split())
cnt = 0

while True:
    well_did = (n//k)*k
    cnt += (n-well_did)
    n = well_did
    if n < k:
        break
    cnt += 1
    n //= k

cnt += (n-1)
print(cnt)

# 숫자가 커지면 1씩 계속 빼는 것 비효율적
# cnt = 0
# while n != 1:
#     if n % k != 0:
#         n -= 1
#         cnt += 1

#     else:
#         n //= k
#         cnt += 1

# print(cnt)
