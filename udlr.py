n=int(input())
move_lis=input().split()
def outchecker():
    global a,b,n
    if a <1 :
        a=1
    if a>n :
        a=n
    if b<1 :
        b=1
    if b>n :
        b=n

a,b = 1,1
for i in move_lis:
    if i == 'R':
        b+=1
    elif i == 'L':
        b-=1
    elif i == 'U':
        a-=1
    elif i == 'D':
        a+=1

    outchecker()

print(a,b)

