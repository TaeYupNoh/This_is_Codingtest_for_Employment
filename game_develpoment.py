n,m=map(int,input().split())
a,b,direction = map(int,input().split())
visit_check = [[0]*m for _ in range(n)]

territory = []
for _ in range(n):
    territory.append(list(map(int,input().split())))

def turn_left():
    global direction
    direction -=1
    if direction < 0:
        direction = 3

da=[0,1,0,-1]
db=[-1,0,1,0]

# Start
turn_checker=0
visit_check[a][a] = 1
visit_cnt=1
while True:
    turn_left()
    turn_checker+=1
    na=a+da[direction]
    nb=b+db[direction]
    if visit_check[na][nb] == 0 and territory[na][nb]==0:
        visit_check[na][nb]=1
        a,b=na,nb
        visit_cnt+=1
        turn_checker=0
    if turn_checker==4:
        na=a-da[direction]
        nb=b-db[direction]
        if territory[na][nb]==1:
            break
        else:
            a,b=na,nb
            turn_checker=0

print(visit_cnt)
