n,m,k=map(int,input().split()) 
lis=list(map(int,input().split()))  
sor_lis=sorted(lis,reverse=True) 
res = 0

while m > 0:
    cnt_k=k
    while cnt_k>0:
        if m==0:
            print(res)
            quit()
        res+=sor_lis[0]
        cnt_k-=1
        m-=1
    res+=sor_lis[1]
    m-=1
print(res)