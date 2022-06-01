t= int(input())
while(t>0):
    t=t-1
    n=int(input())
    li=list()
    ans= None
    li= list(map(int,input().split()))
    mi= min(li)
    ans= sum(li) - (mi*n)
    print(ans)