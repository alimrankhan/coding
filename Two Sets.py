#Two Sets #https://cses.fi/problemset/task/1092
def twosets(n:int):
    # n= int(input())
    print(f'Two Sets: {n}')
    nsum= int((n*(n+1))/2)
    if(nsum&1):
        print('NO')
    else:
        print('YES')
        need_sum= int(nsum/2)
        each_sum= 0
        ans=[]
        for l in range(1,int((n+1)/2+1)):
            r= n-l+1
            # print(l,r)
            if each_sum== need_sum:
                break
            elif each_sum+l == need_sum:
                ans.append(l)
                each_sum+=l
            elif each_sum+r == need_sum:
                ans.append(r)
                each_sum+=r
            else:
                ans.append(l)
                ans.append(r)
                each_sum+= l+r 
        print(len(ans))
        for i in ans:
            print(i, end= ' ')
        print()
        print(n-len(ans))
        for i in range(1,n+1):
            if i not in ans:
                print(i,end=' ')
        print()
        print()
twosets(8)