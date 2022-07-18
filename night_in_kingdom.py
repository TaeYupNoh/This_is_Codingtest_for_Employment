cur_pos=input()
moves = [(-2,-1),(-1,-2),(2,-1),(1,-2),(2,1),(1,2),(-2,1),(-1,2)]
cur_pos_alp=ord(cur_pos[0])-ord('a')+1
cur_pos_num=int(cur_pos[1:])

cnt = 0
for move in moves:
    pre_pos_alp = cur_pos_alp + move[0]
    pre_pos_num = cur_pos_num + move[1]

    if 1<=pre_pos_alp and pre_pos_alp<=8 and 1<=pre_pos_num and pre_pos_num<=8:
        cnt+=1
        print(pre_pos_alp,pre_pos_num)

print(cnt)
